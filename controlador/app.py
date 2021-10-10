from flask import Flask,render_template,request
app = Flask(__name__, template_folder='../vista')

@app.route('/')
def inicio():
    return render_template('comunes/Principal.html')

@app.route('/consultarProductos')
def consultarProductos():
    return render_template('Productos/consultarProductos.html')

@app.route('/registrarProducto')
def registrarProducto():
    return render_template('Productos/registrarProducto.html')

@app.route('/registrarNuevoProducto',methods=['post'])
def registrarNuevoProducto():
    nombre = request.form['nombre']
    return 'Se a registrado el producto: '+nombre

if __name__ == '__main__':
    app.run(debug=True)