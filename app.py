from flask import Flask,render_template,request

app = Flask(__name__)

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

@app.route('/operasBas')
def operasbas():
    return render_template('operasBas.html')


@app.route('/resultado', methods=['GET', 'POST'])
def resul1():
    n1=request.form.get('num1')
    n2=request.form.get('num2')
    return f"<h1> la suma es: {float(n1)+float(n2)}</h1>"



if __name__ == '__main__':
    app.run(debug=True)
