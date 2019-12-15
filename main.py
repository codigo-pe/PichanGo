from flask import Flask,url_for,render_template,abort
#creando la aplicacion
app=Flask(__name__)

#definimos la ruta index que va a llamr a Home.html
@app.route('/')
def index():
    return render_template("Home.html")

@app.route('/perfil')
def Perfil():
    return render_template("Perfil.html")

@app.route('/QuienesSomos')
def Quienes_Somos():
    return render_template("QuienesSomos.html")

@app.route('/registrar')
def Registrar():
    return render_template("registrarvista.html")

@app.route('/login')
def login():
    return render_template("loginvista.html")

@app.errorhandler(404)
def page_not_found(error):
    return "Lo lamentamos, tenemos unos inconvenientes, revisaremos el VAR",404
app.run(debug=True,port=8000)