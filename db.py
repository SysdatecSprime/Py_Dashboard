import pyodbc
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

cnxngen = pyodbc.connect(
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

cnxndep = pyodbc.connect(
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

cnxnclass = pyodbc.connect(
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

cnxnweek = pyodbc.connect(
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

cnxnmonth = pyodbc.connect(
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