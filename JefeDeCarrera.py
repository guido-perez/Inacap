class JefeDeCarrera:
    __idJc=''
    __tipoUsuario=''
    __nombres=''
    __apellidoP=''
    __apellidoM=''
    __comuna=''
    __ciudad=''
    __rut=''
    __direccion=''
    __telefono=''
    __correo=''
    __usuario=''
    __contraseña=''
    __area=''

    def __init__(self, idJc, tipoUsuario, nombres, apellidoP, apellidoM, comuna, ciudad, rut, direccion, telefono, correo, usuario, contraseña, area):
        self.__idJc=idJc
        self.__tipoUsuario=tipoUsuario
        self.__nombres=nombres
        self.__apellidoP=apellidoP
        self.__apellidoM=apellidoM
        self.__comuna=comuna
        self.__ciudad=ciudad
        self.__rut=rut
        self.__direccion=direccion
        self.__telefono=telefono
        self.__correo=correo
        self.__usuario=usuario
        self.__contraseña=contraseña
        self.__area=area   