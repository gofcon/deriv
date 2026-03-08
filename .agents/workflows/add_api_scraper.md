---
description: How to add a new API Scraper to the deriv workspace
---

# Adding a new API Scraper

This workflow outlines how to add a new REST/WebSocket API scraper to the system without modifying any Python code.

## 1. Create an `ApiMst` Definition

The fundamental endpoint and its rules are defined in the `ApiMst` table.

- **`api_id`**: A unique string identifier (e.g., `kis_daily_price`)
- **`api_name`**: Human-readable name
- **`api_type`**: The category or provider of the API (e.g., `KIS`, `KRX`, `SEIBRO`)
- **`api_url`**: The endpoint endpoint URL. It can include parameterized variables.
- **`header_json`**: A dictionary containing static request headers needed for authentication or content type configuration (e.g., `{"tr_id": "FHKST01010400"}`).
- **`request_type`**: The HTTP Request method (`GET`, `POST`, `WEBSOCKET`, etc.).
- **`output_table_name`**: The exact model mapping (e.g., `KIS_DAILY_PRICE`).

## 2. Create `ApiParam` Rules (Optional)

If the API requires validation rules (e.g. max_length, allowed_values) for its dynamic parameters, define them in the `ApiParam` table linking to the `api_id`.

## 3. Schedule and Execution Queue

The actual runtime execution is split into two tables to provide clear audit logging:

### `ApiScheduleMst` (Templates & Macros)

For recurring API workloads, define a schedule:

- **`schedule_id`**: Unique string identifier
- **`api_id`**: Link to Step 1
- **`macro_params_json`**: Defines body payloads or query parameters. Supports dynamic macros (e.g. `{{this_month_start}}`) or list arrays (e.g. `["005930", "035420"]`).
- **`execution_cycle`**: How often the API should be called (`"daily"`, `"monthly"`, etc.)

### `ApiJobMst` (Execution Queue & History Logs)

When `generate_jobs.py` runs, it resolves macros and inserts concrete jobs into this table with `status="READY"`. It saves the history using `base_yymm`.

- **`job_id`**: PK (e.g. `<schedule>_<base_yymm>_<index>`)
- **`base_yymm`**: Indicates which batch generation cycle this job belongs to (e.g. `202603`).
- **`params_json`**: A fully resolved, literal dictionary used for validation and sent with the API request.
- **`is_active`**: Controls if the job is eligible for execution. Old batch jobs are set to `False` to maintain history without re-executing. _Note: Jobs running a `once` cycle will automatically set this to `False` upon SUCCESS._
- **`status`**: Tracked by the system (`READY` -> `RUNNING` -> `SUCCESS`/`FAIL`).

## 4. Register Data via Load Script

Add your configurations into a dummy data script like `scripts/setup/load_api_data.py` (or through DB inserts directly). Use `db.add_api_mst` and `db.add_api_job_mst` functions.

## 5. Generate Jobs and Execute

The execution lifecycle occurs in two phases:

1. **`python scripts/generate_jobs.py --base_yymm [YYYYMM]`**: This reads active Schedules from `ApiScheduleMst`, resolves all macros and arrays, sets old jobs from previous months to `is_active=False` (to preserve history without deletion), and inserts new concrete API calls into `ApiJobMst` with `status="READY"`.
2. **`python main.py --cycle [daily|monthly|etc]`**: The `APIManager` picks up `is_active=True` jobs that match the selected `execution_cycle` (or the `once` cycle) from `ApiJobMst`, performs HTTP requests, updates the job status (`SUCCESS` or `FAIL`), and stores data in the output table.

## 6. Advanced: Dynamic Macros and Arrays

You can generalize your `ApiScheduleMst` runtime parameters (`macro_params_json`) using the Dynamic Parameter Engine.
This allows a single Schedule definition to spawn multiple Job Queue items automatically.

### Date Macros

Instead of hardcoding `"start_date": "2025-12-01"`, you can use dynamic placeholders that resolve at runtime:

- `{{this_month_start}}`, `{{this_month_end}}`
- `{{last_month_start}}`, `{{last_month_end}}`
- `{{today}}`, `{{yesterday}}`

### Array Iteration

If you provide a **list** for any query parameter, `main.py` will automatically expand it into a Cartesian product and execute the API call multiple times sequentially.

**Example:**

```json
{
  "PDNO": ["005930", "035420"],
  "start_date": "{{last_month_start}}"
}
```

_Result: Automatically runs the API twice (first with Samsung Electronics + last month's date, then Naver + last month's date)._
