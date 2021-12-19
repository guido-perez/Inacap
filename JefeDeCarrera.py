from Conexion import Conexion


class jefeDeCarrera:

    #Docentes
    def ListarDocentes(self):
        print("| ID | Nombre y Apellido |  Rut  |  Telefono  |     Correo     | ID Area |")
        try:
            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select id_docente, nombres, apellidop, rut, telefono, correo, id_area from docente "
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex)

 #########################################################################################   
    #Modulos
    def VerModulosSis(self):
        print("| ID |      Nombre Modulo      |")
        try:
            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select * from modulo order by id_modulo ASC"
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex)

    def CrearModulo(self):
        print("|     Modulos Existentes |")
        print("| ID |   Nombre Modulo   |")
        
  
        while True: 
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                      
                SQL0 = f"select * from Modulo order by id_modulo ASC "
                for row in cursor.execute(SQL0):
                    print(row)
            except Exception as ex:
                    print(ex)

            nombre=input("Ingrese nombre de nuevo modulo: ")
            
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                      
                SQL0 = f"insert into Modulo (modulo) values ('{nombre}') "
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" ¡Modulo creado con exito! ")
                bandera=input("Desea ingresar otro modulo?(s/n) ")
                if bandera== "s" or bandera== "S":
                    bandera== True
                elif bandera== "n" or bandera== "N":
                    break

            except Exception as ex:
                    print(ex)
               
    def modificarModulo(self):
            print("|     Modulos Existentes |")
            print("| ID |   Nombre Modulo   |")
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                      
                SQL0 = f"select * from Modulo order by id_modulo ASC "
                for row in cursor.execute(SQL0):
                    print(row)
            except Exception as ex:
                    print(ex)

            modulo=input("Indique Id del Modulo que desea modificar: ")
            nombreNuevo=input("indique el nuevo nombre para el modulo seleccionado: ")

            try:
                cn1= Conexion()

                cursor = cn1.conexion.cursor()                     
                SQL0 = f"update modulo set modulo='{nombreNuevo}' "
                SQL0 = SQL0 + f" where id_modulo='{modulo}'"
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Modulo Modificado con exito...  ")   
            except Exception as ex:
                    print(ex)

    def EliminarModulo(self):

            print("|     Modulos Existentes |")
            print("| ID |   Nombre Modulo   |")
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                      
                SQL0 = f"select * from Modulo order by id_modulo ASC "
                for row in cursor.execute(SQL0):
                    print(row)
            except Exception as ex:
                    print(ex)

            modulo=input("Indique Id del Modulo que desea Eliminar: ")
            
            try:
                cn1= Conexion()

                cursor = cn1.conexion.cursor()                     
                SQL0 = f"delete from modulo where id_modulo='{modulo}' "
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Modulo Eliminado con exito...  ")   
            except Exception as ex:
                    print(ex)

            ###############################################################################
    #Docentes

    def AsignarModDoc(self):
            
            print("\n        Docentes Disponibles             ")
            print("")
            print("ID |        Nombre                    ")
           #listar Docentes
            try:

                cn1= Conexion()
                cursor = cn1.conexion.cursor()                      
                SQL0 = f"select id_docente, nombres, apellidop, apellidom from docente order by id_docente ASC "
                for row in cursor.execute(SQL0):

                 print(row[0]," | ",row[1]+ " " + row[2]+ " " + row[3])

            except Exception as ex:
                        print(ex)
            

            id_docente= int(input("\nIndique Id del docente que desea asignarle un modulo: "))
            print("")
            #listar Modulos
            print("\n        Modulos Disponibles             ")
            print("")
            print("ID |        Nombre                    ")

            try:

                cn1= Conexion()
                cursor = cn1.conexion.cursor()
                SQL0 = f"select id_modulo, modulo from modulo order by id_modulo ASC"
                for row in cursor.execute(SQL0):
                 print(row[0]," | ",row[1])

            except Exception as ex:
                        print(ex)
            
            id_modulo= int(input("\nIndique el modulo que desea asignarle al docente: "))
         
            try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()                     
                SQL0 = f"insert into carga_modulo (id_docente, id_modulo) values ('{id_docente}','{id_modulo}')"
                
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Modulo Asignado con exito...  ")              



            except Exception as ex:

                        print(ex)
    
    def modificarModuloDoc(self):
                    
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                     
                SQL0 = f"select id_docente, nombres, apellidop from docente order by id_docente ASC"
                for row in cursor.execute(SQL0):
                 print(row[0]," | ",row[1]," | ",row[2])

                id_docente=input("Indique el Id del docente que desea modificar modulo: ")

            except Exception as ex:
                print(ex)

            
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                     
                SQL0 = f"select c.id_carga_modulo, d.id_docente, d.nombres , d.apellidop, m.modulo from docente d "
                SQL0 = SQL0 + f"inner join carga_modulo c on c.id_docente = d.id_docente "
                SQL0 = SQL0 + f"inner join modulo m on m.id_modulo = c.id_modulo "
                SQL0 = SQL0 + f"where d.id_docente= '{id_docente}'"
                
                for row in cursor.execute(SQL0):         
                 print(row[0]," | ",row[2]," | ",row[3]," | ",row[4])
                
                id_carga = int(input("\ningrese id del registro a modificar: "))

                
                
            except Exception as ex:
                print(ex)  
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                     
                SQL0 = f"select * from modulo order by id_modulo ASC"
                for row in cursor.execute(SQL0):
                 print(row[0]," | ",row[1])

                id_modulo= input("indique Modulo(ID) que desea asignarle al Docente: ")
            except Exception as ex:
                print(ex)  
             
            try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()                   
                SQL0 = f"update carga_modulo set id_modulo='{id_modulo}' where id_docente='{id_docente}' and id_carga_modulo='{id_carga}'"                
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Modulo Modificado con exito...  ")  
            except Exception as ex:
                print(ex)             


    def eliminarMODDOC(self):

            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                     
                SQL0 = f"select id_docente, nombres, apellidop from docente order by id_docente ASC"
                for row in cursor.execute(SQL0):
                 print(row[0]," | ",row[1]," | ",row[2])

                id_docente=input("Indique el Id del docente al cual Eliminarle un modulo: ")

            except Exception as ex:
                print(ex)

            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                     
                SQL0 = f"select c.id_carga_modulo, d.id_docente, d.nombres , d.apellidop, m.modulo from docente d "
                SQL0 = SQL0 + f"inner join carga_modulo c on c.id_docente = d.id_docente "
                SQL0 = SQL0 + f"inner join modulo m on m.id_modulo = c.id_modulo "
                SQL0 = SQL0 + f"where d.id_docente= '{id_docente}'"
                
                for row in cursor.execute(SQL0):         
                 print(row[0]," | ",row[2]," | ",row[3]," | ",row[4])
                
                id_carga = int(input("\ningrese id del registro a Eliminar: "))

                
                
            except Exception as ex:
                print(ex) 

            try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()                   
                SQL0 = f"delete from carga_modulo where id_docente='{id_docente}' and id_carga_modulo='{id_carga}'"                
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Modulo Eliminado Del Docente con exito...  ")  
            except Exception as ex:
                print(ex)  

    #################################################
            #ESTUDIANTES
    #################################################

    def AsignarModEst(self):
            
            print("\n        Estudiantes Disponibles             ")
            print("")
            print("ID |        Nombre                    ")
           #listar Docentes
            try:

                cn1= Conexion()
                cursor = cn1.conexion.cursor()                      
                SQL0 = f"select id_estudiante, nombres, apellidop, apellidom from estudiante order by id_estudiante ASC "
                for row in cursor.execute(SQL0):

                 print(row[0]," | ",row[1]+ " " + row[2]+ " " + row[3])

            except Exception as ex:
                        print(ex)
            

            id_estudiante= int(input("\nIndique Id del estudiante que desea asignarle un modulo: "))
            print("")
            #listar Modulos
            print("\n        Modulos Disponibles             ")
            print("")
            print("ID |        Nombre                    ")

            try:

                cn1= Conexion()
                cursor = cn1.conexion.cursor()
                SQL0 = f"select id_modulo, modulo from modulo order by id_modulo ASC"
                for row in cursor.execute(SQL0):
                 print(row[0]," | ",row[1])

            except Exception as ex:
                        print(ex)
            
            id_modulo= int(input("\nIndique el modulo que desea asignarle al estudiante: "))
         
            try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()                     
                SQL0 = f"insert into nota (id_modulo, id_estudiante) values ('{id_modulo}','{id_estudiante}')"
                
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Modulo Asignado con exito...  ")              



            except Exception as ex:

                        print(ex)
    
    def modificarModuloEst(self):
                    
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                     
                SQL0 = f"select id_estudiante, nombres, apellidop from estudiante order by id_estudiante ASC "
                for row in cursor.execute(SQL0):
                 print(row[0]," | ",row[1]," | ",row[2])

                id_estudiante=input("Indique el Id del Estudiante que desea modificar modulo: ")

            except Exception as ex:
                print(ex)

            
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                     
                SQL0 = f"select n.id_nota, e.id_estudiante, e.nombres , e.apellidop, m.modulo from estudiante e "
                SQL0 = SQL0 + f"inner join nota n on e.id_estudiante = n.id_estudiante "
                SQL0 = SQL0 + f"inner join modulo m on m.id_modulo = n.id_modulo "
                SQL0 = SQL0 + f"where e.id_estudiante= '{id_estudiante}'"
                
                for row in cursor.execute(SQL0):         
                 print(row[0]," | ",row[2]," | ",row[3]," | ",row[4])
                
                id_nota = int(input("\ningrese id del registro a modificar: "))

                
                
            except Exception as ex:
                print(ex)  
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                     
                SQL0 = f"select * from modulo order by id_modulo ASC"
                for row in cursor.execute(SQL0):
                 print(row[0]," | ",row[1])

                id_modulo= input("indique Modulo(ID) que desea asignarle al Estudiante: ")
            except Exception as ex:
                print(ex)  
             
            try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()                   
                SQL0 = f"update nota set id_modulo='{id_modulo}' where id_estudiante='{id_estudiante}' and id_nota='{id_nota}'"                
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Modulo Modificado con exito...  ")  
            except Exception as ex:
                print(ex)             


    def eliminarMODEST(self):

            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                     
                SQL0 = f"select id_estudiante, nombres, apellidop from estudiante order by id_estudiante ASC"
                for row in cursor.execute(SQL0):
                 print(row[0]," | ",row[1]," | ",row[2])

                id_estudiante=input("Indique el Id del Estudiante al cual Eliminarle un modulo: ")

            except Exception as ex:
                print(ex)

            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                     
                SQL0 = f"select n.id_nota, e.id_estudiante, e.nombres , e.apellidop, m.modulo from estudiante e "
                SQL0 = SQL0 + f"inner join nota n on e.id_estudiante = n.id_estudiante "
                SQL0 = SQL0 + f"inner join modulo m on m.id_modulo = n.id_modulo "
                SQL0 = SQL0 + f"where e.id_estudiante= '{id_estudiante}'"
                
                for row in cursor.execute(SQL0):         
                 print(row[0]," | ",row[2]," | ",row[3]," | ",row[4])
                
                id_nota = int(input("\ningrese id del registro a Eliminar: "))

                
                
            except Exception as ex:
                print(ex) 

            try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()                   
                SQL0 = f"delete from nota where id_estudiante='{id_estudiante}' and id_nota='{id_nota}'"                
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Modulo Eliminado Del Estudiante con exito...  ")  
            except Exception as ex:
                print(ex)      