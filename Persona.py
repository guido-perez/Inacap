

from Conexion import Conexion
import hashlib


class Persona:
    
    def Validacion(self, useraux):

        # Query para comparar el tipo de usuario si es 1) Estudiante  2) Docente  3) Jefe de Carrera
        # Para luego invocar a la clase correspondiente.
        nombre = input("Ingrese rut o correo: ")
        
        if useraux == 'Estudiante':
                
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        SQL = f"select contraseña from estudiante where rut = '{nombre}' or correo = '{nombre}' "
                        for row in cursor.execute(SQL): 
                         pass

                        contador = 0 # Contador en 0 para que el ciclo de validacion
                        while contador < 3: # rompemos el ciclo al momento que el contador sea mayor que 3
                                clave = input("Ingrese una contraseña: ")
                                hash=hashlib.md5(clave.encode('utf-8')).hexdigest() # Encriptamos contrasela en md5
           
                                if row[0] ==  hash: #Comparamos el md5 incresado por el usuario vs el que esta en la bd
                                        print("\n****** Alumno Validado Correctamente *****\n")        
                                else:
                                        contador = contador + 1 
                                        print("\nContraseña incorrecta, intente nuevamente \n")
                                        
                                if contador > 4: # En caso que el contador sea mayor a 0 bloqueamos la contrase, cambiandola por una nuestra y comparamos la bd para rechazar los usuario que tengan la pass a60af2639144aadac7c19042680d3779 
                                        print("\n****** Contraseña Bloqueda *****\n")  # con esto podemos filtrar y saber que usarios estan bloqueados
                                        bloqueada="ContraseñaBloqueada$$$" #a60af2639144aadac7c19042680d3779
                                        bloqueada=hashlib.md5(bloqueada.encode('utf-8')).hexdigest()

                                        #query para modificar la clave encriptada nuestra al sistema
                                        cn= Conexion()
                                        cursor = cn.conexion.cursor()
                                        SQL = f"update estudiante set contraseña='{bloqueada}' where rut = '{nombre}' or correo = '{nombre}' "
                                        cursor.execute(SQL)
                                        cn.conexion.commit()
                                        break        
               
                except Exception as ex:
                        print(ex)

        if useraux == 'Docente':
                
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        SQL = f"select contraseña from docente where rut = '{nombre}' or correo = '{nombre}' "
                        for row in cursor.execute(SQL): 
                         pass

                        contador = 0 # Contador en 0 para que el ciclo de validacion
                        while contador < 3: # rompemos el ciclo al momento que el contador sea mayor que 3
                                clave = input("Ingrese una contraseña: ")
                                hash=hashlib.md5(clave.encode('utf-8')).hexdigest() # Encriptamos contrasela en md5
           
                                if row[0] ==  hash: #Comparamos el md5 incresado por el usuario vs el que esta en la bd
                                        print("\n****** Docente Validado Correctamente *****\n")        
                                else:
                                        contador = contador + 1 
                                        print("\nContraseña incorrecta, intente nuevamente \n")
                                        
                                if contador > 4: # En caso que el contador sea mayor a 0 bloqueamos la contrase, cambiandola por una nuestra y comparamos la bd para rechazar los usuario que tengan la pass a60af2639144aadac7c19042680d3779 
                                        print("\n****** Contraseña Bloqueda *****\n")  # con esto podemos filtrar y saber que usarios estan bloqueados
                                        bloqueada="ContraseñaBloqueada$$$" #a60af2639144aadac7c19042680d3779
                                        bloqueada=hashlib.md5(bloqueada.encode('utf-8')).hexdigest()

                                        #query para modificar la clave encriptada nuestra al sistema
                                        cn= Conexion()
                                        cursor = cn.conexion.cursor()
                                        SQL = f"update docente set contraseña='{bloqueada}' where rut = '{nombre}' or correo = '{nombre}' "
                                        cursor.execute(SQL)
                                        cn.conexion.commit()
                                        break        
               
                except Exception as ex:
                        print(ex)
                        
        if useraux == 'Jefe Carrera':
                
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        SQL = f"select contraseña from jefecarrera where rut = '{nombre}' or correo = '{nombre}' "
                        for row in cursor.execute(SQL): 
                         pass

                        contador = 0 # Contador en 0 para que el ciclo de validacion
                        while contador < 3: # rompemos el ciclo al momento que el contador sea mayor que 3
                                clave = input("Ingrese una contraseña: ")
                                hash=hashlib.md5(clave.encode('utf-8')).hexdigest() # Encriptamos contrasela en md5
           
                                if row[0] ==  hash: #Comparamos el md5 incresado por el usuario vs el que esta en la bd
                                        print("\n****** Jefe Carrera Validado Correctamente *****\n")        
                                else:
                                        contador = contador + 1 
                                        print("\nContraseña incorrecta, intente nuevamente \n")
                                        
                                if contador > 4: # En caso que el contador sea mayor a 0 bloqueamos la contrase, cambiandola por una nuestra y comparamos la bd para rechazar los usuario que tengan la pass a60af2639144aadac7c19042680d3779 
                                        print("\n****** Contraseña Bloqueda *****\n")  # con esto podemos filtrar y saber que usarios estan bloqueados
                                        bloqueada="ContraseñaBloqueada$$$" #a60af2639144aadac7c19042680d3779
                                        bloqueada=hashlib.md5(bloqueada.encode('utf-8')).hexdigest()

                                        #query para modificar la clave encriptada nuestra al sistema
                                        cn= Conexion()
                                        cursor = cn.conexion.cursor()
                                        SQL = f"update jefecarrera set contraseña='{bloqueada}' where rut = '{nombre}' or correo = '{nombre}' "
                                        cursor.execute(SQL)
                                        cn.conexion.commit()
                                        break        
               
                except Exception as ex:
                        print(ex)
                        
        if useraux == 'Administrador':
                
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        SQL = f"select contraseña from administrador where rut = '{nombre}' or correo = '{nombre}' "
                        for row in cursor.execute(SQL): 
                         pass

                        contador = 0 # Contador en 0 para que el ciclo de validacion
                        while contador < 3: # rompemos el ciclo al momento que el contador sea mayor que 3
                                clave = input("Ingrese una contraseña: ")
                                hash=hashlib.md5(clave.encode('utf-8')).hexdigest() # Encriptamos contrasela en md5
           
                                if row[0] ==  hash: #Comparamos el md5 incresado por el usuario vs el que esta en la bd
                                        print("\n****** Administrador Validado Correctamente *****\n")        
                                else:
                                        contador = contador + 1 
                                        print("\nContraseña incorrecta, intente nuevamente \n")
                                        
                                if contador > 4: # En caso que el contador sea mayor a 0 bloqueamos la contrase, cambiandola por una nuestra y comparamos la bd para rechazar los usuario que tengan la pass a60af2639144aadac7c19042680d3779 
                                        print("\n****** Contraseña Bloqueda *****\n")  # con esto podemos filtrar y saber que usarios estan bloqueados
                                        bloqueada="ContraseñaBloqueada$$$" #a60af2639144aadac7c19042680d3779
                                        bloqueada=hashlib.md5(bloqueada.encode('utf-8')).hexdigest()

                                        #query para modificar la clave encriptada nuestra al sistema
                                        cn= Conexion()
                                        cursor = cn.conexion.cursor()
                                        SQL = f"update Administrador set contraseña='{bloqueada}' where rut = '{nombre}' or correo = '{nombre}' "
                                        cursor.execute(SQL)
                                        cn.conexion.commit()
                                        break        
               
                except Exception as ex:
                        print(ex)
        
    def ingresoUsuario(self):
            
        tipousuario= input("Ingrese tipo de usuario 'Docente o Jefe Carrera': ")    
        nombres = input(f"Ingrese Nombres del {tipousuario}: ")
        apellidoP = input(f"Ingrese Apellido Paterno del {tipousuario}: ")
        apellidoM = input(f"Ingrese Apellido Materno del {tipousuario}: ")
        rut = input(f"Ingrese Rut del {tipousuario} (Sin puntos): ")
        #Creacion de contraseña y validacion de contraseña
        clave = input(f"Ingrese una contraseña para el {tipousuario} : ")
        hash=hashlib.md5(clave.encode('utf-8')).hexdigest() #Contraseña encryptada con md5
        
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
 
        idarea = int(input(f"Ingrese area para el {tipousuario}: "))
        
        
        #Obtenemos por medio de una query la id del area
        try: 
                cn0= Conexion()
                cursor = cn0.conexion.cursor()
                        
                SQL0 = f"select nombre from area where id_area = '{idarea}'"
                for row in cursor.execute(SQL0): 
                 pass
                nombre_area = row[0]
                
        except Exception as ex:
                        print(ex) 

        #Obtenemos por medio de una query la id del jefe de carrera
        try: 
                cn0= Conexion()
                cursor = cn0.conexion.cursor()

                    
                SQL = f"select jc.id_jefecarrera from jefecarrera jc "
                SQL = SQL + f" inner join area a on jc.id_jefecarrera = a.id_area "
                SQL = SQL + f" where a.nombre = '{nombre_area}' "
                for row in cursor.execute(SQL): 
                 pass
                idjefecarrera = row[0]

        except Exception as ex:
                        print(ex)
        

      
        if tipousuario=="Docente":
                
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        
                        SQL = f"insert into docente (tipousuario, nombres, apellidop, apellidom, rut, direccion, comuna, ciudad, telefono, correo, contraseña, id_jefecarrera, id_area) "
                        SQL = SQL + f" values ('{tipousuario}', '{nombres}', '{apellidoP}', '{apellidoM}', '{rut}', '{direccion}', '{comuna}', '{ciudad}', '{telefono}', "
                        SQL = SQL + f" '{correo}','{hash}', '{idjefecarrera}', '{idarea}') "
                        
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
                        SQL = SQL + f" '{correo}','{hash}', '{idarea}') "
                        
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