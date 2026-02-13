# KIS API Batch Execution System (v4.0)

## 📋 Overview

A database-driven application for executing Korea Investment & Securities (KIS) APIs in batches.
Version 4.0 introduces **Output Tables**, allowing API responses to be automatically stored in structured database tables.

### Key Features

- **Database-Centric**: All API definitions, user inputs, and **output data** are stored in `kis_api.db` (SQLite).
- **Auto-Generated Schema**: Output table schemas (`models.py`) are automatically generated from source code (`chk_*.py`).
- **Dynamic Data Loading**: `load_api_data.py` scans the repository to populate API definitions and link them to output tables.
- **Batch Execution**: Execute all active programs and save results to their respective tables.

---

## 🏗 Architecture

```mermaid
graph TD
    DB[(kis_api.db)] <--> DM[DatabaseManager]
    DM <--> AM[APIManager]

    subgraph "Preparation"
        SRC[Source Code (chk_*.py)] -->|extract_column_mappings.py| JSON[column_mappings.json]
        JSON -->|generate_output_models.py| MODELS[models.py]
        SRC -->|load_api_data.py| DB
    end

    subgraph "Execution"
        AM -->|Validate| V[Validation Engine]
        AM -->|Execute| HTTP[KISHttpClient]
        HTTP -->|Request| KIS[KIS REST API]
        HTTP -->|Response| DF[DataFrame]
        DF -->|Insert| DB
    end

    User -->|python main.py| AM
    User -->|python load_api_data.py| DB
```

---

## 📂 File Structure

| File                         | Purpose                                                                   |
| ---------------------------- | ------------------------------------------------------------------------- |
| `main.py`                    | **Entry Point**. Batch execution & data storage.                          |
| `database.py`                | **Data Access**. Manages APIs, Inputs, and **Output Data Insertion**.     |
| `models.py`                  | **Data Models**. API/Input definitions + **60+ Output Tables**.           |
| `load_api_data.py`           | **Loader**. Scans repo to load API definitions & mapping info.            |
| `extract_column_mappings.py` | **Extractor**. Scans `chk_*.py` to find `COLUMN_MAPPING`.                 |
| `generate_output_models.py`  | **Generator**. Creates `SQLModel` classes from mappings.                  |
| `init_database.py`           | **Initializer**. Recreates DB and creates all tables (including Outputs). |
| `kis_auth.py`                | **Auth**. Token management.                                               |
| `kis_http.py`                | **HTTP Client**. API calls.                                               |
| `insert_master_data.py`      | **Master Data**. Downloads & inserts 16 types of master data.             |
| `scripts/run_daily.sh`       | **Deployment**. Wrapper script for daily execution via cron/systemd.      |

---

## 📚 Master Data System

A dedicated subsystem for managing static master data (Stock Codes, Futures, Options, etc.).

### 1. Master Data Tables (`app/models.py`)

- **16 Master Tables**: `DomFutureMst`, `OverStockMst`, `DomBondMst`, etc.
- **Metadata Tables**: SQLite doesn't support comments, so we use custom tables:
  - `meta_table_mst`: Stores table descriptions.
  - `meta_column_mst`: Stores column descriptions and enum values.

### 2. Data Loading (`insert_master_data.py`)

- **Process**:
  1.  **Download**: Fetches `.zip` files from KIS CDN.
  2.  **Extract**: Unzips to `temp_master_data_full`.
  3.  **Parse**: Reads fixed-width data (`.mst`, `.cod`) based on spec.
  4.  **Insert**: Uses `MasterDatabaseManager` to bulk insert (overwrite mode).
  5.  **Metadata Update**: Scans `SQLModel` definitions to populate metadata tables.
  6.  **Cleanup**: Auto-deletes temporary files after success.

---

## 🚀 Usage

### 1. Setup & Model Generation (One-time or Update)

If source code (`chk_*.py`) changes or you want to add new APIs:

1.  **Extract Mappings**:

    ```bash
    python extract_column_mappings.py
    ```

    - Scans `temp_repo` for `COLUMN_MAPPING`.
    - Generates `column_mappings.json`.

2.  **Generate Models**:

    ```bash
    python generate_output_models.py
    ```

    - Reads `column_mappings.json`.
    - Generates `generated_output_models.py`.
    - **Action**: Copy the content to `models.py`.

3.  **Initialize Database**:

    ```bash
    python init_database.py
    ```

    - Creates `kis_api.db` with all tables.

4.  **Load API Definitions**:

    ```bash
    python load_api_data.py
    ```

    - Scans `temp_repo` for `.py` files.
    - Populates `api_definitions` table.
    - Links programs to output tables (e.g., `inquire_price` -> `stock_price`).

---

### 2. Batch Execution (Daily Operation)

Run the main script to execute active APIs and store data.

```bash
python main.py
```

