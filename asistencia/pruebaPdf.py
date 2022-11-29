import pdfkit
import pdfminer
#from registroPas import Pasante
#r1 = Pasante()
#dato = r1.cajapasante.get()
a = '10000'
with open('prueba.html', 'w') as file:
    file.write('<h1>Hola Mundo</h1><br>')
    file.write('<h2>Pagina de Prueba PDF</h2><br>')
    file.write('<b>Resultado: </b>'+ a)
exe = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=exe)
pdfkit.from_file('prueba.html', 'prueba1.pdf', configuration=config)


