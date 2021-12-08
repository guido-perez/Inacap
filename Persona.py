

from Conexion import Conexion



class Persona:
    
    def Validacion(self, useraux):

        # Query para comparar el tipo de usuario si es 1) Estudiante  2) Docente  3) Jefe de Carrera
        # Para luego invocar a la clase correspondiente.
        nombre = input("Ingrese rut o correo: ")
        password = input("Ingrese una contraseña: ")

        if useraux == 'Estudiante':
                
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        
                        SQL = f"select contraseña from estudiante where rut = '{nombre}' or correo = '{nombre}' "
                        for row in cursor.execute(SQL): 
                         print(end="")

                        
                        print("\n****** Alumno Validado Correctamente *****\n")
                except Exception as ex:
                        print(ex)

        if useraux == 'Docente':
                
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        
                        SQL = f"select contraseña from docente where rut = '{nombre}' or correo = '{nombre}' "
                        for row in cursor.execute(SQL): 
                         print(end="")

                        
                        print("\n****** Docente Validado Correctamente *****\n")
                except Exception as ex:
                        print(ex)       

        if useraux == 'Jefe Carrera':
                
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        
                        SQL = f"select contraseña from jefecarrera where rut = '{nombre}' or correo = '{nombre}' "
                        for row in cursor.execute(SQL): 
                         print(end="")

                        
                        print("\n****** Jefe Carrera Validado Correctamente *****\n")
                except Exception as ex:
                        print(ex)

        if useraux == 'Administrador':
                
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        
                        SQL = f"select contraseña from administrador where rut = '{nombre}' or correo = '{nombre}' "
                        for row in cursor.execute(SQL): 
                         print(end="")

                        
                        print("\n****** Administrador Validado Correctamente *****\n")
                except Exception as ex:
                        print(ex)
        
    def ingresoUsuario(self):
            
        tipousuario= input("Ingrese tipo de usuario 'Docente o Jefe Carrera': ")    
        nombres = input(f"Ingrese Nombres del {tipousuario}: ")
        apellidoP = input(f"Ingrese Apellido Paterno del {tipousuario}: ")
        apellidoM = input(f"Ingrese Apellido Materno del {tipousuario}: ")
        rut = input(f"Ingrese Rut del {tipousuario} (Sin puntos): ")
        direccion = input(f"Ingrese Direccion del {tipousuario}: ")
        comuna = input(f"Ingrese Comuna del {tipousuario}: ")
        ciudad = input(f"Ingrese Ciudad del {tipousuario}: ")
        telefono = int(input(f"Ingrese Telefono del {tipousuario}: "))
        
        #Creacion de Correo
        cadena = nombres[:1]
        cadena2 = apellidoP[:3]
        cadena3 = apellidoM[:3]
        correo = cadena + cadena2 + cadena3 + "@inacapmail.cl" 
        correo = correo.lower()
               
        print("\n \n")
        print("\n        Listado Areas             ")
        print("")
        print("ID |        Nombre                    ")
        try: 
                cn0= Conexion()
                cursor = cn0.conexion.cursor()
                        
                SQL0 = f"select * from area "
                for row in cursor.execute(SQL0): 
                 print(row[0]," | ",row[1],"     | ", row[2])

        except Exception as ex:
                        print(ex) 
        
        print()
       # fechaInscripcion = input(f"Ingrese fechaInscripcion del {tipousuario}: ")
        idarea = int(input(f"Ingrese area para el {tipousuario}: "))
        
        try: 
                cn0= Conexion()
                cursor = cn0.conexion.cursor()
                        
                SQL0 = f"select nombre from area where id_area = '{idarea}'"
                for row in cursor.execute(SQL0): 
                 print(end="")
                nombre_area = row[0]
                
        except Exception as ex:
                        print(ex) 


        try: 
                cn0= Conexion()
                cursor = cn0.conexion.cursor()

                    
                SQL = f"select jc.id_jefecarrera from jefecarrera jc "
                SQL = SQL + f" inner join area a on jc.id_jefecarrera = a.id_area "
                SQL = SQL + f" where a.nombre = '{nombre_area}' "
                for row in cursor.execute(SQL): 
                 print(end="")
                idjefecarrera = row[0]

        except Exception as ex:
                        print(ex)
        
        #Creacion de contraseña
                    
        if len(rut) == 10:  
          contraseña = rut[:8]
        if len(rut) == 9:
         contraseña = rut[:7]
        
      
        if tipousuario=="Docente":
                
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        
                        SQL = f"insert into docente (tipousuario, nombres, apellidop, apellidom, rut, direccion, comuna, ciudad, telefono, correo, contraseña, id_jefecarrera, id_area) "
                        SQL = SQL + f" values ('{tipousuario}', '{nombres}', '{apellidoP}', '{apellidoM}', '{rut}', '{direccion}', '{comuna}', '{ciudad}', '{telefono}', "
                        SQL = SQL + f" '{correo}','{contraseña}', '{idjefecarrera}', '{idarea}') "
                        
                        #alter sequence estudiante_idestudiante_seq restart start with 1;
                        
                        cursor.execute (SQL)
                        cn.conexion.commit()
                        
                        print("\n****** Docente Ingresado Correctamente *****\n")
                        
                        # Intente un Last_Value e intente un :new o sql un last_insert_id()
                        

                except Exception as ex:
                        print(ex)

        elif tipousuario=="Jefe carrera":
                    
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        
                        SQL = "insert into jefecarrera (tipousuario, nombres, apellidop, apellidom, rut, direccion, comuna, ciudad, telefono, correo, contraseña, id_area) "
                        SQL = SQL + f" values ('{tipousuario}', '{nombres}', '{apellidoP}', '{apellidoM}', '{rut}', '{direccion}', '{comuna}', '{ciudad}', '{telefono}', "
                        SQL = SQL + f" '{correo}','{contraseña}', '{idarea}') "
                        
                        #alter sequence estudiante_idestudiante_seq restart start with 1;
                        
                        cursor.execute (SQL)
                        cn.conexion.commit()
                        
                        print("\n****** Jefe Carrera Ingresado Correctamente *****\n")
                        
                        # Intente un Last_Value e intente un :new o sql un last_insert_id()
                        

                except Exception as ex:
                        print(ex)

    def eliminarDocente(self):
                  
        print("\n \n")
        print("\n        Listado Docente             ")
        print("")
        print("ID |      Rut           |       Nombre                    ")
        try: 
                cn= Conexion()
                cursor = cn.conexion.cursor()
                        
                SQL = f"select id_docente, rut,  nombres, apellidop, apellidom from Docente "
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