
from Matricula import Matricula
from Persona import Persona


class Menu:
    useraux='' 
    #Creacion de Menu con las opciones basicas de seleccion
def Menu():
        
        print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
        print("✧✧✧✧✧✧✧✧✧ Bienvenidos al Sistema Inacap ✧✧✧✧✧✧✧✧")
        print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦ MENÚ PRINCIPAL ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦\n")
        print("1.- Estudiantes                                                       ") # Invoca a la clase Estudiantes se valida por usuario
        print("2.- Docentes                                                          ") # Invoca a la Clase Docentes se valida por usuario
        print("3.- Jefe de Carrera                                                   ") # Invoca a la Clase JefedeCarrera se valida por usuario
        print("4.- Administrador                                                     ") # Salimos del programa
        print("                                                                      ") # Salimos del programa
        print("5.- Salir                                                           ") # Salimos del programa   
        print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
        print("  Todos los derechos e izquierdos reservados®   ")
        print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
    
    
op=0
while not op == 5:
        
        Menu()
        op=int(input("✧ Seleccione una opcion: "))
        
        if op > 0 and op <= 5:
            #se cumplan ambas opciones
            if op == 1:
                 
                def MenuEstudiante():
 
                    print("\n✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("✧✧✧✧✧✧✧✧✧ Bienvenidos al Sistema Inacap ✧✧✧✧✧✧✧✧")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦ MENÚ ESTUDIANTE ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦\n   ") # Invoca a la Clase Matricula
                    print("1.- Matricularse                                                      ") # Invoca a la Funcion IngresarMatricula  #OK
                    print("2.- Ver Modulos                                                       ") # Invoca a la Funcion ListaModulos   #
                    print("3.- Ver Notas                                                         ") # Invoca a la Funcion VerNota   #
                    print("4.- Cambiar contraseña                                                ") 
                    print("5.- Portal de Pago                                                    ") 
                    print("                                                                      ")
                    print("\n5.- Salir                                                           ") # Salimos del programa   
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("  Todos los derechos e izquierdos reservados®                         ")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                
                op=0
                while not op == 4:
                        
                        MenuEstudiante()
                        op=int(input("✧ Seleccione una opcion: "))
                        
                        if op > 0 and op <= 4:
                            #se cumplan ambas opciones
                            if op == 1:
                                print("\n✦ Accediendo al Portal Matriculas\n")
                                Mat = Matricula()
                                Mat.MostrarCarrera()
                                Mat.CalcularCuota()
                                Mat.ingresarMatricula()
                                Mat.Transaccion()
                                break
                                # Invocamos a Clase Matricula para ingresar un Alumno
                                # Del mismo formulario, llenamos la tabla Estudiante 
                                
                            if op == 2:
                                print("\n✦ Accediendo a Portal Notas del Modulos\n")
                                useraux = 'Estudiante'
                                User = Persona()
                                User.Validacion(useraux)
                                # Invocamos a Clase Personas para validar usuario y contraseña  

                                # Invocamos Clase Estudiantes para ver ver modulos
                                print("Menu en construccion vuelva mas tarde.... ") 
                            if op == 3:
                                print("\n✦ Accediendo a Portal Notas del Notas\n")
                                useraux = 'Estudiante'
                                User = Persona()
                                User.Validacion(useraux)

                                # Invocamos Clase Estudiantes para ver ver notas
                                print("Menu en construccion vuelva mas tarde.... ") 
                            if op == 4:
                                #sys.exit("Saliendo del MunuEstudiante")
                                Menu()
                        else:
                            print("\n--- Opcion seleccionada no es valida ---")
                            print("--- Vuelva a seleccionar una de las alternativas del MunuEstudiante --- \n")   
                   
            #Fin Estudiante
            if op == 2:
                
                useraux = 'Docente'
                User = Persona()
                User.Validacion(useraux)  
                # Invocamos a clase personas para validar usuario y contraseña
                # Incocamos Clase Docente
                
                def MenuDocente():
  
                    print("\n✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("✧✧✧✧✧✧✧✧✧ Bienvenidos al Sistema Inacap ✧✧✧✧✧✧✧✧")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦ MENÚ DOCENTE ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦\n      ") # Invoca a la Clase Nota
                    print("1.- Agregar Nota a Estudinte                                          ") # Invoca a la Funcion Agregar Nota
                    print("2.- Modificar Nota a Estudinte                                        ") # Invoca a la Funcion Modificar Nota
                    print("3.- Eliminar Nota a Estudinte                                         ") # Invoca a la Funcion Eliminar Nota
                    print("4.- Cambiar contraseña                                                ") 
                    print("                                                                      ") 
                    print("6.-                                                                   ")
                    print("\n4.- Salir                                                           ") # Salimos del programa   
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("  Todos los derechos e izquierdos reservados®                         ")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                
                op=0
                while not op == 4:
                        
                        MenuDocente()
                        op=int(input("✧ Seleccione una opcion: "))
                        
                        if op > 0 and op <= 4:
                            #se cumplan ambas opciones
                            if op == 1:
                                print("\n✦ Accediendo al Portal Agregar Notas\n")
                                # Invocamos a Clase Notas para Agregar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                            if op == 2:
                                print("\n✦ Accediendo a Portal Modificar Notas\n")
                                # Invocamos a Clase Notas para Modificar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                                print("Menu en construccion vuelva mas tarde.... ") 
                            if op == 3:
                                print("\n✦ Accediendo a Portal Eliminar Notas\n")
                                # Invocamos a Clase Notas para Eliminar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                print("Menu en construccion vuelva mas tarde.... ") 
                            if op == 4:
                                sys.exit("Saliendo del MenuDocente")
                        else:
                            print("\n--- Opcion seleccionada no es valida ---")
                            print("--- Vuelva a seleccionar una de las alternativas del MenuDocente --- \n")   

            #Fin Docentes
            if op == 3:
                
                useraux = 'JefeCarrera'
                User = Persona()
                User.Validacion(useraux)  
                # Invocamos a clase personas para validar usuario y contraseña
                # Incocamos Clase Jefe de Carrera
                
                def MenuJefeCarrera():
                    
                    print("\n✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("✧✧✧✧✧✧✧✧✧ Bienvenidos al Sistema Inacap ✧✧✧✧✧✧✧✧            ")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦ MENÚ JEFE DE CARRERA ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦\n") # Invoca a la Clase Nota
                    print("1.- Asignar Modulo a Estudinte                                      ") # Invoca a la Funcion Agregar Nota
                    print("2.- Modificar Modulo a Estudinte                                      ") # Invoca a la Funcion Modificar Nota
                    print("3.- Eliminar Modulo a Estudinte                                       ") # Invoca a la Funcion Eliminar Nota
                    print("4.- Ver Modulos del Sistema                                           ") 
                    print("5.- Nuevo Modulo                                                      ")                     
                    print("6.- Modificar Modulo                                                  ") 
                    print("7.- Eliminar Modulo                                                   ")
                    print("8.- Agregar Modulo a Docente                                          ") 
                    print("9.- Modificar Modulo a Docente                                        ")                      
                    print("10.- Eliminar Modulo a Docente                                        ") 
                    print("11.- Ver Modulos del Sistema                                          ") 
                    print("12.- Cambiar contraseña                                               ") 
                    print("                                                                      ")                                                            
                    print("\n12.- Salir                                                           ") # Salimos del programa   
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("  Todos los derechos e izquierdos reservados®                         ")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                
                op=0
                while not op == 12:
                        
                        MenuJefeCarrera()
                        op=int(input("✧ Seleccione una opcion: "))
                        
                        if op > 0 and op <= 12:
                            #se cumplan ambas opciones
                            if op == 1:
                                print("\n✦ Accediendo al Portal Agregar Notas\n")
                                # Invocamos a Clase Notas para Agregar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                            if op == 2:
                                print("\n✦ Accediendo a Portal Modificar Notas\n")
                                # Invocamos a Clase Notas para Modificar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                                print("Menu en construccion vuelva mas tarde.... ") 
                            if op == 3:
                                print("\n✦ Accediendo a Portal Eliminar Notas\n")
                                # Invocamos a Clase Notas para Eliminar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                print("Menu en construccion vuelva mas tarde.... ")
                            if op == 4:
                                print("\n✦ Accediendo al Portal Agregar Notas\n")
                                # Invocamos a Clase Notas para Agregar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                            if op == 5:
                                print("\n✦ Accediendo a Portal Modificar Notas\n")
                                # Invocamos a Clase Notas para Modificar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                                print("Menu en construccion vuelva mas tarde.... ") 
                            if op == 6:
                                print("\n✦ Accediendo a Portal Eliminar Notas\n")
                                # Invocamos a Clase Notas para Eliminar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                print("Menu en construccion vuelva mas tarde.... ")
                            if op == 7:
                                print("\n✦ Accediendo al Portal Agregar Notas\n")
                                # Invocamos a Clase Notas para Agregar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                            if op == 8:
                                print("\n✦ Accediendo a Portal Modificar Notas\n")
                                # Invocamos a Clase Notas para Modificar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                
                                print("Menu en construccion vuelva mas tarde.... ") 
                            if op == 9:
                                print("\n✦ Accediendo a Portal Eliminar Notas\n")
                                # Invocamos a Clase Notas para Eliminar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                print("Menu en construccion vuelva mas tarde.... ")
                            if op == 10:
                                print("\n✦ Accediendo a Portal Eliminar Notas\n")
                                # Invocamos a Clase Notas para Eliminar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                print("Menu en construccion vuelva mas tarde.... ")
                            if op == 11:
                                print("\n✦ Accediendo a Portal Eliminar Notas\n")
                                # Invocamos a Clase Notas para Eliminar rut del Alumno
                                # validamos el modulo, seccion y agregamos nota 
                                print("Menu en construccion vuelva mas tarde.... ")                                 
                            if op == 12:
                                sys.exit("Saliendo del MenuDocente")
                        else:
                            print("\n--- Opcion seleccionada no es valida ---")
                            print("--- Vuelva a seleccionar una de las alternativas del MenuDocente --- \n")   

            #Fin JefeCarrera
            if op == 4:
                print("\nAccediento al Formulario Administrador\n")
                useraux = 'Administrador'
                User = Persona()
                User.Validacion(useraux)
                
                def MunuAdmin():
                    
                    print("\n✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("✧✧✧✧✧✧✧✧✧ Bienvenidos al Sistema Inacap ✧✧✧✧✧✧✧✧            ")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦ MENÚ ADMIN ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦\n") # 
                    print("1.- Ingresar Usuarios                                                ") # 
                    print("2.- Eliminar Usuarios                                                ") # Invoca a la funcion Eliminar Usuarios
                    print("3.- Cambiar Contraseña de Usuario                                    ")
                    print("4.- Ver Estudiantes Matriculados                                     ")
                    print("5.- Matricular                                                       ") # Invoca a la funcion Eliminar Usuarios                    
                    print("6.- Anular Matricula                                                 ") # Invoca a la funcion Anular Matricula Usuarios
                    print("7.- Modificar Matricula                                              ") # a la funcion Modificar Matricula Usuarios
                    print("8.- Ver Notas de Estudiante                                          ") # Invoca a la Funcion VerNota                    
                    print("9.- Agregar Nota a Estudinte                                          ") # Invoca a la Funcion Agregar Nota
                    print("10.- Modificar Nota a Estudinte                                        ") # Invoca a la Funcion Modificar Nota
                    print("11.- Eliminar Nota a Estudinte                                         ") # Invoca a la Funcion Eliminar Nota 
                    print("12.- Ver Modulos de Estudiante                                         ") # Invoca a la Funcion ListaModulos                   
                    print("13.- Inscribir Modulo a Estudinte                                      ") # Invoca a la Funcion Agregar Nota
                    print("14.- Modificar Modulo a Estudinte                                      ") # Invoca a la Funcion Modificar Nota
                    print("15.- Eliminar Modulo a Estudinte                                       ") # Invoca a la Funcion Eliminar Nota
                    print("16.- Ver Modulos del Sistema                                           ") 
                    print("17.- Nuevo Modulo                                                      ")                     
                    print("18.- Modificar Modulo                                                  ") 
                    print("19.- Eliminar Modulo                                                   ")
                    print("20.- Agregar Modulo a Docente                                          ") 
                    print("21.- Modificar Modulo a Docente                                        ")                      
                    print("22.- Eliminar Modulo a Docente                                        ") 
                    print("23.- Ver Modulos de Docente                                          ") 
                    print("                                                                    ")                                                            
                    print("\n24.- Salir                                                           ") # Salimos del programa   
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("  Todos los derechos e izquierdos reservados®                         ")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    
                op=0
                while not op == 24:
                                            
                    MunuAdmin()
                    op=int(input("✧ Seleccione una opcion: "))
                                            
                    if op > 0 and op <= 24:
                                #se cumplan ambas opciones
                                    if op == 1:
                                        print("\nIngresando Formulario de Ingreso de Usuarios\n")        
                                        User = Persona()
                                        User.ingresoUsuario()
                                        break
                                        # Invocamos a clase Personas
                                        # Invocamos la funcion para ingresar Docente o Jefe de Carrera

                                    if op == 2:
                                        print("\nIngresando Formulario de Eliminar de Usuarios\n")
                                        User = Persona()
                                        User.eliminarDocente()
                                        break

                                        # Invocamos a clase Personas
                                        # Incocamosla funcion para eliminar  Docente o Jefe de Carrera
                                                    
                                    if op == 3:
                                        pass

                                    if op == 4:
                                        pass
                                        
                                    if op == 5:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 6:
                                        print("\nIngresando Formulario de Anular Matricula\n")
                                        User = Matricula()
                                        User.AnularMatricula()
                                        break
                                        # Invocamos a clase personas para validar usuario y contraseña
                                        # Incocamos Clase Persona
                                        
                                    if op == 7:
                                        print("\nIngresando Formulario de Modificar Matricula\n")
                                        User = Matricula()
                                        User.ActualizarMatricula()
                                                                          
                                    if op == 8:
                                        print("Menu en construccion vuelva mas tarde.... ")
                                    if op == 9:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 10:
                                        print("Menu en construccion vuelva mas tarde.... ")    
                                    if op == 11:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 12:
                                        print("Menu en construccion vuelva mas tarde.... ")                                          
                                    if op == 13:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 14:
                                        print("Menu en construccion vuelva mas tarde.... ")    
                                    if op == 15:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 16:
                                        print("Menu en construccion vuelva mas tarde.... ")                                          
                                    if op == 17:
                                        print("Menu en construccion vuelva mas tarde.... ")    
                                    if op == 18:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 19:
                                        print("Menu en construccion vuelva mas tarde.... ")                                          
                                    if op == 20:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 21:
                                        print("Menu en construccion vuelva mas tarde.... ")    
                                    if op == 22:
                                        print("Menu en construccion vuelva mas tarde.... ")                                    
                                    if op == 23:
                                        print("Menu en construccion vuelva mas tarde.... ")                                                                                 
                                    if op == 24:
                                        sys.exit("Saliendo del MunuAdmin")
                                                
                    else:
                                print("\n--- Opcion seleccionada no valida ---")
                                print("--- Vuelva a seleccionar una de las alternativas del MenuAdmin --- \n")
                                                
                
            if op == 5:
                sys.exit("Saliendo del sistema")
            
        else:
            print("\n--- Opcion seleccionada no valida ---")
            print("--- Vuelva a seleccionar una de las alternativas del MenuAdmin --- \n")

            



                

