import cx_Oracle

class Conexion:
    
    
    lib_dir = "C:\instantclient_21_3"
    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    conexion= cx_Oracle.connect(user="ADMIN", password="Inacap2021.-", dsn="dbprueba_high")