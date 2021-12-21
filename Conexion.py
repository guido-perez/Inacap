
from datetime import date
import cx_Oracle


class Conexion:    
    
    lib_dir = "C:\instantclient_21_3"
    try:
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
        conexion= cx_Oracle.connect(user="ADMIN", password="Inacap2021.-", dsn="dbprueba_high")
        cursor = conexion.cursor()   
                            
    except Exception as ex:
        print(ex)
        

      

"""" 
Pauta de Trabajo
  
1)asignar modulo a docente    jc.AsignarModDoc()   

2)ver módulos docente       doc.verModulos()

3)quitar módulos a docente    jc.eliminarMODDOC()

4)agregar modulo a sistema   jc.CrearModulo()  

5)editar modulo a sistema   jc.modificarModulo()

6)eliminar modulo a sistema   jc.EliminarModulo()

7)ver todos los módulos del sistema    jc.VerModulosSis() 

8)Inscribir alumno en modulo   jc.AsignarModEst()   jc.asignarSECEST()  

9)quitar alumno del modulo    jc.modificarModuloEst() 

10)cambiar alumno de sección  - modificarSECEST()

11)agregar nota a alumno   doc.agregarNota()

12)editar nota a alumno    doc.modificarNota() 

13)quitar nota a alumno     doc.eliminarNota() 

14)matricular alumno     mat.ingresarMatricula()

15)anular matricula  mat.AnularMatricula

16)editar matricula  mat.ActualizarMatricula()

17)listar alumnos matriculados    

II- Todas las opciones de quitar o eliminar se realizaran solicitando el

identificador único del elemento a eliminar.     OK

III-Todas las opciones de edición se deben realizar buscando por id y mostrar los valores actuales  - OK

IV-Todas las opciones de listar/mostrar deben mostrar todos los campos de los objetos  - OK

V-Los datos se deben guardar en listas dentro de los objetos  - OK
  
VI-Los datos de las listas se deben guardar en bases de datos Oracle - KO

VII-Para acceder al sistema debemos hacerlo mediante un login de usuario - OK

VIII-Encryptacion md5  - OK 

UF Y CUPONERA DE PAGO - OK

V
"""

