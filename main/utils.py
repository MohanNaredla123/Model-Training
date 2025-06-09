import os
from dotenv import load_dotenv

load_dotenv()

class ConnectionString:
    def __init__(self):
        self.driver = 'ODBC Driver 17 for SQL Server'
        self.server = os.getenv('SQL_SERVER')
        self.database = os.getenv('DATABASE')
        self.user_id = os.getenv('USER_ID', None)
        self.pwd = os.getenv('PASSWORD', None)


    def setup_connection_string(self, isWindowsAuthentication: bool=True) -> str:
        if isWindowsAuthentication:
            conn_str = (
                f"DRIVER={self.driver};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                "Trusted_Connection=yes;"
            )
        else:
            conn_str = (
                f"DRIVER={self.driver};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"UID={self.user_id};"
                f"PWD={self.pwd};"
            )

        return conn_str

