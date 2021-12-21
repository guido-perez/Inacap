from Conexion import Conexion


class estudiante:

    def verNotas(self):
        
        try:
            
            idest= input(" Indique su ID de estudiante para ver sus notas: ") 
            cn1= Conexion()
            cursor = cn1.conexion.cursor()                      
            SQL0 = f"select m.modulo, n.nota_1, n.nota_1, n.nota_1, n.nota_1, nota_examen from nota n "
            SQL0 = SQL0 + f"inner join modulo m on n.id_modulo=m.id_modulo "
            SQL0 = SQL0 + f"where id_estudiante='{idest}'"
            for row in cursor.execute(SQL0):
                    print("****************************************************")
                    print(f"{row[0]}")
                    print("*****************************************************")
                    print("                                                     ")   
                    print(f"Nota 1: {row[1]}                                    ")
                    print(f"Nota 2: {row[2]}                                    ")
                    print(f"Nota 3: {row[3]}                                    ")
                    print(f"Nota 4: {row[4]}                                    ")
                    print(f"Nota Examen: {row[5]}                               ")
                    print("                                                     ")  

        except Exception as ex:
                print(ex)
        