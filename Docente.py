from Conexion import Conexion


class docente:
    def agregarNota(self):
        ###ver modulos docente
        print("| ID |      Nombre Modulo      |")
        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select s.id_seccion, s.seccion, s.modalidad, c.carrera from seccion s "
            SQL0 = SQL0 + f"inner join carrera c on c.id_carrera=s.id_carrera "
            SQL0 = SQL0 + f"order by id_seccion ASC "
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex)
        seccion= int(input("Indique en que Seccion Desea Ingresar Nota: "))

        ###seleccion modulo acorde a docente   
        try:
            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select n.id_modulo, m.modulo from nota n "
            SQL0 = SQL0 + f"inner join modulo m on m.id_modulo=n.id_modulo "
            SQL0 = SQL0 + f"where n.id_seccion='{seccion}'"
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex)

        nmodulo= input("Indique en que modulo Desea Ingresar Nota: ")
        try:
            cn1= Conexion()
            cursor = cn1.conexion.cursor() 
            SQL0 = f"select n.id_nota, n.id_estudiante, e.nombres || ' '|| e.apellidop || ' '|| e.apellidom NombreAlumno from nota n "
            SQL0 = SQL0 + f"inner join estudiante e on n.id_estudiante=e.id_estudiante "
            SQL0 = SQL0 + f"where n.id_modulo='{nmodulo}'and n.id_seccion='{seccion}'"
            for row in cursor.execute(SQL0):
                print(row[1], row[2])
        except Exception as ex:
                print(ex)                           
        
        try:
            
            idestudiante= input("Indique el Id del estudiante para ingresar nota: ")
            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select n.id_nota, m.modulo, n.nota_1, n.nota_2, n.nota_3, n.nota_4, nota_examen from nota n "
            SQL0 = SQL0 + f"inner join modulo m on n.id_modulo=m.id_modulo "
            SQL0 = SQL0 + f"where n.id_estudiante='{idestudiante}' and n.id_seccion='{seccion}'"
            for row in cursor.execute(SQL0):
                    print("****************************************************")
                    print(f"{row[1]}")
                    print("*****************************************************")
                    print("                                                     ")   
                    print(f"Nota 1: {row[2]}                                    ")
                    print(f"Nota 2: {row[3]}                                    ")
                    print(f"Nota 3: {row[4]}                                    ")
                    print(f"Nota 4: {row[5]}                                    ")
                    print(f"Nota Examen: {row[6]}                               ")
                    print("                                                     ")  
            for row in cursor.execute(SQL0):
                print(row)
            
              
               
        except Exception as ex:
                print(ex)
            
        try:
            idnota=row[0]
            selecnota=int(input("Indique la Nota que desea ingresar(1-4-Examen): "))
            nota=int(input(f"Ingrese la nota '{selecnota}'"))
            

            cn1= Conexion()
            cursor = cn1.conexion.cursor()
            SQL0 = f"update nota set nota_{selecnota}='{nota}' where id_nota = {idnota} "
            
            cursor.execute(SQL0)
            cn1.conexion.commit()
            print("Nota ingresada con exito! ")
        except Exception as ex:
            print(ex)
   

    def modificarNota(self):

        print("| ID |      Nombre Modulo      |")
        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select s.id_seccion, s.seccion, s.modalidad, c.carrera from seccion s "
            SQL0 = SQL0 + f"inner join carrera c on c.id_carrera=s.id_carrera "
            SQL0 = SQL0 + f"order by id_seccion ASC "
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex)
        seccion= int(input("Indique en que Seccion Desea Modificar Nota: "))

        ###seleccion modulo acorde a docente   
        try:
            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select n.id_modulo, m.modulo from nota n "
            SQL0 = SQL0 + f"inner join modulo m on m.id_modulo=n.id_modulo "
            SQL0 = SQL0 + f"where n.id_seccion='{seccion}'"
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex)

        nmodulo= input("Indique en que modulo Desea Modificar Nota: ")
        try:
            cn1= Conexion()
            cursor = cn1.conexion.cursor() 
            SQL0 = f"select n.id_nota, n.id_estudiante, e.nombres || ' '|| e.apellidop || ' '|| e.apellidom NombreAlumno from nota n "
            SQL0 = SQL0 + f"inner join estudiante e on n.id_estudiante=e.id_estudiante "
            SQL0 = SQL0 + f"where n.id_modulo='{nmodulo}'and n.id_seccion='{seccion}'"
            for row in cursor.execute(SQL0):
                print(row[1], row[2])
        except Exception as ex:
                print(ex)                           
        
        try:
            
            idestudiante= input("Indique el Id del estudiante para Modificar nota: ")
            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select n.id_nota, m.modulo, n.nota_1, n.nota_2, n.nota_3, n.nota_4, nota_examen from nota n "
            SQL0 = SQL0 + f"inner join modulo m on n.id_modulo=m.id_modulo "
            SQL0 = SQL0 + f"where n.id_estudiante='{idestudiante}' and n.id_seccion='{seccion}'"
            for row in cursor.execute(SQL0):
                    print("****************************************************")
                    print(f"{row[1]}")
                    print("*****************************************************")
                    print("                                                     ")   
                    print(f"Nota 1: {row[2]}                                    ")
                    print(f"Nota 2: {row[3]}                                    ")
                    print(f"Nota 3: {row[4]}                                    ")
                    print(f"Nota 4: {row[5]}                                    ")
                    print(f"Nota Examen: {row[6]}                               ")
                    print("                                                     ")  
            for row in cursor.execute(SQL0):
                print(row)
            
              
               
        except Exception as ex:
                print(ex)
            
        try:
            idnota=row[0]
            selecnota=int(input("Indique la Nota que desea Modificar(1-4-Examen): "))
            nota=int(input(f"Ingrese la nota '{selecnota}'"))
            

            cn1= Conexion()
            cursor = cn1.conexion.cursor()
            SQL0 = f"update nota set nota_{selecnota}='{nota}' where id_nota = {idnota} "
            
            cursor.execute(SQL0)
            cn1.conexion.commit()
            print("Nota Modificar con exito! ")
        except Exception as ex:
            print(ex)


    def eliminarNota(self):
        
        print("| ID |      Nombre Modulo      |")
        try:

            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select s.id_seccion, s.seccion, s.modalidad, c.carrera from seccion s "
            SQL0 = SQL0 + f"inner join carrera c on c.id_carrera=s.id_carrera "
            SQL0 = SQL0 + f"order by id_seccion ASC "
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex)
        seccion= int(input("Indique en que Seccion Donde Desea Eliminar Nota: "))

        ###seleccion modulo acorde a docente   
        try:
            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select n.id_modulo, m.modulo from nota n "
            SQL0 = SQL0 + f"inner join modulo m on m.id_modulo=n.id_modulo "
            SQL0 = SQL0 + f"where n.id_seccion='{seccion}'"
            for row in cursor.execute(SQL0):
                print(row)
        except Exception as ex:
                print(ex)

        nmodulo= input("Indique en que modulo Donde Desea Eliminar Nota: ")
        try:
            cn1= Conexion()
            cursor = cn1.conexion.cursor() 
            SQL0 = f"select n.id_nota, n.id_estudiante, e.nombres || ' '|| e.apellidop || ' '|| e.apellidom NombreAlumno from nota n "
            SQL0 = SQL0 + f"inner join estudiante e on n.id_estudiante=e.id_estudiante "
            SQL0 = SQL0 + f"where n.id_modulo='{nmodulo}'and n.id_seccion='{seccion}'"
            for row in cursor.execute(SQL0):
                print(row[1], row[2])
        except Exception as ex:
                print(ex)                           
        
        try:
            
            idestudiante= input("Indique el Id del estudiante para eliminar nota: ")
            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select n.id_nota, m.modulo, n.nota_1, n.nota_2, n.nota_3, n.nota_4, nota_examen from nota n "
            SQL0 = SQL0 + f"inner join modulo m on n.id_modulo=m.id_modulo "
            SQL0 = SQL0 + f"where n.id_estudiante='{idestudiante}' and n.id_seccion='{seccion}'"
            for row in cursor.execute(SQL0):
                    print("****************************************************")
                    print(f"{row[1]}")
                    print("*****************************************************")
                    print("                                                     ")   
                    print(f"Nota 1: {row[2]}                                    ")
                    print(f"Nota 2: {row[3]}                                    ")
                    print(f"Nota 3: {row[4]}                                    ")
                    print(f"Nota 4: {row[5]}                                    ")
                    print(f"Nota Examen: {row[6]}                               ")
                    print("                                                     ")  
            for row in cursor.execute(SQL0):
                print(row)
            
              
               
        except Exception as ex:
                print(ex)
            
        try:
            idnota=row[0]
            selecnota=int(input("Indique la Nota que desea Eliminar(1-4-Examen): "))
            
            

            cn1= Conexion()
            cursor = cn1.conexion.cursor()
            SQL0 = f"update nota set nota_{selecnota}= null where id_nota = {idnota} "
            
            cursor.execute(SQL0)
            cn1.conexion.commit()
            print("Nota Eliminada con exito! ")
        except Exception as ex:
            print(ex)


