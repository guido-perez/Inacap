class Docente:
    __tipoUsuario=''
    __nombres=''
    __apellidoP=''
    __apellidoM=''
    __rut=''
    __direccion=''
    __comuna=''
    __ciudad=''
    __telefono=''
    __correo=''
    __usuario=''
    __contraseña=''
    __jefeCarrera_idJc=''
    __area=''

    def __init__(self, tipoUsuario, nombres, apellidoP, apellidoM, rut, direccion, comuna, ciudad, telefono, correo, usuario, contraseña, jefeCarrera_idJc, area):
        self.__tipoUsuario=tipoUsuario
        self.__nombres=nombres
        self.__apellidoP=apellidoP
        self.__apellidoM=apellidoM
        self.__rut=rut
        self.__direccion=direccion
        self.__comuna=comuna
        self.__ciudad=ciudad
        self.__telefono=telefono
        self.__correo=correo
        self.__usuario=usuario
        self.__contraseña=contraseña
        self.__jefeCarrera_idJc=jefeCarrera_idJc
        self.__area=area=area
        
