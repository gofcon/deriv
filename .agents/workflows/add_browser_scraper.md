---
description: How to add a new Browser Scraper to the deriv workspace
---

# Adding a new Browser Scraper

This workflow outlines how to add a new Playwright-based browser scraper to the system without modifying any Python code. The architecture is driven by JSON configurations stored in the database.

## 1. Create a `BrowserMst` Definition

The target site and extraction rules are defined in the `BrowserMst` table.

- **`browser_id`**: A unique string identifier (e.g., `browser_krx_isin`)
- **`browser_name`**: Human-readable name
- **`target_url`**: The URL to scrape. Parameters from the job can be injected using `{param_name}` syntax.
- **`output_table_name`**: Set this to `"BROWSER_RST"` to save results dynamically without creating a new SQLAlchemy model.
- **`behavior_json` (List of Objects)**: Actions to perform _before_ scraping (e.g., typing into inputs, clicking search buttons).
  - Valid actions: `"click"`, `"input"`, `"wait"`, `"wait_for_selector"`
- **`selector_json` (Object)**: Defines what data to extract and map to keys.
  - Set `is_list: True` if you are extracting multiple items (like a grid/table).
- **`pagination_json` (Object)**: Defines how to handle multiple pages.
  - Dynamic pagination is supported by providing `total_items_selector` and `items_per_page`.
  - Provide `next_selector` to specify the next page button.

## 2. Schedule and Execution Queue

The actual execution is controlled by two distinct tables to provide clear audit trails:

### `BrowserScheduleMst` (Templates & Macros)

For recurring or macro-based workloads, define a schedule:

- **`schedule_id`**: Unique string identifier
- **`browser_id`**: Link to Step 1
- **`macro_params_json`**: Allows dynamic dates (e.g. `{{this_month_start}}`) or list expansion (e.g. `["KR1", "KR2"]`).
- **`execution_cycle`**: How often it runs (e.g. `"daily"`, `"monthly"`)

### `BrowserJobMst` (Execution Queue & History Logs)

When you run `generate_jobs.py`, it resolves the macros from `BrowserScheduleMst` and creates concrete jobs here with a `READY` status. It preserves the execution history per batch month.

- **`job_id`**: Primary Key (e.g. `<schedule>_<base_yymm>_<index>`)
- **`base_yymm`**: Indicates which batch generation cycle this job belongs to (e.g. `202603`).
- **`params_json`**: Fully resolved literal dictionary. No macros allowed here.
- **`is_active`**: Controls if the job is eligible for execution. Old batch jobs are set to `False` by the generator to maintain history without re-executing. _Note: Jobs running a `once` cycle will automatically set this to `False` upon SUCCESS._
- **`status`**: Tracked by the system (`READY` -> `RUNNING` -> `SUCCESS`/`FAIL`).

## 3. Register Data via Load Script

Add the Python definitions for `BrowserMst` and `BrowserJobMst` to `scripts/setup/load_browser_data.py` (or a similar data loader script) using `db.add_browser_mst` and `db.add_browser_job_mst`.

Run the loader script to insert the data into the Oracle database.

## 4. Generate Jobs and Execute

The execution now happens in two phases:

1. **`python scripts/generate_jobs.py --base_yymm [YYYYMM]`**: This reads active Schedules from `BrowserScheduleMst`, resolves all macros and arrays, sets old jobs from previous months to `is_active=False` (to preserve history without deletion), and inserts new concrete jobs into `BrowserJobMst` with `status="READY"`.
2. **`python main.py --cycle [daily|monthly|etc]`**: The `BrowserScraper` picks up `is_active=True` jobs that match the selected `execution_cycle` (or the `once` cycle) from `BrowserJobMst`, executes Playwright, updates the job status to `SUCCESS` or `FAIL` (and dynamically turns off `is_active` for `once` jobs), and stores data in `BrowserRst`.

## 5. Advanced: Dynamic Macros and Arrays

You can generalize your `BrowserScheduleMst` extracting parameters using the Dynamic Parameter Engine.
This allows a single Schedule definition to spawn multiple Job Queue items automatically.

### Date Macros

Instead of hardcoding `"start_date": "2025-12-01"`, you can use dynamic placeholders that resolve at runtime:

- `{{this_month_start}}`, `{{this_month_end}}`
- `{{last_month_start}}`, `{{last_month_end}}`
- `{{today}}`, `{{yesterday}}`

### Array Iteration

If you provide a **list** for a parameter, `main.py` will automatically expand it and run the entire scraping process multiple times (once for each item).

**Example:**

```json
{
  "search_keyword": ["KR1", "KR2"],
  "start_date": "{{last_month_start}}"
}
```

_Result: Automatically runs the scraper twice (first for KR1 with last month's date, then for KR2 with last month's date)._
