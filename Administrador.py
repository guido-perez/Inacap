
from Conexion import Conexion
import hashlib


class Administrador:
    
    def ingresoUsuario(self):
        
        tipousuario= input("Ingrese tipo de usuario 'Docente o Jefe Carrera': ") 
        while tipousuario=='': 
                tipousuario= input("Ingrese tipo de usuario 'Docente o Jefe Carrera': ")  
        
        nombres = input(f"Ingrese Nombres del {tipousuario}: ") 
        while nombres=='':  
                nombres = input(f"Ingrese Nombres del {tipousuario}: ")
        
        apellidoP = input(f"Ingrese Apellido Paterno del {tipousuario}: ")        
        while apellidoP=='':         
                apellidoP = input(f"Ingrese Apellido Paterno del {tipousuario}: ")
        
        apellidoM = input(f"Ingrese Apellido Materno del {tipousuario}: ")                 
        while apellidoM=='':                
                apellidoM = input(f"Ingrese Apellido Materno del {tipousuario}: ")
        
        rut = input(f"Ingrese Rut del {tipousuario} (Sin puntos): ")
        while rut=='':  
                rut = input(f"Ingrese Rut del {tipousuario} (Sin puntos): ")
        
        clave = input(f"Ingrese una contraseña para el {tipousuario} : ")        
        while clave=='':         
                #Creacion de contraseña y validacion de contraseña
                clave = input(f"Ingrese una contraseña para el {tipousuario} : ")
                hash=hashlib.md5(clave.encode('utf-8')).hexdigest() #Contraseña encryptada con md5
        
        direccion = input(f"Ingrese Direccion del {tipousuario}: ")
        while direccion=='':         
                direccion = input(f"Ingrese Direccion del {tipousuario}: ")
        
        comuna = input(f"Ingrese Comuna del {tipousuario}: ")
        while comuna=='':          
                comuna = input(f"Ingrese Comuna del {tipousuario}: ")
        
        ciudad = input(f"Ingrese Ciudad del {tipousuario}: ")        
        while ciudad=='':         
                ciudad = input(f"Ingrese Ciudad del {tipousuario}: ")
        
        telefono = int(input(f"Ingrese Telefono del {tipousuario}: "))
        while telefono=='':         
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


    def CambiarContraseña(self, useraux, Rut):
            
        # Query para comparar el tipo de usuario si es 1) Estudiante  2) Docente  3) Jefe de Carrera
        # Para luego invocar a la clase correspondiente.
        print("\n*** IMPORNTE!! Si es que tiene mas de una matricula, Su usuario puede ser el correo asignado a su matricula ***\n" )
        correo = input("Ingrese correo: ")
        useraux = useraux.replace(" ", "")
     
        try:   # POR VALIDAR MAS DE UN RUT
                cn= Conexion()
                cursor = cn.conexion.cursor()
                if useraux == 'Estudiante':
                        SQL = f"select e.contraseña, e.id_estudiante, e.rut, c.carrera from estudiante e  "
                        SQL = SQL + f"inner join matricula m on e.id_estudiante = m.id_estudiante "
                        SQL = SQL + f"inner join carrera c on c.id_carrera = m.id_carrera  "
                        SQL = SQL + f" where e.rut = '{Rut}' or correo='{correo}'"
                        contador=0
                        print("ID |        RUT           |       CARRERA                    ")
                        for row in cursor.execute(SQL): 
                                print(row[1]," | ",row[2]," | ",row[3])
                                contador=contador+1
                        
                        if contador > 1:

                                id = input("Seleccione la id de estudiante correspondiente: ")
                                
                                print("*** IMPORNTE!! Como tiene mas de una matricula, Su usuario debe ser el correo asignado a su matricula ***" )
                                SQL = f"select contraseña from estudiante where id_estudiante = '{id}' or or correo='{correo}'"
                                for row in cursor.execute(SQL):
                                         pass           
                else:
                
                        SQL = f"select contraseña from {useraux} where rut = '{Rut}' or correo='{correo}'"
 
                        for row in cursor.execute(SQL): 
                         pass
  
                bloqueada="a60af2639144aadac7c19042680d3779"   #Md5 de Password Ingresada por el Administrador para Bloquar Cuentas"  ContraseñaBloqueada$$$ "
                        
                if row[0]==bloqueada:
                        print("\n*************************************************************************************")
                        print("*** Contraseña Bloqueada, Contactese con el administrador < contacto@inacap.cl > ****")
                        print("*************************************************************************************")
                        exit()      
          
                #Validamos que contraseña actual sea igual a la que esta en la base de datos ya encriptada
                clave_actual = input("Ingrese contraseña actual contraseña: ")
                hash_actual=hashlib.md5(clave_actual.encode('utf-8')).hexdigest() # Encriptamos contrasela en md5
                while row[0] !=  hash_actual:
                                print("\n******Contraseña Antigua no Coincide. Intente Nuevamente *****\n")
                                clave_actual = input("Ingrese contraseña actual contraseña: ")
                                hash_actual=hashlib.md5(clave_actual.encode('utf-8')).hexdigest() # Encriptamos contrasela en md5                

                clave_nueva = input("Ingrese nueva contraseña: ")
                clave = input("Repita nueva contraseña: ")
                  
                 #Validamos que contraseña nueva se repita 2 veces para asegurarnos que el usuario sepa que contraseña este utilizando       
                while clave_nueva != clave: 
                        print("Contraseñas no coinciden, Intente Nuevamente")
                        clave_nueva = input("Ingrese nueva contraseña: ")
                        clave = input("Repita nueva contraseña: ")

                            
                #Realizadas todas las validaciones procedemos a encriptar la nueva contraseña y enviamos a la BD un UPDATE
                hash=hashlib.md5(clave_nueva.encode('utf-8')).hexdigest() # Encriptamos contrasela en md5

                #query para modificar la clave encriptada nuestra al sistema
                cn= Conexion()
                cursor = cn.conexion.cursor()
                SQL = f"update {useraux} set contraseña='{hash}' where rut = '{Rut}' or correo='{correo}' "
                cursor.execute(SQL)
                cn.conexion.commit()
                print("\n****** Cambio de Contraseña se realizo Correctamente *****\n")

        except Exception as ex:
                print(ex)
                
    def eliminarUsuario(self):
        
        print("\n✧ Portal Eliminar Usuarios \n")
        print("1.- Estudiante                                               ") # 
        print("2.- Docente                                                ") # Invoca a la funcion Eliminar Usuarios
        print("3.- Jefe de Carrera                                    ")
        
        usuario = input("\n Ingrese Usuario que desea Eliminar: ")
        
        if usuario == 1:
            usuario = 'Estudiante'
        elif usuario == 2:
            usuario = 'Docente'
        elif usuario == 3:
            usuario = 'jefecarrera'
        else:
            print("Debe Elegir una ID usuario de la Lista")
                              
        print("\n \n")
        print(f"\n        Listado {usuario}             ")
        print("")
        print("ID |      Rut           |       Nombre                    ")
        try: 
                cn= Conexion()
                cursor = cn.conexion.cursor()
                        
                SQL = f"select id_{usuario}, rut, e.nombres || ' '|| e.apellidop || ' '|| e.apellidom Nombre_Usuario from {usuario} "
                for row in cursor.execute(SQL): 
                 print(row[0]," | ",row[1]," | ",row[2]+" "+row[3] )

        except Exception as ex:
                        print(ex) 
        
        rut = input(f"\n Ingrese Rut {usuario} a Eliminar: ")
        
        try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                    

                SQL0 = f"delete from {usuario} WHERE rut='{rut}' "

                cursor.execute(SQL0)
                cn1.conexion.commit()
                
                print(f"\n****** Usuario Eliminado Correctamente *****\n")
        except Exception as ex:

                        print(ex)
                        
    def DesbloquearContraseña(self):
        
        print("\n✧ Portal Desbloquear Contraseña de Usuarios \n")
        print("1.- Estudiante                                               ") # 
        print("2.- Docente                                                ") # Invoca a la funcion Eliminar Usuarios
        print("3.- Jefe de Carrera                                    ")
        
        usuario = input("\n Ingrese ID Usuario que desea desbloquear: ")
        
        if usuario == 1:
            usuario = 'Estudiante'
        elif usuario == 2:
            usuario = 'Docente'
        elif usuario == 3:
            usuario = 'jefecarrera'
        else:
            print("Debe Elegir una ID usuario de la Lista")
        
        Rut = input("\nIngrese Usuario para validar usuario:")     
        clave_nueva = input("Ingrese nueva contraseña: ")
        clave = input("Repita nueva contraseña: ")
                  
                 #Validamos que contraseña nueva se repita 2 veces para asegurarnos que el usuario sepa que contraseña este utilizando       
        while clave_nueva != clave: 
                print("Contraseñas no coinciden, Intente Nuevamente")
                clave_nueva = input("Ingrese nueva contraseña: ")
                clave = input("Repita nueva contraseña: ")

                 #Realizadas todas las validaciones procedemos a encriptar la nueva contraseña y enviamos a la BD un UPDATE
                hash=hashlib.md5(clave_nueva.encode('utf-8')).hexdigest() # Encriptamos contrasela en md5  
                  
        try: 
                cn= Conexion()
                cursor = cn.conexion.cursor()
                        
                SQL = f"update {usuario} set  contraseña={hash} where contraseña='a60af2639144aadac7c19042680d3779'  "
                for row in cursor.execute(SQL): 
                 print(row[0]," | ",row[1]," | ",row[2]+" "+row[3] )

        except Exception as ex:
                        print(ex) 