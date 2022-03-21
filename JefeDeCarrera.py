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
    
    def modificarDoc(self):
        print("| ID | Nombre y Apellido |  Rut  |  Telefono  |     Correo     | ID Area |")
        try:
            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select id_docente, nombres, apellidop, rut, telefono, correo, id_area from docente "
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex) 
        id_docente=int(input("indique ID Docente Para Cambiar Nombre: "))     
        newNombre=input("indique el nuevo nombre del Docente: ")  
        try:
            cn1= Conexion()
            cursor = cn1.conexion.cursor()  
            SQL0 = f"update docente set nombres='{newNombre}' where id_docente='{id_docente}' "
            cursor.execute(SQL0)
            cn1.conexion.commit()
            print(" Docente Actualizado con exito...  ")   
        except Exception as ex:
                print(ex)   


    def eliminarDocente(self):

            print("\n \n")
            print("\n Listado Docente ")
            print("")
            print("ID | Rut | Nombre ")
            try:
                cn= Conexion()
                cursor = cn.conexion.cursor()

                SQL = f"select id_docente, rut, nombres, apellidop, apellidom from Docente "
                for row in cursor.execute(SQL):
                    print(row[0]," | ",row[1]," | ",row[2]+" "+row[3]+" "+row[4] )



            except Exception as ex:
                print(ex)

            rut = input(f"\n Ingrese Rut Docente a Eliminar: ")

            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()



                SQL0 = f"delete from docente WHERE rut='{rut}' "



                cursor.execute(SQL0)
                cn1.conexion.commit()

                print("\n****** Docente Eliminado Correctamente *****\n")
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
            ###############################################################################

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


######################################
            #SECCIONES
