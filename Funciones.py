from Conexion import Conexion

class Funciones:

        #funciones Consulta
        def ListarMatriculas(self):

            try:

                cn0= Conexion()

                cursor = cn0.conexion.cursor()

                       

                SQL0 = f"select * from matricula "

                for row in cursor.execute(SQL0):

                 print(row)



            except Exception as ex:

                        print(ex)



        def ListarCarreras(self):

            try:

                cn0= Conexion()

                cursor = cn0.conexion.cursor()

                       

                SQL0 = f"select * from carrera "

                for row in cursor.execute(SQL0):

                 print(row)



            except Exception as ex:

                        print(ex)
        



        

        def ListarDocentes(self):

            try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()

                       

                SQL0 = f"select * from docente "

                for row in cursor.execute(SQL0):

                 print(row)



            except Exception as ex:

                        print(ex)
        
                    
        def ListarModulos(self):

            try:

                cn3= Conexion()

                cursor = cn3.conexion.cursor()

                       

                SQL0 = f"select distinct  id_modulo, modulo from modulo"

                for row in cursor.execute(SQL0):

                 print(row)



            except Exception as ex:

                        print(ex)



        #Funciones update.
        def AsignarModDoc(self):
            
            print("\n        Docentes Disponibles             ")
            print("")
            print("ID |        Nombre                    ")
           #listar Docentes
            try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()

                       

                SQL0 = f"select id_docente, nombres, apellidop, apellidom from docente "

                for row in cursor.execute(SQL0):

                 print(row[0]," | ",row[1]+ " " + row[2]+ " " + row[3])

                 



            except Exception as ex:

                        print(ex)
            

            iddocente= int(input("\nIndique Id del docente que desea asignarle un modulo: "))
            print("")
            #listar Modulos
            print("\n        Modulos Disponibles             ")
            print("")
            print("ID |        Nombre                    ")

            try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()

                       

                SQL0 = f"select id_modulo, modulo from modulo "

                for row in cursor.execute(SQL0):

                 print(row[0]," | ",row[1])

                 



            except Exception as ex:

                        print(ex)
            
            idmodulo= int(input("\nIndique el modulo que desea asignarle al docente: "))

            
            #ingreso de datos
            
            try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()

                       

                SQL0 = f"update modulo set id_docente='{iddocente}' "
                SQL0 = SQL0 + f" where id_modulo='{idmodulo}'"

                cursor.execute(SQL0)
                cn1.conexion.commit()

                print(" Modulo Asignado con exito...  ")              



            except Exception as ex:

                        print(ex)
        



        #Funciones Delete
        