- **Process**:
  1.  Authenticates with KIS.
  2.  Fetches active programs from DB.
  3.  Calls API.
  4.  **Stores result DataFrame into the corresponding Output Table** (e.g., `stock_price` table).

---

### 3. Verify Data

Check the data in the database:

```bash
python verify_data.py
# or
sqlite3 kis_api.db "SELECT * FROM stock_price;"
```

---

## 💻 Code Reference

### `models.py` (Output Models)

Output tables are `SQLModel` classes generated dynamically.

```python
class StockPrice(SQLModel, table=True):
    __tablename__ = "stock_price"
    id: Optional[int] = Field(default=None, primary_key=True)
    program_name: str = Field(index=True)
    # ... columns from COLUMN_MAPPING ...
    stck_prpr: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
```

### `load_api_data.py` (Alias Mapping)

Handles naming differences between files and logical program names.

```python
ALIASES = {
    "inquire_price": "stock_price",
    "inquire_daily_price": "daily_price",
}
```

This ensures `chk_inquire_price.py` maps to the `stock_price` table.

---

## ☁️ Deployment & Scheduling (Oracle Cloud/Fedora)

Scripts are provided in the `scripts/` directory for automated daily execution.

### 1. File Manifest

- `scripts/run_cycle.sh`: Universal wrapper script. Usage: `./run_cycle.sh <cycle>`
- `scripts/kis-api-5min.service/timer`: 5-minute interval execution.
- `scripts/kis-api-1hour.service/timer`: 1-hour interval execution.
- `scripts/kis-api-daily.service/timer`: Daily execution (05:00 AM).

### 2. Job Configuration (`JobMst`)

Each job in the database now has an `execution_cycle` field:

- `5min`: Executed by `kis-api-5min` timer.
- `1hour`: Executed by `kis-api-1hour` timer.
- `daily`: Executed by `kis-api-daily` timer.

### 3. Setup Guide

1.  **Upload**: Copy project to `/home/opc/deriv`.
2.  **Permission**: `chmod +x scripts/run_cycle.sh`
3.  **Register Systemd Units**:

    ```bash
    # Copy all unit files
    sudo cp scripts/kis-api-*.service /etc/systemd/system/
    sudo cp scripts/kis-api-*.timer /etc/systemd/system/

    # Reload and Enable
    sudo systemctl daemon-reload
    sudo systemctl enable --now kis-api-5min.timer
    sudo systemctl enable --now kis-api-1hour.timer
    sudo systemctl enable --now kis-api-daily.timer
    ```

    sudo systemctl enable --now kis-api-daily.timer

    ```

    ```

4.  **Monitor**: `journalctl -u kis-api-5min.service -f`

### 4. Customizing Execution Windows (Time Restrictions)

To restrict execution to specific times (e.g., Stock Market Hours), edit the `.timer` files:

**Example: `scripts/kis-api-5min.timer`**

```ini
[Timer]
# Run Mon-Fri, from 08:30 to 16:00, every 5 minutes
OnCalendar=Mon..Fri *-*-* 08:30..16:00/5:00
```

**Example: `scripts/kis-api-1hour.timer`**

```ini
[Timer]
# Run Mon-Fri, from 09:00 to 16:00, every hour
OnCalendar=Mon..Fri *-*-* 09..16:00:00
```

User `systemctl daemon-reload` after editing timer files.

---

## 🔄 Migration Guide: SQLite to Oracle Cloud ADB

### 1. Dependencies

Add `oracledb` to `requirements.txt`:

```bash
pip install oracledb>=2.0.0
```

### 2. Configuration (`app/config.py`)

Replace file path logic with Oracle connection parameters. Use environment variables for security.

```python
# app/config.py
import os

DB_TYPE = os.getenv("DB_TYPE", "sqlite")  # 'sqlite' or 'oracle'

# SQLite
DB_PATH = os.path.join(BASE_DIR, "data", "kis_api.db")

# Oracle ADB
ORACLE_USER = os.getenv("ORACLE_USER", "admin")
ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")
ORACLE_DSN = os.getenv("ORACLE_DSN", "db2024_high")
ORACLE_WALLET_DIR = os.getenv("TNS_ADMIN")  # Path to unzipped wallet
```

### 3. Database Connection (`app/database.py`, `app/db_mst.py`)

Update `create_engine` logic to support both types.

```python
def get_engine():
    if DB_TYPE == "oracle":
        # python-oracledb Thin Mode (Requires TNS_ADMIN for Wallet)
        db_url = f"oracle+oracledb://{ORACLE_USER}:{ORACLE_PASSWORD}@{ORACLE_DSN}"
        return create_engine(db_url)
    else:
        return create_engine(f"sqlite:///{DB_PATH}")
```

### 4. Systemd Environment

Update `scripts/kis-api.service` to include Oracle environment variables:

```ini
[Service]
Environment="DB_TYPE=oracle"
Environment="TNS_ADMIN=/usr/lib/oracle/wallet"
EnvironmentFile=/home/opc/deriv/.env
...
```
