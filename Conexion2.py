#       CONEXION  Nº2  CON  BD
#          PYTHON -  ORACLE
#En el CMD hay que desempaquetar la conexión con oracle "pip install cx_Oracle" /(Para ponerlo hay que activar la opción PAT cuando se instale python)
#Se importa desde la carpeta de python  la librería para conectarse a  Python con Oracle
import  cx_Oracle;
#Se limpia la pantalla
from os import system;
system("cls");
class ConexionOra():
    # (): es una puerta
    #Se crea la conexión a la BD en el constructo
    def __init__(self):
               
        self.connection=cx_Oracle.connect(
            user="SNunez",
            password="654321",
            dsn="localhost/xe"      
            #dsn = Data Source Name ( Nombre de la funte de los datos )
            #dsn="localhost:1521/xe"  #1521 = Este es el puerto que oracle  que trae por defecto.
           
        );
         # Se crea el cursor para conectarse a la BD y realizar consultas de datos
        self.AA = self.connection.cursor();
        print("\n=========================================================");
        print(" . . . . . . Conexión Establecida a la BD  . . . . . . !!! ");
        print("===========================================================\n");
    def Listado1(self):
       
        try:        
            self.AA.execute("Select * From  Alumnos");  
            Busque = self.AA.fetchall(); # Devuelve todos los registros de la consulta y los almacena en la variable Busque
            #Busque = self.AA.fetchone();  # Devuelve solo un  registros de la consulta , solo el primer registro
            print(" " );
            print(" Los datos de los Alumnos son  :\n",Busque );
            print(" " );
        except Exception:
            print("\n==============================================");
            print("....... Error  en la Consulta  Realizado ....... ");
            print("==============================================\n");
   