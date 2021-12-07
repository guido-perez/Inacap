
from Conexion import Conexion

class Nota:
    idCarrera=''

    def MostrarCarrera(self):
        try: 
            cn= Conexion()
            cursor = cn.conexion.cursor()
                
            SQL = "select notas from modulos "
            

               
            for row in cursor.execute(SQL): 
               print(row)

        except Exception as ex:
                print(ex)

        
        idEstudiante = int(input("\nSelecciona ID carrara para Matricularse: "))
        Matricula.idCarrera=idEstudiante
        
        Matricula.carrera= row[1]
        Matricula.area=row[2]
