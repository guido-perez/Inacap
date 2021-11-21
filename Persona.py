import time

class Persona:
    __nombre=''
    __apellidoP=''
    __apellidoM=''
    __rut=''
    __direccion=''
    __telefono=''
    __correo=''
    __usuario=''
    __contraseña=''
    __tipoUsuario=''
    __idUsuario=''
    

    #primer parametro siempre es la instancia
    def __init__(self, nombre, apellidoP, apellidoM, rut, direccion, telefono,correo, usuario,contraseña,tipoUsuario,idUsuario ):
        self.__nombre=nombre
        self.__apellidoP=apellidoP
        self.__apellidoM=apellidoM
        self.__rut=rut
        self.__direccion=direccion
        self.__telefono=telefono
        self.__correo=correo
        self.__usuario=usuario
        self.__contraseña=contraseña
        self.__tipoUsuario=tipoUsuario
        self.__idUsuario=idUsuario
    
    
    def Validacion():
        
        
        # Query para comparar el tipo de usuario si es 1) Estudiante  2) Docente  3) Jefe de Carrera
        # Para luego invocar a la clase correspondiente.
        
        
        
        palabra = input("Ingrese una contraseña: ")
        password = "123"

        time.sleep(1)


        while password != palabra:
            for i in range(2): 
                print("*** Validando contraseña espere porfavor ... ", end="\n")
            time.sleep(1)

            password = input("Ingrese nuevamente la contraseña: ")
            print("*** Validando contraseña espere porfavor ... ")
            print("* Contraseña Validada Correctamente * ")
