
from fpdf import FPDF
from referencias import *
from Conexion import Conexion
import os

class PDF(FPDF):



        def header(self):
                self.image('logoInacap.png',
                x = 135, y = 10, w = 60, h = 30)

                self.set_font('Arial', '', 15)
                self.cell(w = 0, h = 30, txt = 'Comprobante de Pago',ln=2, border = 0, align = 'L', fill = 0, )
                self.multi_cell(w = 0, h = 15, txt = 'Codigo de Operacion:  ', border = 0, align = 'L', fill = 0)
                self.cell(w = 0, h = 0, txt = 'Medio de Pago: {} ',  border =0, align = 'L', fill = 0)
                                
                self.multi_cell(w = 0, h = 20, txt = '', border =0, align = 'L', fill = 0)
                self.ln(5)
                #self.multi_cell(w = 100, h = 15,  txt = '{variable}', border = 0, fill = 0)
                #self.multi_cell(w = 100, h = 15,  txt = '{variable}',  fill = 0)
                #http://www.fpdf.org/es/doc/cell.htm
                        
        # Page footer
        def footer(self):
                # Position at 1.5 cm from bottom
                self.set_y(-20)

                # Arial italic 8
                self.set_font('Arial', 'I', 12)

                # Page number
                self.cell(w = 0, h = 10, txt =  'Pagina ' + str(self.page_no()) + '/{nb}',
                border = 0,
                align = 'C', fill = 0)   


datos = (
        ('carlos@gmail.com', '05-02-2020','180000'),
        )
 
 
# datos para comprobante matricula
rut = input("\nIngrese el rut del alumno matriculado: ")
try:            
        cn= Conexion()
        SQL = f"select d.concepto_pago, to_char(fecha_pago, 'dd/mm/yy'), d.valor_cuota, d.tipo_pago, d.id_transaccion from detalle_pago d "
        SQL = SQL + f" inner join transaccion t on t.id_transaccion = d.id_transaccion "
        SQL = SQL + f" inner join matricula m on m.id_matricula = t.id_transaccion "
        SQL = SQL + f" where d.estado_pago='Pagada' and d.concepto_pago='Matricula' and m.rut='{rut}' "
        for row in cn.cursor.execute(SQL):
         datos = ((row),)
         
except Exception as ex:
                print(ex) 
            
"""

  
pdf = PDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.alias_nb_pages()

pdf.add_page()

# TEXTO
pdf.set_font('Arial', '', 15)
                
# titulo
pdf.cell(w = 0, h = 15, txt = 'Comprobante', border = 1, ln=1, align = 'C', fill = 0)

# encabezado
pdf.cell(w = 60, h = 15, txt = 'Concepto de Pago', border = 1, align = 'C', fill = 0)

pdf.cell(w = 70, h = 15, txt = 'Fecha de Pago', border = 1, align = 'C', fill = 0)

#MultiCell para que de un salto de linea
pdf.multi_cell(w = 0, h = 15, txt = 'Monto a Pagar', border = 1, align = 'C', fill = 0)

                                                
for valor in datos:

        pdf.cell(w = 60, h = 9, txt = str(valor[0]), border = 1, align = 'C', fill = 0)

        pdf.cell(w = 70, h = 9, txt = str(valor[1]), border = 1, align = 'C', fill = 0)
                        
        pdf.multi_cell(w = 0, h = 9, txt = str(valor[2]), border = 1, align = 'C', fill = 0)

pdf.output('Comprobante.pdf')

path = 'Comprobante.pdf'
os.system(path)