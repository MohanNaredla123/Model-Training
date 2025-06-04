from data import ConnectionString

import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus


conn_str_builder = ConnectionString()
conn_str = conn_str_builder.setup_connection_string()
params = quote_plus(conn_str)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

try:
    df = pd.read_sql("SELECT * FROM dbo.AttendanceData", engine)
    print(df.head(5))

except Exception as e:
    print(f"Unable to Connect to SQL Server: {e}")