#######################################

    def ListarSecciones(self):
        print("| ID | Nombre  |  Modalidad  |  ID Carrera |")
        try:
            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select id_seccion, seccion, modalidad, id_carrera from seccion "
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex)

    def CrearSeccion(self):
        print("|     Secciones Existentes |")
        print("| ID |   Nombre Seccion   |")
        
  
        while True: 
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                      
                SQL0 = f"select * from Seccion order by id_seccion ASC "
                for row in cursor.execute(SQL0):
                    print(row)
            except Exception as ex:
                    print(ex)

            seccion=input("Ingrese nombre de la nueva seccion: ")
            
            modalidad=input("Ingrese Modalidad (Vespertina/Diurna): ")

            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                      
                SQL0 = f"select id_jefe_carrera, nombres, apellidop from jefecarrera order by id_jefe_carrera ASC "
                for row in cursor.execute(SQL0):
                    print(row[0]," | ",row[1]," | ",row[2])
            except Exception as ex:
                    print(ex)
        
            id_jefecarrera= input("Indique el ID del Jefe de Carrera encargado de la nueva Seccion: ")

            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                      
                SQL0 = f"select id_carrera, carrera from carrera order by id_carrera ASC "
                for row in cursor.execute(SQL0):
                    print(row[0]," | ",row[1])
            except Exception as ex:
                    print(ex)
            
            id_carrera= input("Indique el ID de la carrera a la cual pertenecera la nueva Seccion: ")
        

            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                      
                SQL0 = f"insert into seccion (seccion, modalidad, id_jefe_carrera, id_carrera) values ('{seccion}', '{modalidad}','{id_jefecarrera}','{id_carrera}') "
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" ¡Seccion creada con exito! ")
                bandera=input("Desea ingresar otra Seccion?(s/n) ")
                if bandera== "s" or bandera== "S":
                    bandera== True
                elif bandera== "n" or bandera== "N":
                    break

            except Exception as ex:
                    print(ex)

    def modificarSeccion(self):
            print("| ID | Nombre  |  Modalidad  |  ID Carrera |")
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                      
                SQL0 = f"select id_seccion, seccion, modalidad, id_carrera from seccion "
                for row in cursor.execute(SQL0):
                    print(row[0]," | ",row[1]," | ",row[2]," | ",row[3])
            except Exception as ex:
                    print(ex)
            id_seccion=input("Indique ID de seccion que desea modificar: ")
            nombrenuevo=input("Indique el nuevo nombre para la Seccion: ")

            try:
                cn1= Conexion()

                cursor = cn1.conexion.cursor()                     
                SQL0 = f"update seccion set seccion='{nombrenuevo}' "
                SQL0 = SQL0 + f" where id_seccion='{id_seccion}'"
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Seccion Modificada con exito...  ")   
            except Exception as ex:
                    print(ex)

    def eliminarSeccion(self):

            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                      
                SQL0 = f"select id_seccion, seccion, modalidad, id_carrera from seccion "
                for row in cursor.execute(SQL0):
                    print(row[0]," | ",row[1]," | ",row[2]," | ",row[3])
            except Exception as ex:
                    print(ex)
            id_seccion=input("Indique ID de seccion que desea Eliminar: ")

            try:
                cn1= Conexion()

                cursor = cn1.conexion.cursor()                     
                SQL0 = f"delete from seccion where id_seccion='{id_seccion}' "
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Seccion Eliminada con exito...  ")   
            except Exception as ex:
                    print(ex)




        ######################################33
                #Seccion y Docentes
        #####################################

    
    def asignarSecDoc(self):
        ###listar Docentes
        ###elegir docente
        ###listar seccion
        ###asignar seccion
        print("| ID | Nombre y Apellido |  Rut  |  Telefono  |     Correo     | ID Area |")
        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select id_docente, nombres, apellidop, rut, telefono, correo, id_area from docente "
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex)
        docente= input(" Indique El ID del docente para asignarle Seccion: ")

        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select id_seccion, seccion, modalidad from seccion order by id_seccion ASC "
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex)
        idseccion= input(" Indique el ID de Seccion que desea asignarle al Docente: ")

        try:

            cn1= Conexion()

            cursor = cn1.conexion.cursor()                   
            SQL0 = f"insert into carga_seccion (id_seccion, id_docente) values ('{idseccion}', '{docente}')"               
            cursor.execute(SQL0)
            cn1.conexion.commit()
            print(" Seccion Asignada con exito...  ")  
        except Exception as ex:
            print(ex)           

    def modificarSECDOC(self):

        print("| ID | Nombre y Apellido |  Rut  |")
        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select id_docente, nombres, apellidop, rut from docente "
            for row in cursor.execute(SQL0):
                print(row[0],"  |  ",row[1],"  |  ",row[2],"  |  ",row[3],"  |  ")
        except Exception as ex:
                print(ex)
        docente= input(" Indique El ID del docente que desea cambiar de Seccion: ")

        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select c.id_carga_seccion, d.id_docente, d.nombres , d.apellidop, s.seccion from docente d "
            SQL0 = SQL0 + f"inner join carga_seccion c on c.id_docente = d.id_docente "
            SQL0 = SQL0 + f"inner join seccion s on s.id_seccion = c.id_seccion "
            SQL0 = SQL0 + f"where d.id_docente= '{docente}'"
            for row in cursor.execute(SQL0):
                print(row[0],"  |  ",row[2],"  |  ",row[3],"  |  ",row[4])
        except Exception as ex:
                print(ex)
        idcarga= input(" Indique el ID del registro que desea cambiar la seccion: ")    

        print("| ID | Nombre  |  Modalidad  |  ID Carrera |")
        try:
            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select id_seccion, seccion, modalidad, id_carrera from seccion "
            for row in cursor.execute(SQL0):
                print(row[0],"  |  ",row[1],"  |  ",row[2],"  |  ")
        except Exception as ex:
                print(ex) 
        id_seccion= input("Indique la nueva seccion que desea asignale al Docente: ")   

        try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()                   
                SQL0 = f"update carga_seccion set id_seccion='{id_seccion}' where id_docente='{docente}' and id_carga_seccion='{idcarga}'"                
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Seccion Del Docente Modificada con exito...  ")  
        except Exception as ex:
                print(ex)  

    def eliminarSECDOC(self):

        print("| ID | Nombre y Apellido |  Rut  |")
        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select id_docente, nombres, apellidop, rut from docente "
            for row in cursor.execute(SQL0):
                print(row[0],"  |  ",row[1],"  |  ",row[2],"  |  ",row[3],"  |  ")
        except Exception as ex:
                print(ex)
        docente= input(" Indique El ID del docente que desea elimnarle la Seccion: ")

        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select c.id_carga_seccion, d.id_docente, d.nombres , d.apellidop, s.seccion from docente d "
            SQL0 = SQL0 + f"inner join carga_seccion c on c.id_docente = d.id_docente "
            SQL0 = SQL0 + f"inner join seccion s on s.id_seccion = c.id_seccion "
            SQL0 = SQL0 + f"where d.id_docente= '{docente}'"
            for row in cursor.execute(SQL0):
                print(row[0],"  |  ",row[2],"  |  ",row[3],"  |  ",row[4])
        except Exception as ex:
                print(ex)
        idcarga= input(" Indique el ID del registro que desea Eliminar: ")    

        print("| ID | Nombre  |  Modalidad  |  ID Carrera |") 

        try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()                   
                SQL0 = f"delete from carga_seccion where id_docente='{docente}' and id_carga_seccion='{idcarga}'"                
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Seccion Eliminada Del Docente con exito...  ")  
        except Exception as ex:
                print(ex) 



                ################################
                ##Secciones Estudiante
                ################################
    
    def asignarSECEST(self):
        
        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select id_estudiante, nombres, apellidop, rut from estudiante "
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex)
        estudiante= input(" Indique El ID del Estudiante para asignarle Seccion: ")


        #actualizar notas con seccion y docente

        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select s.id_seccion, c.id_carga_seccion, d.id_docente, d.nombres , d.apellidop, s.seccion from docente d "
            SQL0 = SQL0 + f"inner join carga_seccion c on c.id_docente = d.id_docente "
            SQL0 = SQL0 + f"inner join seccion s on s.id_seccion = c.id_seccion "
            for row in cursor.execute(SQL0):
                print(row[1],"  |  ",row[3], row[4],"  |  ", row[5])
            
        except Exception as ex:
                print(ex)
        idcarga= input(" Indique el ID del registro que contenga la Seccion y Docente para asignarle al estudiante: ")
        
        
        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select s.id_seccion, c.id_carga_seccion, d.id_docente, d.nombres , d.apellidop, s.seccion from docente d "
            SQL0 = SQL0 + f"inner join carga_seccion c on c.id_docente = d.id_docente "
            SQL0 = SQL0 + f"inner join seccion s on s.id_seccion = c.id_seccion "
            SQL0 = SQL0 + f"where c.id_carga_seccion='{idcarga}'"
            for row in cursor.execute(SQL0):
                pass
            docente=row[2] 
            seccion=row[0]
        except Exception as ex:
            print(ex)

        try:
            cn1= Conexion()
            cn1.conexion.cursor()
            SQL0= f"select id_docente, id_seccion from carga_seccion where id_carga_seccion='{idcarga}'"
            for row in cursor.execute(SQL0):
                pass
                

        except Exception as ex:
            print(ex)
        for idnota in cursor.execute("SELECT id_nota FROM Nota WHERE id_nota=(SELECT max(id_nota) FROM Nota)"):
            idnota = idnota[0]
        try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()                     
                SQL0 = f"update nota set id_seccion='{seccion}', id_docente= '{docente}' where id_nota = '{idnota}'"
            
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Seccion Asignada con exito...  ")              

        except Exception as ex:

                print(ex)
        #Actualizar estudiante con su seccion
        try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()                     
                SQL0 = f"update estudiante set id_seccion='{seccion}' where id_estudiante='{estudiante}'"
            
                cursor.execute(SQL0)
                cn1.conexion.commit()            

        except Exception as ex:

                print(ex)


    def modificarSECEST(self):

        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select id_estudiante, nombres, apellidop, rut from estudiante "
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex)
        estudiante= input(" Indique El ID del Estudiante para Modificar Seccion: ")

        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select n.id_nota, e.nombres, e.apellidop , s.seccion from nota n "
            SQL0 = SQL0 + f"inner join estudiante e on e.id_estudiante = n.id_estudiante "
            SQL0 = SQL0 + f"inner join seccion s on s.id_seccion = n.id_seccion "
            SQL0 = SQL0 + f"where e.id_estudiante= '{estudiante}'"
            for row in cursor.execute(SQL0):
                print(row[0],"  |  ",row[1], row[2],"  |  ", row[3])
            
        except Exception as ex:
                print(ex)
        carga= input("Indique el registro que Desea Modificar Seccion: ")

        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select s.id_seccion, d.id_docente, d.nombres , d.apellidop, s.seccion from docente d "
            SQL0 = SQL0 + f"inner join carga_seccion c on c.id_docente = d.id_docente "
            SQL0 = SQL0 + f"inner join seccion s on s.id_seccion = c.id_seccion "
            for row in cursor.execute(SQL0):
                print(row[0],"  |  ",row[1],"  |  ", row[4])
            
        except Exception as ex:
                print(ex)
        seccion= input("Indique la nueva seccion para el estudiante: ")
        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select s.id_seccion, d.id_docente, d.nombres , d.apellidop, s.seccion from docente d "
            SQL0 = SQL0 + f"inner join carga_seccion c on c.id_docente = d.id_docente "
            SQL0 = SQL0 + f"inner join seccion s on s.id_seccion = c.id_seccion "
            SQL0 = SQL0 + f"where s.id_seccion='{seccion}'"
            for row in cursor.execute(SQL0):
                print(row[0],"  |  ", row[1],"  |  ", row[4])
            
        except Exception as ex:
                print(ex)
        docente= row[1]

        try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()                     
                SQL0 = f"update nota set id_seccion='{seccion}', id_docente= '{docente}' where id_nota = '{carga}'"
            
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print(" Seccion Modificada con exito...  ")              

        except Exception as ex:

                print(ex)



## sadasdasdaad ##


