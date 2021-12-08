import sys

from Matricula import Matricula
from Persona import Persona


class Menu:
    useraux='' 
    #Creacion de Menu con las opciones basicas de seleccion
def Menu():
        
        
        print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
        print("✧✧✧✧✧✧✧✧✧✧✧✧ Bienvenidos al Sistema Inacap  ✧✧✧✧✧✧✧✧✧✧✧")
        print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦ MENÚ PRINCIPAL ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
        print("1.- Estudiantes                                               ") # Invoca a la clase Estudiantes
        print("2.- Docentes                                                  ") # Invoca a la Clase Docentes
        print("3.- Jefe de Carrera                                           ") # Invoca a la Clase JefedeCarrera
        print("4.- Administrador                                                      ") # Salimos del programa
        print("                                                              ") # Salimos del programa
        print("\n5.- Salir                                                   ") # Salimos del programa   
        print("\n✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
        print("\n        Todos los derechos e izquierdos reservados®            ")
        print("\n✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
    
    
op=0
while not op == 5:
        
        Menu()
        op=int(input("Seleccione una opcion: "))
        
        if op > 0 and op <= 5:
            #se cumplan ambas opciones
            if op == 1:
                print("\nIngresando seccion Estudiante\n")
                print("¿El Alumno Matriculado? (S/N)\n")
                sino = input("Ingrese una opcion: ")
                if sino == "S" or sino == "s":
                    print("\nAccediendo a Portal Estudiante\n")  
                    useraux = 'Estudiante'
                    User = Persona()
                    User.Validacion(useraux)
                    break
                    # Invocamos a clase personas para val1idar usuario y contraseña
                    # Invocamos Clase Estudiantes
                if sino == "N" or sino == "n":
                    
                    print("\nAccediendo al Portal Matricula\n")
                    Mat = Matricula()
                    Mat.MostrarCarrera()
                    Mat.CalcularCuota()
                    Mat.ingresarMatricula()
                    break
                    # Invocamos a Clase Matricula para ingresar un Alumno
                    # Del mismo formulario, llenamos la tabla Estudiante

            if op == 2:
                print("Ingresando seccion Docentes")
                useraux = 'Docente'
                User = Persona()
                User.Validacion(useraux)
                print("Menu Docente en construccion vuelva mas tarde.... ") 
                break

                # Invocamos a clase personas para validar usuario y contraseña
                # Incocamos Clase Docentes
                
            if op == 3:
                print("\nAccediendo seccion Jefe de Carrera\n")
                useraux = 'Jefe Carrera'
                User = Persona()
                User.Validacion(useraux)
                print("Menu Jefe Carrera en construccion vuelva mas tarde....") 
                #break

                # Invocamos a clase personas para validar usuario y contraseña
                # Incocamos Clase Jefe de Carrera

            if op == 4:
                print("\nAccediento al Formulario Administrador\n")
                useraux = 'Administrador'
                User = Persona()
                User.Validacion(useraux)
                
                def MunuAdmin():
                    
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("✧✧✧✧✧✧✧✧✧✧ Bienvenidos al Sistema Inacap  ✧✧✧✧✧✧✧✧✧✧✧")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦ MENÚ Admin ✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦        ")
                    print("1.- Ingresar Usuarios                                           ") # Invoca a la funcion Ingresar Usuarios
                    print("2.- Eliminar Usuarios                                                  ") # Invoca a la funcion Eliminar Usuarios
                    print("3.- Anular Matricula                                           ") # Invoca a la funcion Anular Matricula Usuarios
                    print("4.- Modificar Matricula                                                         ") # a la funcion Modificar Matricula Usuarios
                    print("                                                              ") # Salimos del programa
                    print("\n5.- Salir                                                   ") # Salimos del programa   
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")
                    print("        Todos los derechos e izquierdos reservados®            ")
                    print("✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦")                           


                op=0
                while not op == 5:
                                            
                    MunuAdmin()
                    op=int(input("Seleccione una opcion: "))
                                            
                    if op > 0 and op <= 5:
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
                                        print("\nIngresando Formulario de Anular Matricula\n")
                                        User = Matricula()
                                        User.AnularMatricula()
                                        break

                                        # Invocamos a clase personas para validar usuario y contraseña
                                        # Incocamos Clase Persona


                                    if op == 4:
                                        print("\nIngresando Formulario de Modificar Matricula\n")
                                        User = Matricula()
                                        User.ActualizarMatricula()

                                    if op == 5:
                                        sys.exit("Saliendo del MunuAdmin")
                                                
                    else:
                                print("\n--- Opcion seleccionada no valida ---")
                                print("--- Vuelva a seleccionar una de las alternativas del MenuAdmin --- \n")
                                                
                
            if op == 5:
                sys.exit("Saliendo del sistema")
            
        else:
            print("\n--- Opcion seleccionada no valida ---")
            print("--- Vuelva a seleccionar una de las alternativas del MenuAdmin --- \n")

            



                

