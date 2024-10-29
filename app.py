from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "clave_secreta"

@app.route("/")
def index():
    if 'form_data' not in session:
        session['form_data'] = []
    return render_template('index.html', forms_data=session['form_data'])

# Formulario "Inscripción en curso"
@app.route("/inscripcion", methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        curso = request.form.get('curso')

        session['form_data'].append({'nombre': nombre, 'apellidos': apellidos, 'curso': curso})
        session.modified = True

        return redirect(url_for('index'))
    return render_template('inscripcion.html')

# Formulario "Registro de usuarios"
@app.route("/registro_usuarios", methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        email = request.form.get('email')
        password = request.form.get('password')

        session['form_data'].append({'nombre': nombre, 'apellidos': apellidos, 'email': email, 'password': password})
        session.modified = True

        return redirect(url_for('index'))
    return render_template('registro_usuarios.html')

# Formulario "Registro de productos"
@app.route("/registro_productos", methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form.get('producto')
        categoria = request.form.get('categoria')
        existencia = int(request.form.get('existencia'))
        precio = float(request.form.get('precio'))

        session['form_data'].append({'producto': producto, 'categoria': categoria, 'existencia': existencia, 'precio': precio})
        session.modified = True

        return redirect(url_for('index'))
    return render_template('registro_productos.html')

# Formulario "Registro de libros"
@app.route("/registro_libros", methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        resumen = request.form.get('resumen')
        medio_fisico = 'fisico' in request.form
        medio_magnetico = 'magnetico' in request.form

        session['form_data'].append({'titulo': titulo, 'autor': autor, 'resumen': resumen, 'medio_fisico': medio_fisico, 'medio_magnetico': medio_magnetico})
        session.modified = True

        return redirect(url_for('index'))
    return render_template('registro_libros.html')

@app.route("/vaciar")
def vaciar():
    session.pop('form_data', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
