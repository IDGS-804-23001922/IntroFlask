from flask import Flask, render_template, request,flash
import math
import forms
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.secret_key = 'clave-super-secreta-123'  # obligatoria

csrf = CSRFProtect(app)


app = Flask(__name__)
app.secret_key = 'clave_secreta'
csrf = CSRFProtect()

@app.route('/')
def index():
    title ='IDGS804 - INTRO FLASK'
    listado=['juan','ana','pedro','pablo']
    return render_template('index.html',title=title, listado=listado)

@app.route('/saludo1')
def saludo1():
    return render_template('saludo1.html')

@app.route('/saludo2')
def saludo2():
    return render_template('saludo2.html')

@app.route('/hola')
def ind():
    return 'Hola, Mundo - Hola'

@app.route("/user/<string:user>")
def func(user):
    return f'hola, {user}'

@app.route("/numero/<int:n>")
def numero(n):
    return f'<h1>Numero: {n}</h1>'

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f'<h1>Hola {username}, tu ID es {id}</h1>'

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f'<h1>La suma es: {n1 + n2}</h1>'

@app.route("/default/")
@app.route("/default/<string:param>")
def func2(param='juan'):
    return f'<h1>Hola, {param}</h1>'

@app.route("/operas")
def operas():
    return '''
    <form>
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="apaterno">APaterno:</label>
        <input type="text" id="apaterno" name="apaterno" required><br><br>

        <input type="submit" value="Enviar">
    </form>
    '''

@app.route("/OperasBas")
def OperasBas():
    return render_template('operasBas.html')

@app.route("/resultado", methods=['GET','POST'])
def resul1():
    n1=request.form.get('num1')
    n2=request.form.get('num2')
    return f"<h1>la suma es: {float(n1)+float(n2)}</h1>"

@app.route("/operabass", methods=['GET','POST'])
def operabass():
    res=None
    if request.method=='POST':
        n1=request.form.get('n1')
        n2=request.form.get('n2')
        if request.form.get('opera')=='suma':
            res=float(n1)+float(n2)
        if request.form.get('opera')=='resta':
            res=float(n1)-float(n2)
        if request.form.get('opera')=='multip':
            res=float(n1)*float(n2)
        if request.form.get('opera')=='division':
            res=float(n1)/float(n2)

    return render_template('operasBas.html',res=res)

@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
    res = 0

    if request.method == 'POST':
        x1 = int(request.form['x1'])
        y1 = int(request.form['y1'])
        x2 = int(request.form['x2'])
        y2 = int(request.form['y2'])

        res = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

    return render_template('distacia.html', res=res)

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom=''
    ape=''
    email=''
    alumno_clas=forms.userForm(request.form)
    if request.method=='POST' and alumno_clas.validate():
        mat=alumno_clas.matricula.data
        nom=alumno_clas.nombre.data
        ape=alumno_clas.apellido.data
        email=alumno_clas.correo.data
    return render_template('alumnos.html',form=alumno_clas,mat=mat,nom=nom,ape=ape,email=email)



@app.route("/cinepolis", methods=['GET', 'POST'])
def cine():

    total = None
    error = ""

    form = forms.CinepolisForm()

    if form.validate_on_submit():

        nombre = form.nombre.data
        compradores = form.compradores.data
        boletos = form.boletos.data
        tarjeta = form.tarjeta.data

        precio = 12.000
        max_boletos = compradores * 7

        if boletos > max_boletos:
            flash(f"No puedes comprar {boletos}. Máximo: {max_boletos} (7 por persona).", "error")
            total = None
            return render_template("cinepolis.html", form=form, total=total, error=error)

        subtotal = boletos * precio

        descuento = 0
        if boletos >= 3 and boletos <= 5:
            descuento = 0.10
        elif boletos > 5:
            descuento = 0.15

        total = subtotal - (subtotal * descuento)

        if tarjeta == "si":
            total = total - (total * 0.10)

        total = round(total, 2)

    elif request.method == "POST":
        error = "Revisa los datos, algo está mal."

    return render_template("cinepolis.html", form=form, total=total, error=error)

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)
