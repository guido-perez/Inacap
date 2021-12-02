from Conexion import Conexion

class Matricula:
    """
    __rut=''
    __nombres=''
    __apellidosP=''
    __apellidosM=''
    __direccion=''
    __comuna=''
    __cuidad=''
    __telefono=''
    __fechaInscripcion=''
    __semestre=''
    __cuota=0
    __arancel=0
    __carrera=''
    __sede=''
    __estadopago=False
    """ 
    def ingresarMatricula(self):
        """
        rut = input("Ingrese Rut del Alumno (Sin puntos): ")
        nombres = input("Ingrese Nombre del Alumno: ")
        apellidoP = input("Ingrese Apellido Paterno del Alumno: ")
        apellidoM = input("Ingrese Apellido Materno del Alumno: ")
        direccion = input("Ingrese Direccion del Alumno: ")
        comuna = input("Ingrese Comuna del Alumno: ")
        ciudad = input("Ingrese cuidad del Alumno: ")
        telefono = int(input("Ingrese telefono del Alumno: "))
        fechaInscripcion = input("Ingrese fechaInscripcion del Alumno: ")
        semestre = input("Ingrese semestre del Alumno: ")
        cuota = int(input("Ingrese cuota del Alumno: "))
        arancel = int(input("Ingrese arancel del Alumno: "))
        carrera = input("Ingrese carrera del Alumno: ")
        sede = input("Ingrese sede del Alumno: ")
        estadopago = input("Ingrese estadopago del Alumno: ")
        area = "Tecnologías de Información y Ciberseguridad"
        #Creacion de Correo
        cadena = nombres[:1]
        cadena2 = apellidoP[:3]
        cadena3 = apellidoM[:3]
        correo = cadena + cadena2 + cadena3 + "@inacapmail.cl" 
         """ 
        rut = "16916296-4"
        nombres = "Prueba"
        apellidoP = "Super"
        apellidoM = "Mega"
        direccion = "asdasd"
        comuna = "asdasdasd"
        ciudad = "asdasdasd"
        telefono = 541564
        fechaInscripcion = "sadasdasd"
        semestre = "asdasd"
        cuota = 12
        arancel = 12312312
        carrera = "asdasdasd"
        sede = "asdasdasd"
        estadopago = "asdasdasdasd"
        area = "Tecnologías de Información y Ciberseguridad"
        #Creacion de Correo
        cadena = nombres[:1]
        cadena2 = apellidoP[:3]
        cadena3 = apellidoM[:3]
        correo = cadena + cadena2 + cadena3 + "@inacapmail.cl" 
        correo.lower()
        
        if len(rut) == 10:  
            contraseña = rut[:8]
        if len(rut) == 9:
            contraseña = rut[:7]
               
        try: 
                cn= Conexion()
                cursor = cn.conexion.cursor()
                
                SQL = "insert into Estudiante (tipousuario, rut, nombres, apellidop, apellidom, direccion, comuna, ciudad, telefono, correo, contraseña, area) "
                SQL = SQL + f" values ('Estudiante', '{rut}', '{nombres}', '{apellidoP}', '{apellidoM}', '{direccion}', '{comuna}', '{ciudad}', '{telefono}', "
                SQL = SQL + f" '{correo}','{contraseña}', '{area}') "

            
                cursor.execute (SQL)
                cn.conexion.commit()
                
                print("\n****** Estudiante Ingresado Correctamente *****\n")
                
                for estudiante_idestudiante in cursor.execute("SELECT idestudiante FROM Estudiante WHERE idestudiante=(SELECT max(idestudiante) FROM Estudiante)"):
                 estudiante_idestudiante = str(estudiante_idestudiante)
                 estudiante_idestudiante= estudiante_idestudiante[1:-2]
                 estudiante_idestudiante = int(estudiante_idestudiante)               
                 print("")
                 
                cn2= Conexion()
                cursor2 = cn2.conexion.cursor()
                
                SQL2 = "insert into Matricula ( rut, nombres, apellidop, apellidom, direccion, comuna, ciudad, telefono, fechainscripcion, "
                SQL2 = SQL2+ " semestre, cuota, arancel, carrera, sede, estudiante_idestudiante, estadopago)"
                SQL2 = SQL2 + f" values ('{rut}', '{nombres}', '{apellidoP}', '{apellidoM}', '{direccion}', '{comuna}', '{ciudad}', '{telefono}', '{fechaInscripcion}', "
                SQL2 = SQL2 + f" '{semestre}', '{cuota}', '{arancel}', '{carrera}', '{sede}','{estudiante_idestudiante}', '{estadopago}' )"
                cursor2.execute (SQL2)
                cn2.conexion.commit()
                print("\n****** Alumno Matriculado Correctamente *****\n")
                
        except Exception as ex:
                print(ex)

         