from flask import Flask, render_template, abort
app = Flask(__name__)

#La página principal debe mostrar una página donde ponga vuestro nombre y 
#una lista de enlaces a las diferentes páginas (para probar como funcionan). 
#Cada una de las páginas deberá tener un enlace a la página principal.

@app.route('/',methods=["GET","POST"])
def inicio():
    return render_template("inicio.html")

#Si el exponente es positivo, el resultado es la potencia.
#Si el exponente es 0, el resultado es 1.
#Si el exponente es negativo, el resultado es 1/potencia con el exponente positivo.

@app.route('/potencia/')
def potencia():
    return render_template("potencia.html")

#Página potencia: Se accede con la URL /potencia/base/exponente (siendo base y exponente dos números enteros). 
#Se muestra una página dinámica donde se muestra un título "Calcular potencia", se muestra la base y el exponente 
#y se muestra el resultado:

@app.route('/potencia/<int:num1>/<num2>',methods=["GET","POST"])
def calcularpotencia(num1,num2):
#Si el exponente es positivo, el resultado es la potencia.
#Si el exponente es 0, el resultado es 1.
#Si el exponente es negativo, el resultado es 1/potencia con el exponente positivo.
    base=num1
    exponente=int(num2)
    if exponente>0:
        resultado = base**exponente
    elif exponente==0:
        resultado = 1
    elif exponente < 0:
        resultado = 1/base**exponente
    return render_template("potencia.html",num1=base,num2=exponente,res=resultado)

#Página cuenta letras: Se accede con la URL /cuenta/palabra/letra (siendo palabra y letra dos cadenas cualquiera). 

@app.route('/letras')
def letras():
    return render_template("letras.html")

#Página cuenta letras: Se accede con la URL /cuenta/palabra/letra (siendo palabra y letra dos cadenas cualquiera).
@app.route('/cuenta/<dato1>/<dato2>',methods=["GET","POST"])
def contar(dato1,dato2):
#Si la letra no es una cadena con un carácter se devuelve un error 404.
    palabra=dato1
    letra=dato2
    if len(letra) > 1:
        abort(404)
#muestra el siguiente mensaje "En la palabra ********* aparece *** veces el carácter ***".
    else:
        resultado=palabra.count(letra)

    return render_template("letras.html",dato1=palabra,dato2=letra,res=resultado)


@app.route('/libros')
def libros():
    return render_template("libros.html")

#Página libros: A esta página se entra con la URL /libro/codigo (siendo código un número entero). 
@app.route('/libro/<int:dato1>',methods=["GET","POST"])
def buscarcodigo(dato1):
#Tienes que buscar el código en el fichero libros.xml y debes mostrar una página con un título "Biblioteca" 
#y el nombre del libro y el autor. Si no existe el código debe devolver una respuesta 404.
    doc = etree.parse('libros.xml')
    codigo=dato1
    libro=doc.xpath('//libro/codigo[text()="%i"]/../titulo/text()' % codigo)
    autor=doc.xpath('//libro/codigo[text()="%i"]/../autor/text()' % codigo)
    if len(libro)  == 0:
        abort(404)
    return render_template("libros.html",libro=libro[0],autor=autor[0])

app.run("0.0.0.0",8000,debug=True)