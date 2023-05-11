import pyodbc
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

cnxn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server}; SERVER= "
    + config.get('database', 'server')
    + "; DATABASE="
    + config.get('database', 'database')
    + "; UID="
    + config.get('database', 'username')
    + "; PWD="
    + config.get('database', 'password')
    + "; TrustServerCertificate=yes"
    + "; max_pool_size="
    + config.get('database', 'max_pool_size')
)

def open_conn():
    return cnxn