from flask import Flask, render_template
app = Flask(__name__)

#La página principal debe mostrar una página donde ponga vuestro nombre y 
#una lista de enlaces a las diferentes páginas (para probar como funcionan). 
#Cada una de las páginas deberá tener un enlace a la página principal.

@app.route('/',methods=["GET","POST"])
def inicio():
    return render_template("inicio.html")

#Página potencia: Se accede con la URL /potencia/base/exponente (siendo base y exponente dos números enteros). Se muestra una página dinámica donde se muestra un título "Calcular potencia", se muestra la base y el exponente y se muestra el resultado:
#Si el exponente es positivo, el resultado es la potencia.
#Si el exponente es 0, el resultado es 1.
#Si el exponente es negativo, el resultado es 1/potencia con el exponente positivo.

@app.route('/potencia/')
def potencia():
    return render_template("potencia.html")

@app.route('/potencia/<int:num1>/<num2>',methods=["GET","POST"])
def calcularpotencia(num1,num2):
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
#Si la letra no es una cadena con un carácter se devuelve un error 404. 
#Se muestra una página donde hay un título "Cuanta letras", 
#y muestra el siguiente mensaje "En la palabra ********* aparece *** veces el carácter ***".

@app.route('/letras')
def letras():
    return render_template("letras.html")










@app.route('/libros')
def libros():
    return render_template("libros.html")


app.run("0.0.0.0",8000,debug=True)