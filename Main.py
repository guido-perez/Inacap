import sys

import Estudiante
import Docente
import JefeDeCarrera

#Creacion de Menu con las opciones basicas de seleccion
def Menu():
    print("***************************************")
    print("---- Bienvenidos al Sistema Inacap  ---\n")
    print("1) Estudiantes") # Invoca a la clase Estudiantes
    print("2) Docentes") # Invoca a la Clase Docentes
    print("3) Jefe de Carrera") # Invoca a la Clase JefedeCarrera
    print("\n4) Salir") # Salimos del programa
    print("\n***************************************")
    
    
op=0
while not op == 4:
    
    Menu()
    #Convertimos la variable "op" a tipo Int
    op=int(input()) 
    
    if op > 0 and op <= 4:
        #se cumplan ambas opciones
        if op == 1:
            print("Ingresando seccion Estudiante")
            # Invocamos a clase personas para validar usuario y contraseña
            # Incocamos Clase Estudiantes

        if op == 2:
            print("Ingresando seccion Docentes")
            # Invocamos a clase personas para validar usuario y contraseña
            # Incocamos Clase Docentes
            
        if op == 3:
            print("Ingresando seccion Jefe de Carrera")
            # Invocamos a clase personas para validar usuario y contraseña
            # Incocamos Clase Jefe de Carrera

        if op == 4:
            sys.exit("Saliendo del sistema")


        
    else:
        print("Opcion seleccionada no valida")
        
