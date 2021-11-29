import cx_Oracle
lib_dir = "C:\instantclient_21_3"
try:
    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    conexion= cx_Oracle.connect(user="ADMIN", password="Inacap2021.-", dsn="dbprueba_high")
    
    cursor = conexion.cursor()
   # data=cursor.execute("select * from docente")
   # data.fetchall()
   # print(cursor)
    for row in cursor.execute("select * from docente"):
        print(row)
        
except Exception as ex:
    print(ex)



