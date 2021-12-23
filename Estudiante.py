from Conexion import Conexion



class Estudiante:
    useraux= ''
    
    def verModulos(self, Rut):
        
        #rut = input("Ingrese rut o correo: ")
        
        try: 
            cn= Conexion()
            cursor = cn.conexion.cursor()
            SQL = f"select n.id_nota, e.nombres || ' '|| e.apellidop || ' '|| e.apellidom NombreAlumno, m.modulo from nota n "
            SQL = SQL + f" inner join modulo m on m.id_modulo = n.id_modulo "
            SQL = SQL + f" where e.rut='{Rut}' "
   
            contador= 0
            for row in cursor.execute(SQL): 
                contador = contador + 1
            if contador > 1:
                    print("******************************************************")
                    print(f"Listado Modulos Estudiante : {row[1]}                     ") 
                    print("*****************************************************")
                    print("                                                     ") 
                    contador2= 0 
                    for i in cursor.execute(SQL):
                        contador2= contador2 + 1
                        print(f"Modulo {contador2}: {i[2]}")
                    print(f"\nEl Alumno tiene asignado un total de {contador2} Modulos \n ")
                    print("*****************************************************")
                    
        except Exception as ex:
            print(ex)

    def verNotas(self, Rut):
            
            
            try:
                cn= Conexion()
                cursor = cn.conexion.cursor()                      
                SQL = f"select DISTINCT n.id_estudiante, e.nombres || ' '|| e.apellidop || ' '|| e.apellidom NombreAlumno, c.carrera from nota n "
                SQL = SQL + f" inner join estudiante e on e.id_estudiante = n.id_estudiante "
                SQL = SQL + f"inner join matricula m on m.id_estudiante=e.id_estudiante "
                SQL = SQL + f"inner join carrera c on c.id_carrera=m.id_carrera "
                SQL = SQL + f"where e.rut='{Rut}' "
                contador = 0
                for row in cursor.execute(SQL):
                    print(row[0]," | ",row[1],"     | ", row[2])

            except Exception as ex:
                    print(ex)
                    
            try:
                idest= input("✧ Indique su ID de estudiante para ver sus notas: \n")
                
                cn= Conexion()
                cursor = cn.conexion.cursor()                      
                SQL = f"select m.modulo, n.nota_1, n.nota_2, n.nota_3, n.nota_4, nota_examen from nota n "
                SQL = SQL + f"inner join modulo m on n.id_modulo=m.id_modulo "
                SQL = SQL + f"where id_estudiante='{idest}' "
                for row in cursor.execute(SQL):
                        print("****************************************************")
                        print(f"{row[0]}")
                        print("*****************************************************")
                        print("                                                     ")   
                        print(f"Nota 1: {row[1]}                                    ")
                        print(f"Nota 2: {row[2]}                                    ")
                        print(f"Nota 3: {row[3]}                                    ")
                        print(f"Nota 4: {row[4]}                                    ")
                        print(f"Nota Examen: {row[5]}                               ")
                        print("                                                     ")  

            except Exception as ex:
                    print(ex)
