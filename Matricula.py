
from Conexion import Conexion
from datetime import datetime, date
import hashlib
import UF 

class Matricula:
    idCarrera=''
    cuota=0
    arancel=0
    carrera=''
    area=''
    idTransaccion=''
    valorCuota=0
    cantidadUF = 0
    cuotaUF = 0
    aux=0
    contraseña = ''
    def MostrarCarrera(self):
        print("ID |     Carrera                  ") 
        #
        try: 
            cn= Conexion()
            cursor = cn.conexion.cursor()   
            SQL = "select * from Carrera"
            for row in cursor.execute(SQL):
                print(row[0]," | ", row[1])

        except Exception as ex:
                print(ex)

        Matricula.idCarrera = int(input("\nSelecciona ID Carrera para Matricularse: "))  
        
        
    def CalcularCuota(self):
       
        #Asignamos las variables segun la variable obtenida
        
        try: 
            cn= Conexion()
            cursor = cn.conexion.cursor()   
            SQL = f"select * from Carrera where id_carrera='{Matricula.idCarrera}'"
            for row in cursor.execute(SQL): 
               pass

        except Exception as ex:
                print(ex)
    
        Matricula.carrera= row[1]
        Matricula.arancel=row[2]
        Matricula.area=row[3]
        
        print(f"El arancel de la carrera seleccionada es: {Matricula.arancel}")
        
        Matricula.cuota = int(input("Selecciones la cantidad de cuota para pagar arancel semestral entre 1 y 5: "))
        if Matricula.cuota <= 5 and Matricula.cuota >= 1:
            
            print(f"El arancel de la carrera seleccionada es: {Matricula.arancel}")
            print("El valor de la matricula es de $136.000 ") 
            print(f"Las cuotas se paga al valor UF del dia. UF es de hoy es {UF.valorUF}")
            Matricula.cantidadUF = Matricula.arancel / UF.valorUF # Se guarda en la BD
            Matricula.cuotaUF =  Matricula.cantidadUF / Matricula.cuota # Se guarda en la BD
            Matricula.valorCuota = int(Matricula.cuotaUF * UF.valorUF)
            print(f"Ud debera pagar {Matricula.cuota} cuotas de {Matricula.valorCuota}")
            
            print("**********************************************************")
            print("El valor cuota se calcula aL valor de la UF del dia    ")
            print("**********************************************************")
        else:
            print("Ingrese un numero entre 1 y 5")
       
    def Transaccion(self):
        
        print("Portal de Pago")
        rut = input("\nIngrese el rut del alumno matriculado: ")
        
        try: 
            cn= Conexion()
            cursor = cn.conexion.cursor()   
            SQL = f"select m.id_matricula, m.rut, c.carrera from matricula m "
            SQL = SQL + f"inner join carrera c on c.id_carrera=m.id_carrera "
            SQL = SQL + f" where rut='{rut}'"
            
            contador = 0
            for row in cursor.execute(SQL):
                print("ID |        RUT           |       CARRERA                    ")
                print(row[0]," | ",row[1],"     | ", row[2])   
                contador=contador+1
            if contador > 1:
                print(f"condador {contador}")

                Matricula.aux = input("Seleccione la Matricula a pagar: ")
              
        except Exception as ex:
                print(ex)
    
        #Ingresos a Transaccion
        tipo_pago = input("Indique el medio de Pago (Efectivo - Tarjeta de Debido - Tarjeta de Credito) : ") 
        concepto_pago = "Colegiatura"   
          
        try: 
                #Insertamos los datos a la tabla transaccion
                cn= Conexion()
                cursor = cn.conexion.cursor()
                
                SQL = "insert into transaccion (total, fecha, cantidad_cuota) "
                SQL = SQL + f" values ('{Matricula.arancel}', to_date(sysdate, 'dd/mm/yyyy'), '{Matricula.cuota}') "
                #Insertamos los valores obtenidos el Arancel que es el total del pago, la fecha del dia y la cantidad de cuotas seleccionadas
                
                cursor.execute (SQL)
                cn.conexion.commit()
                
                print("\n****** Transaccion realizada Correctamente *****\n")
                
                #Obtener el Ultimo ID Ingresado de transaccion
                for id in cursor.execute("SELECT id_transaccion FROM transaccion WHERE id_transaccion=(SELECT max(id_transaccion) FROM transaccion)"):
                    Matricula.idTransaccion = id[0]               
               
                #Insertamos el detalle de la transaccion ingresada
                cn2= Conexion()
                cursor2 = cn2.conexion.cursor()
                    
                if Matricula.cuota > 1:
                    for i in range(1,Matricula.cuota+1):
                        SQL2 = "insert into detalle_pago ( tipo_pago, cuota, valor_cuota, fecha_vencimiento, uf_dia, estado_pago, concepto_pago, id_transaccion, cantidad_uf, cuota_uf) "
                        SQL2 = SQL2 + f" values ('{tipo_pago}', '{i}', '{Matricula.valorCuota}', last_day(add_months(to_date(sysdate, 'dd/mm/yyyy'),-1+{i})), '{UF.valorUF}', 'Pendiente', "
                        SQL2 = SQL2 + f"'{concepto_pago}', '{Matricula.idTransaccion}', '{Matricula.cantidadUF}','{Matricula.cuotaUF}')"
                        cursor2.execute (SQL2)
                        cn2.conexion.commit()
                            
                else: 
                        SQL2 = "insert into detalle_pago ( tipo_pago, cuota, valor_cuota, fecha_vencimiento, uf_dia, estado_pago, concepto_pago, id_transaccion, cantidad_uf, cuota_uf) "
                        SQL2 = SQL2 + f" values ('{tipo_pago}', '{Matricula.cuota}', '{Matricula.valorCuota}', last_day(to_date(sysdate, 'dd/mm/yyyy')), '{UF.valorUF}', 'Pendiente', "
                        SQL2 = SQL2 + f"'{concepto_pago}', '{Matricula.idTransaccion}', '{Matricula.cantidadUF}','{Matricula.cuotaUF}')"
                        cursor2.execute (SQL2)
                        cn2.conexion.commit()
                        
                #Creamos el registro de la matricula
                #La matricula se debe  antes de la e a fecha vencimiento de la primera cuota o se anulara aumaticamente mediante un trigger 
                cn= Conexion()
                cursor = cn.conexion.cursor()
                SQL2 = "insert into detalle_pago ( tipo_pago, valor_cuota,fecha_vencimiento, estado_pago, concepto_pago, id_transaccion) "
                SQL2 = SQL2 + f" values ('{tipo_pago}', '136000',last_day(to_date(sysdate, 'dd/mm/yyyy')), 'Pendiente', 'Matricula', '{Matricula.idTransaccion}')"
                cursor.execute (SQL2)
                cn.conexion.commit()
      
                print("\n****** Cuponera de Pago creada Correctamente *******\n")
                        
                #Actualizamos la tabla Matricula con la ID de transaccion 
                cn= Conexion()
                cursor = cn.conexion.cursor()
                if contador > 1:
                    SQL = f"update matricula set id_transaccion='{Matricula.idTransaccion}'"
                    SQL = SQL + f" where rut='{rut}' and id_matricula='{Matricula.aux}' "
                else:
                    SQL = f"update matricula set id_transaccion='{Matricula.idTransaccion}'"
                    SQL = SQL + f" where rut='{rut}' "
                cursor.execute (SQL)
                cn.conexion.commit()
                
        except Exception as ex:
                print(ex) 


    def ModificarCuponera(self):
        
        print("Portal de Pago")
        rut = input("\nIngrese el rut del alumno matriculado: ")
        
        try: 
            cn= Conexion()
            cursor = cn.conexion.cursor()   
            SQL = f"select m.id_matricula, m.rut, c.carrera, m.id_transaccion from matricula m "
            SQL = SQL + f"inner join carrera c on c.id_carrera=m.id_carrera "
            SQL = SQL + f" where rut='{rut}'"
            
            contador = 0
            for row in cursor.execute(SQL):
                print("ID |        RUT           |       CARRERA                    ")
                print(row[0]," | ",row[1],"     | ", row[2])
                Matricula.aux = row[0]                  #automaticamente asignamos el valor de id matricula para realizar la comparativa de la cuponera   
                Matricula.idTransaccion = row[3]
                
                contador=contador+1
            if contador > 1:
                print(f"condador {contador}")
                Matricula.aux = input("Seleccione la Matricula a pagar: ")
                
                #validacion en caso de tener mas de una carrera para pagar matricula
                cn= Conexion()
                cursor = cn.conexion.cursor()   
                SQL = f"select m.id_transaccion from matricula m "
                SQL = SQL + f" where id_matricula='{Matricula.aux}'"
                for row in cursor.execute(SQL):
                    Matricula.idTransaccion = row[0]   
          
        except Exception as ex:
                print(ex)
      
        #Ingresos a Transaccion
        concepto_pago = input("Indique el concepto de Pago (Matricula - Colegiatura) : ") 
        if concepto_pago == 'Matricula' or concepto_pago == 'matricula': 
           Matricula.valorCuota = 136000
           print("El valor de la matricula es de $136.000 ") 
        tipo_pago = input("Indique el medio de Pago (Efectivo - Tarjeta de Debido - Tarjeta de Credito) : ")

        # UPDATEEEE  
        try: 
            
                if concepto_pago == 'Matricula' or concepto_pago == 'matricula':
                    #Si elije pagar la matricula validamos
                    #Actualizamos el detalle de la transaccion ingresada en la funcion transaccion. cambiando el estado de pago
                    cn= Conexion()
                    cursor = cn.conexion.cursor()
                    SQL2 = f"update detalle_pago set estado_pago='Pagada', valor_cuota=136000, fecha_pago=to_date(sysdate, 'dd/mm/yyyy') where id_transaccion='{Matricula.idTransaccion}' and concepto_pago='Matricula' "
                    cursor.execute (SQL2)
                    cn.conexion.commit()
                    
                    #Mostramos Comprobante 
                    
                    
                    cn= Conexion()
                    cursor = cn.conexion.cursor()   
                    SQL = f"select concepto_pago, to_char(fecha_pago, 'dd/mm/yy'), valor_cuota from detalle_pago where id_transaccion='{Matricula.idTransaccion}' and concepto_pago='Matricula' "
                    for row in cursor.execute(SQL):
                      pass
                    print("******************************************************")
                    print("Comprobante de Pago")
                    print("*****************************************************")
                    print("                                                     ")   
                    print(f"Concepto pago: {row[0]}                             ")
                    print(f"Fecha de Pago: {row[1]}                             ")
                    print(f"Monto a Pagar: {row[2]}                             ")
                    print("                                                     ")
                    print("\n****** Matricula de Pagada Correctamente *******\n ")
                    print("*****************************************************")
                    
                else:    
                    #Mostrar Cuponera validando que sea la carrera por id_matricula 
                    cn= Conexion()
                    cursor = cn.conexion.cursor()   
                    SQL = f"select d.cuota, d.tipo_pago, d.valor_cuota, d.uf_dia, to_char(d.fecha_vencimiento,'dd/mm/yy'), d.concepto_pago, d.estado_pago from detalle_pago d "
                    SQL = SQL + f" inner join transaccion t on d.id_transaccion = t.id_transaccion "
                    SQL = SQL + f" inner join matricula m on t.id_transaccion = m.id_transaccion  "
                    SQL = SQL + f" where m.rut='{rut}' and m.id_matricula='{Matricula.aux}' and d.estado_pago='Pendiente' "
                    
                    for row in cursor.execute(SQL):
                        print(row)
                
                    if Matricula.cuota > 1:
                        for i in range(1,Matricula.cuota+1):
                            SQL2 = "insert into detalle_pago ( tipo_pago, cuota, valor_cuota, fecha_vencimiento, uf_dia, estado_pago, concepto_pago, id_transaccion, cantidad_uf, cuota_uf) "
                            SQL2 = SQL2 + f" values ('{tipo_pago}', '{i}', '{Matricula.valorCuota}', last_day(add_months(to_date(sysdate, 'dd/mm/yyyy'),-1+{i})), '{UF.valorUF}', 'Pendiente', "
                            SQL2 = SQL2 + f"'{concepto_pago}', '{id}', '{Matricula.cantidadUF}','{Matricula.cuotaUF}')"
                            cursor2.execute (SQL2)
                            cn2.conexion.commit()
                    else: 
                            SQL2 = "insert into detalle_pago ( tipo_pago, cuota, valor_cuota, fecha_vencimiento, uf_dia, estado_pago, concepto_pago, id_transaccion, cantidad_uf, cuota_uf) "
                            SQL2 = SQL2 + f" values ('{tipo_pago}', '{Matricula.cuota}', '{Matricula.valorCuota}', last_day(to_date(sysdate, 'dd/mm/yyyy')), '{UF.valorUF}', 'Pendiente', "
                            SQL2 = SQL2 + f"'{concepto_pago}', '{id}', '{Matricula.cantidadUF}','{Matricula.cuotaUF}')"
                            cursor2.execute (SQL2)
                            cn2.conexion.commit()
                    print("\n****** Cuponera de Pago creada Correctamente *******\n")
                
                #Actualizamos la tabla Matricula con la ID de transaccion 
                cn= Conexion()
                cursor = cn.conexion.cursor()
                if contador > 1:
                    SQL = f"update matricula set id_transaccion='{id}'"
                    SQL = SQL + f" where rut='{rut}' and id_matricula='{Matricula.aux}' "
                else:
                    SQL = f"update matricula set id_transaccion='{id}'"
                    SQL = SQL + f" where rut='{rut}' "
                cursor.execute (SQL)
                cn.conexion.commit()
                
        except Exception as ex:
                print(ex) 



     
    def ingresarMatricula(self):
        
        #Ingreso de Datos para Matricularse
        print("\nFormulario Matricula \n")
        rut = input("Ingrese Rut del Alumno (Sin puntos): ")
        
        #Creacion de contraseña y validacion de contraseña
        clave = input("Ingrese una contraseña : ")
        Matricula.contraseña=hashlib.md5(clave.encode('utf-8')).hexdigest() #Contraseña encryptada con md5
        
        nombres = input("Ingrese Nombre del Alumno: ")
        apellidoP = input("Ingrese Apellido Paterno del Alumno: ")
        apellidoM = input("Ingrese Apellido Materno del Alumno: ")
        direccion = input("Ingrese Direccion del Alumno: ")
        comuna = input("Ingrese Comuna del Alumno: ")
        ciudad = input("Ingrese cuidad del Alumno: ")
        telefono = int(input("Ingrese telefono del Alumno: "))
        semestre = input("Ingrese semestre del Alumno: ")
        sede = input("Ingrese sede del Alumno: ")
        valor_matricula= 136000

        #Creacion de Correo
        cadena = nombres[:1]
        cadena2 = apellidoP[:3]
        cadena3 = apellidoM[:3]
        correo = cadena + cadena2 + cadena3 + "@inacapmail.cl" 
        correo = correo.lower()
        

          
        try: 
                cn= Conexion()
                cursor = cn.conexion.cursor()
                
                SQL = "insert into Estudiante (tipo_usuario, nombres, apellidop, apellidom, rut, direccion, comuna, ciudad, telefono, correo, contraseña) "
                SQL = SQL + f" values ('Estudiante', '{nombres}', '{apellidoP}', '{apellidoM}', '{rut}', '{direccion}', '{comuna}', '{ciudad}', '{telefono}', "
                SQL = SQL + f" '{correo}','{Matricula.contraseña}') "
                #Falta validar con un contar si la seccion es > a 15 o 20 cambiar a id 2 en referencia a curso completo. 
                #alter sequence estudiante_idestudiante_seq restart start with 1;
                
                cursor.execute (SQL)
                cn.conexion.commit()
                
                print("\n****** Estudiante Ingresado Correctamente *****\n")
                
                # Intente un Last_Value e intente un :new o sql un last_insert_id()
                
              
                #Obtener el Ultimo ID Ingresado
                for id_estudiante in cursor.execute("SELECT id_estudiante FROM Estudiante WHERE id_estudiante=(SELECT max(id_estudiante) FROM Estudiante)"):
                  id_estudiante = id_estudiante[0]               
               
                cn2= Conexion()
                cursor2 = cn2.conexion.cursor()
                
                SQL2 = "insert into Matricula ( fecha_matricula, semestre, sede, rut, nombres, apellidop, apellidom, direccion, comuna, ciudad, telefono,  "
                SQL2 = SQL2+ " valor_matricula, estado_matricula, id_estudiante, id_carrera)"
                SQL2 = SQL2 + f" values ( to_date(sysdate, 'dd/mm/yyyy'), '{semestre}', '{sede}', '{rut}', '{nombres}', '{apellidoP}', '{apellidoM}', '{direccion}', '{comuna}', '{ciudad}', '{telefono}', "
                SQL2 = SQL2 + f"  '{valor_matricula}','Pendiente','{id_estudiante}', '{Matricula.idCarrera}')"
                cursor2.execute (SQL2)
                cn2.conexion.commit()
                print("\n****** Alumno Matriculado Correctamente *******\n")
                print("**********************************************************")
                print("Recuerde realizar el pago de matricula de lo contrario su matricula se Anulara")
                print("**********************************************************")

                
        except Exception as ex:
                print(ex)

    def AnularMatricula(self):
            
            print("\n            Lista Alumnos            ")
            print("")
            print("     Nombre          |         Rut   ")
            print("")
            try:

                cn1= Conexion()
                cursor = cn1.conexion.cursor()
                SQL0 = f"Select distinct nombres, apellidop, rut from estudiante "
                for row in cursor.execute(SQL0):
                 print(row[0],row[1]+ "     |     " + row[2])
    
            except Exception as ex:
                print(ex)
            
            rut= input("Ingrese Rut del Estudiante Para Anular Matricula: ")
            
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                    
                SQL0 = f"DELETE FROM estudiante WHERE rut='{rut}' "
                cursor.execute(SQL0)
                cn1.conexion.commit()
            except Exception as ex:
                        print(ex)
            try:
                cn1= Conexion()
                cursor = cn1.conexion.cursor()                    
                SQL0 = f"DELETE FROM matricula WHERE rut='{rut}' "
                cursor.execute(SQL0)
                cn1.conexion.commit()
                print("  Matricula Anulada y Estudiante Eliminado  ")

            except Exception as ex:
                        print(ex)
            
            try:

                cn1= Conexion()
                cursor = cn1.conexion.cursor()
                SQL0 = f"Select distinct nombres, apellidop, rut from estudiante "
                for row in cursor.execute(SQL0):
                 print(row[0],row[1]+ "     |     " + row[2])
   
            except Exception as ex:

                return"Lista Actualizada"
                    
    def ActualizarMatricula(self):

            print("ingrese rut de la matricula a actualizar'")

            rut=input("rut: ")
            nombres=input("Ingrese nombre nuevo: ")
            apellidop=input("Ingrese Apellido Paterno: ")
            apellidom=input("Ingrese Apellido Materno: ")
                        
            try:

                cn1= Conexion()

                cursor = cn1.conexion.cursor()

                       

                SQL0 = f"update matricula set nombres='{nombres}', apellidop='{apellidop}', apellidom='{apellidom}' "
                SQL0 = SQL0 + f" where rut='{rut}'"

                cursor.execute(SQL0)
                cn1.conexion.commit()

                print(" Datos Actualizados con Exito  ")              



            except Exception as ex:

                        print(ex)



        #Funciones Delete
            