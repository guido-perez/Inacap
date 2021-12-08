
from Conexion import Conexion
from datetime import datetime


class Matricula:
    idCarrera=''
    cuota=0
    arancel=0
    carrera=''
    area=''
    def MostrarCarrera(self):
        print("ID |     Carrera           |    Area                                            | Arancel") 
        try: 
            cn= Conexion()
            cursor = cn.conexion.cursor()
                
            SQL = "select * from Carrera"
            

               
            for row in cursor.execute(SQL): 
               print(row)

        except Exception as ex:
                print(ex)

        
        idEstudiante = int(input("\nSelecciona ID carrara para Matricularse: "))
        Matricula.idCarrera=idEstudiante
        
        Matricula.carrera= row[1]
        Matricula.area=row[2]

    def CalcularCuota(self):
        Matricula.idCarrera
        try: 
            cn= Conexion()
            cursor = cn.conexion.cursor()
                
            SQL = f"select arancel from carrera where idcarrera='{Matricula.idCarrera}' "
               
            for row in cursor.execute(SQL): 
              row = str(row)
              row = row[1:-2]
              row = int(row)    
            Matricula.arancel = row 
            
            meses = int(input("\nIndique la cantidad de cuotas a pagar por semestre: "))
            cuota = Matricula.arancel / meses
            cuoda = round(cuota,3)
            cuota = int(cuota)
            
            Matricula.cuota = cuota
            
            print(f"\nValor por cuota es de {cuota} durante {meses} meses ")
                       
        except Exception as ex:
                print(ex)


     
    def ingresarMatricula(self):
        #Ingreso de Datos 
        rut = input("Ingrese Rut del Alumno (Sin puntos): ")
        nombres = input("Ingrese Nombre del Alumno: ")
        apellidoP = input("Ingrese Apellido Paterno del Alumno: ")
        apellidoM = input("Ingrese Apellido Materno del Alumno: ")
        direccion = input("Ingrese Direccion del Alumno: ")
        comuna = input("Ingrese Comuna del Alumno: ")
        ciudad = input("Ingrese cuidad del Alumno: ")
        telefono = int(input("Ingrese telefono del Alumno: "))
        date = datetime.now()
        fechaInscripcion = date.strftime('%d/%b/%Y')
        semestre = input("Ingrese semestre del Alumno: ")
        cuota = Matricula.cuota 
        arancel = Matricula.arancel 
        carrera = Matricula.carrera
        sede = input("Ingrese sede del Alumno: ")
        estadopago = input("Ingrese estadopago del Alumno: ")
        #area = Matricula.area
    
        
        #Creacion de Correo
        cadena = nombres[:1]
        cadena2 = apellidoP[:3]
        cadena3 = apellidoM[:3]
        correo = cadena + cadena2 + cadena3 + "@inacapmail.cl" 
        correo = correo.lower()
        
        #Asignar Contraseña
        
        if len(rut) == 10:  
            contraseña = rut[:8]
        if len(rut) == 9:
            contraseña = rut[:7]
        
          
        try: 
                cn= Conexion()
                cursor = cn.conexion.cursor()
                
                SQL = "insert into Estudiante (tipousuario, rut, nombres, apellidop, apellidom, direccion, comuna, ciudad, telefono, correo, contraseña, idcarrera, idseccion) "
                SQL = SQL + f" values ('Estudiante', '{rut}', '{nombres}', '{apellidoP}', '{apellidoM}', '{direccion}', '{comuna}', '{ciudad}', '{telefono}', "
                SQL = SQL + f" '{correo}','{contraseña}', '{Matricula.idCarrera}', '1') "
                #Falta validar con un contar si la seccion es > a 15 o 20 cambiar a id 2 en referencia a curso completo. 
                #alter sequence estudiante_idestudiante_seq restart start with 1;
                
                cursor.execute (SQL)
                cn.conexion.commit()
                
                print("\n****** Estudiante Ingresado Correctamente *****\n")
                
                # Intente un Last_Value e intente un :new o sql un last_insert_id()
                
              
                #Obtener el Ultimo ID Ingresado
                for estudiante_idestudiante in cursor.execute("SELECT idestudiante FROM Estudiante WHERE idestudiante=(SELECT max(idestudiante) FROM Estudiante)"):
                 estudiante_idestudiante = str(estudiante_idestudiante)
                 estudiante_idestudiante= estudiante_idestudiante[1:-2]
                 estudiante_idestudiante = int(estudiante_idestudiante)               
               
                cn2= Conexion()
                cursor2 = cn2.conexion.cursor()
                 
                SQL2 = "insert into Matricula ( rut, nombres, apellidop, apellidom, direccion, comuna, ciudad, telefono, fechainscripcion, "
                SQL2 = SQL2+ " semestre, cuota, arancel, idcarrera, sede, idestudiante, estadopago)"
                SQL2 = SQL2 + f" values ('{rut}', '{nombres}', '{apellidoP}', '{apellidoM}', '{direccion}', '{comuna}', '{ciudad}', '{telefono}', to_date(sysdate, 'dd/mm/yyyy'), "
                SQL2 = SQL2 + f" '{semestre}', '{cuota}', '{arancel}', '{Matricula.idCarrera}', '{sede}', '{estudiante_idestudiante}', '{estadopago}')"
                cursor2.execute (SQL2)
                cn2.conexion.commit()
                print("\n****** Alumno Matriculado Correctamente *******\n")
                
        except Exception as ex:
                print(ex)

         