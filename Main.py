import sys

from Matricula import Matricula
from Persona import Persona



class Menu:
    useraux=''

#Creacion de Menu con las opciones basicas de seleccion
    def MenuPrincipal():
        
        
        print("==============================================================")
        print("-------------- Bienvenidos al Sistema Inacap  ---------------")
        print("====================== MENÚ PRINCIPAL ======================   ")
        print("1.- Estudiantes                                               ") # Invoca a la clase Estudiantes
        print("2.- Docentes                                                  ") # Invoca a la Clase Docentes
        print("3.- Jefe de Carrera                                           ") # Invoca a la Clase JefedeCarrera
        print("4.- Administrador                                                      ") # Salimos del programa
        print("                                                              ") # Salimos del programa
        print("\n5.- Salir                                                   ") # Salimos del programa   
        print("\n=============================================================")
        print("\n         Todos los derechos e izquierdos reservados            ")
        print("\n=============================================================")


    op=0
    while not op == 5:
        
        MenuPrincipal()
        op=int(input("Seleccione una opcion: "))
        
        if op > 0 and op <= 5:
            #se cumplan ambas opciones
            if op == 1:
                print("\nIngresando seccion Estudiante\n")
                print("¿El Alumno Matriculado? (S/N)\n")
                sino = input("Ingrese una opcion: ")
                if sino == "S" or "s":
                    print("\nAccediendo a Portal Estudiante\n")
                    
                    print("Menu Estudiante en construccion vuelva mas tarde....")    
                    useraux = 'Estudiante'
                    Usr = Persona()
                    Usr.Validacion(useraux)
                    break

                
                # Invocamos a clase personas para val1idar usuario y contraseña
                # Invocamos Clase Estudiantes

                if sino == "N" or "n":

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
                Usr = Persona()
                Usr.Validacion(useraux)
                break

                # Invocamos a clase personas para validar usuario y contraseña
                # Incocamos Clase Docentes
                
            if op == 3:
                print("\nAccediendo seccion Jefe de Carrera\n")
                useraux = 'Jefe Carrera'
                Usr = Persona()
                Usr.Validacion(useraux)
                break

                # Invocamos a clase personas para validar usuario y contraseña
                # Incocamos Clase Jefe de Carrera


            if op == 4:
                print("\nAccediento al Formulario Administrador\n")
                useraux = 'Administrador'
                Usr = Persona()
                Usr.Validacion(useraux)
                User.ingresoUsuario()

            if op == 5:
                sys.exit("Saliendo del sistema")
            
        else:
            print("\n--- Opcion seleccionada no valida ---")
            print("--- Vuelva a seleccionar una de las alternativas del Menu --- \n")
            
