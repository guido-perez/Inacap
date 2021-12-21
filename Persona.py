

from Conexion import Conexion
import hashlib


class Persona:
       
        
    def Validacion(self, useraux, Rut):

        # Query para comparar el tipo de usuario si es 1) Estudiante  2) Docente  3) Jefe de Carrera
        # Para luego invocar a la clase correspondiente.
        run=''
        contraseña = ''
        if useraux == 'Estudiante':
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        SQL = f"select contraseña, rut from estudiante where rut = '{Rut}' or correo = '{Rut}'"
                        
                        for row in cursor.execute(SQL):
                         pass
                         run = row[1]   
                         contraseña=row[0]

                        if run !=Rut:
                                print("Usuario no encontrado") 
                                count = 0
                                while count < 3:
                                        Rut = input("\nIngrese Usuario para validar usuario:") 
                                        cn= Conexion()
                                        cursor = cn.conexion.cursor()
                                        SQL = f"select contraseña, rut from estudiante where rut = '{Rut}' or correo = '{Rut}' "
                                        for row in cursor.execute(SQL):
                                                count = count +1  
                                                run = row[1]   
                                                contraseña=row[0]
                                        if run == Rut:
                                                break
                                        else:
                                             print("Usuario no encontrado")
 
                   
                        contador = 0 # Contador en 0 para que el ciclo de validacion
                        while contador < 3: # rompemos el ciclo al momento que el contador sea mayor que 3
                                clave = input("Ingrese una contraseña: ")
                                hash=hashlib.md5(clave.encode('utf-8')).hexdigest() # Encriptamos contrasela en md5
                                
                                if contraseña ==  hash: #Comparamos el md5 incresado por el usuario vs el que esta en la bd
                                        print("\n****** Alumno Validado Correctamente *****\n")
                                        break
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
                                        SQL = f"update estudiante set contraseña='{bloqueada}' where rut = '{Rut}' or correo = '{Rut}' "
                                        cursor.execute(SQL)
                                        cn.conexion.commit()
                                                
                                        
                except Exception as ex:
                        print(ex)

        elif useraux == 'Docente':
                
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        SQL = f"select contraseña, rut from docente where rut = '{Rut}' or correo = '{Rut}' "
                        for row in cursor.execute(SQL): 
                         pass
                         run = row[1]   
                         contraseña=row[0]
                         
                        if run !=Rut:
                                print("Usuario no encontrado") 
                                count = 0
                                while count < 3:
                                        Rut = input("\nIngrese Rut para validar usuario:") 
                                        cn= Conexion()
                                        cursor = cn.conexion.cursor()
                                        SQL = f"select contraseña, rut from docente where rut = '{Rut}' "
                                        for row in cursor.execute(SQL):
                                                count = count +1  
                                                run = row[1]   
                                                contraseña=row[0]
                                        if run == Rut:
                                                break
                                        else:
                                             print("Usuario no encontrado") 
                         
                         
                        contador = 0 # Contador en 0 para que el ciclo de validacion
                        while contador < 3: # rompemos el ciclo al momento que el contador sea mayor que 3
                                clave = input("Ingrese una contraseña: ")
                                hash=hashlib.md5(clave.encode('utf-8')).hexdigest() # Encriptamos contrasela en md5
           
                                if contraseña ==  hash: #Comparamos el md5 incresado por el usuario vs el que esta en la bd
                                        print("\n****** Docente Validado Correctamente *****\n")        
                                        break                                
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
                                        SQL = f"update docente set contraseña='{bloqueada}' where rut = '{Rut}' or correo = '{Rut}' "
                                        cursor.execute(SQL)
                                        cn.conexion.commit()
                                        break        
               
                except Exception as ex:
                        print(ex)
                        
        elif useraux == 'Jefe Carrera':
                
                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        SQL = f"select contraseña, rut from jefecarrera where rut = '{Rut}' or correo = '{Rut}' "
                        for row in cursor.execute(SQL): 
                         pass
                         run = row[1]   
                         contraseña=row[0]
                        
                        if run !=Rut:
                                print("Usuario no encontrado") 
                                count = 0
                                while count < 3:
                                        Rut = input("\nIngrese Rut para validar usuario:") 
                                        cn= Conexion()
                                        cursor = cn.conexion.cursor()
                                        SQL = f"select contraseña, rut from jefecarrera where rut = '{Rut}' "
                                        for row in cursor.execute(SQL):
                                                count = count +1  
                                                run = row[1]   
                                                contraseña=row[0]
                                        if run == Rut:
                                                break
                                        else:
                                             print("Usuario no encontrado")  

                        contador = 0 # Contador en 0 para que el ciclo de validacion
                        while contador < 3: # rompemos el ciclo al momento que el contador sea mayor que 3
                                clave = input("Ingrese una contraseña: ")
                                hash=hashlib.md5(clave.encode('utf-8')).hexdigest() # Encriptamos contrasela en md5
           
                                if contraseña ==  hash: #Comparamos el md5 incresado por el usuario vs el que esta en la bd
                                        print("\n****** Jefe Carrera Validado Correctamente *****\n")        
                                        break
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
                                        SQL = f"update jefecarrera set contraseña='{bloqueada}' where rut = '{Rut}' or correo = '{Rut}' "
                                        cursor.execute(SQL)
                                        cn.conexion.commit()
                                        break        
               
                except Exception as ex:
                        print(ex)
                        
        elif useraux == 'Administrador':

                try: 
                        cn= Conexion()
                        cursor = cn.conexion.cursor()
                        SQL = f"select contraseña, rut from administrador where rut = '{Rut}' or correo = '{Rut}'"
                        
                        for row in cursor.execute(SQL):
                         pass
                         run = row[1]   
                         contraseña=row[0]

                        if run !=Rut:
                                print("Usuario no encontrado") 
                                count = 0
                                while count < 3:
                                        Rut = input("\nIngrese Usuario para validar usuario:") 
                                        cn= Conexion()
                                        cursor = cn.conexion.cursor()
                                        SQL = f"select contraseña, rut from administrador where rut = '{Rut}' or correo = '{Rut}' "
                                        for row in cursor.execute(SQL):
                                                count = count +1  
                                                run = row[1]   
                                                contraseña=row[0]
                                        if run == Rut:
                                                break
                                        else:
                                             print("Usuario no encontrado")
 
                   
                        contador = 0 # Contador en 0 para que el ciclo de validacion
                        while contador < 3: # rompemos el ciclo al momento que el contador sea mayor que 3
                                clave = input("Ingrese una contraseña: ")
                                hash=hashlib.md5(clave.encode('utf-8')).hexdigest() # Encriptamos contrasela en md5
                                
                                if contraseña ==  hash: #Comparamos el md5 incresado por el usuario vs el que esta en la bd
                                        print("\n****** Administrador Validado Correctamente *****\n")
                                        break
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
                                        SQL = f"update administrador set contraseña='{bloqueada}' where rut = '{Rut}' or correo = '{Rut}' "
                                        cursor.execute(SQL)
                                        cn.conexion.commit()
                                                
                                        
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
                        
    

        