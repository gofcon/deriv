import sqlite3

def dump_full_schema(db_path='data/kis_api.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    tables = ['api_mst', 'api_job_mst', 'api_schedule_mst', 'SEIBRO_BOND_KACD_LIST']
    
    for table in tables:
        print(f"\n===== FULL SCHEMA FOR: {table} =====")
        try:
            cursor.execute(f"PRAGMA table_info({table})")
            columns = cursor.fetchall()
            for col in columns:
                # col format: (id, name, type, notnull, default_value, pk)
                print(f"ID: {col[0]} | Name: {col[1]:<20} | Type: {col[2]:<15} | NotNull: {col[3]} | Default: {col[4]} | PK: {col[5]}")
        except Exception as e:
            print(f"Error reading table {table}: {e}")
            
    conn.close()

if __name__ == "__main__":
    dump_full_schema()
