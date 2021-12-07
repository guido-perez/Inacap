

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
                        
                        SQL = f"select contraseña from jefecarrera where rut = '{nombre}' or correo = '{nombre}' "
                        for row in cursor.execute(SQL): 
                         print(end="")

                        
                        print("\n****** Jefe Carrera Validado Correctamente *****\n")
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
        
        print("\n \n")
        
        try: 
                cn0= Conexion()
                cursor = cn0.conexion.cursor()
                        
                SQL0 = f"select * from carrera "
                for row in cursor.execute(SQL0): 
                 print(end="")

        except Exception as ex:
                        print(ex)
        
        print()
       # fechaInscripcion = input(f"Ingrese fechaInscripcion del {tipousuario}: ")
        idcarrera = input(f"Ingrese carrera para el {tipousuario}: ")
        
        #Creacion de Correo
        cadena = nombres[:1]
        cadena2 = apellidoP[:3]
        cadena3 = apellidoM[:3]
        correo = cadena + cadena2 + cadena3 + "@inacapmail.cl" 
        correo = correo.lower()
            
        #Creacion de contraseña
                    
        if len(rut) == 10:  
          contraseña = rut[:8]
        if len(rut) == 9:
         contraseña = rut[:7]
        
        try: 
                cn= Conexion()
                cursor = cn.conexion.cursor()
                
                SQL = "insert into {tipousuario} (tipousuario, nombres, apellidop, apellidom, rut, direccion, comuna, ciudad, telefono, correo, contraseña, idjefecarrera idcarrera) "
                SQL = SQL + f" values ('{tipousuario}', '{nombres}', '{apellidoP}', '{apellidoM}', '{rut}', '{direccion}', '{comuna}', '{ciudad}', '{telefono}', "
                SQL = SQL + f" '{correo}','{contraseña}', '{Matricula.idCarrera}', '{idcarrera}'') "
                
                #alter sequence estudiante_idestudiante_seq restart start with 1;
                
                cursor.execute (SQL)
                cn.conexion.commit()
                
                print("\n****** Estudiante Ingresado Correctamente *****\n")
                
                # Intente un Last_Value e intente un :new o sql un last_insert_id()
                
              
                #Obtener el Ultimo ID Ingresado
                for estudiante_idestudiante in cursor.execute("SELECT idestudiante FROM Estudiante WHERE idestudiante=(SELECT max(idestudiante) FROM Estudiante)"):
                 estudiante_idestudiante = str(estudiante_idestudiante)
                 estudiante_idestudiante= estudiante_idestudiante[1:-2]
                 estudiante_idestudiante = int(estudiante_idestudiante)               
               
                cn2= Conexion()
                cursor2 = cn2.conexion.cursor()
                 
                SQL2 = "insert into Matricula ( rut, nombres, apellidop, apellidom, direccion, comuna, ciudad, telefono, fechainscripcion, "
                SQL2 = SQL2+ " semestre, cuota, arancel, idcarrera, sede, idestudiante, estadopago)"
                SQL2 = SQL2 + f" values ('{rut}', '{nombres}', '{apellidoP}', '{apellidoM}', '{direccion}', '{comuna}', '{ciudad}', '{telefono}', to_date(sysdate, 'dd/mm/yyyy'), "
                SQL2 = SQL2 + f" '{semestre}', '{cuota}', '{arancel}', '{Matricula.idCarrera}', '{sede}', '{estudiante_idestudiante}', '{estadopago}')"
                cursor2.execute (SQL2)
                cn2.conexion.commit()
                print("\n****** Alumno Matriculado Correctamente *******\n")
                
        except Exception as ex:
                print(ex)

            