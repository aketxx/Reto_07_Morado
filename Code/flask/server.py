from flask import Flask, render_template, request, jsonify
from bbdd import con_sql

app = Flask(__name__)

con_sql.crear_tablas()

def francesa(monto, tasa=0.1, n=12):
    return round(monto * (tasa / (1 - (1+tasa)**-n)), 2)


def alemana(monto, tasa=0.1, n=12):
    capital = monto / n
    return [round(capital + monto*tasa,2) for _ in range(n)]

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/registro", methods=["GET","POST"])
def registro():

    if request.method == "GET":
        return render_template("registro.html")

    nombre = request.form["nombre"]
    email = request.form["email"]
    pw = request.form["pw"]

    if con_sql.usuario_existe(email):
        return render_template("registrado.html",
            msg=f"{email} ya estaba registrado")

    con_sql.insertar_usuario(nombre,email,pw)

    return render_template("registrado.html",
        msg=f"Usuario {email} registrado correctamente")

@app.route("/result", methods=["POST"])
def result():

    nombre = request.form.get("nombre")
    correo = request.form.get("email")
    pw = request.form.get("pw")
    ciudad = request.form.get("ciudad")
    estudios = request.form.get("estudios")

    if con_sql.usuario_existe(correo):
        return render_template(
            "registrado.html",
            msg=f"El usuario {correo} ya estaba registrado"
        )

    con_sql.insertar_usuario(nombre, correo, pw)

    return render_template(
        "registrado.html",
        msg=f"""
Usuario registrado correctamente:
Nombre: {nombre}
Ciudad: {ciudad}
Estudios: {estudios}
"""
    )


@app.route("/consulta")
def consulta():
    return render_template("consulta.html")


@app.route("/resultado", methods=["POST"])
def resultado():

    edad = request.form.get("edad", type=int)
    ingreso = request.form.get("ingreso", type=float)
    estudios = request.form.get("estudios")
    amort = request.form.get("amortizacion")

    creditos = con_sql.filtrar_creditos(edad, ingreso, estudios)

    if not creditos:
        return render_template("error.html", mensaje="Sin resultados")

    monto = creditos[0][4]

    cuotas = alemana(monto) if amort=="alemana" else francesa(monto)

    return render_template(
        "resultado.html",
        creditos=creditos,
        cuotas=cuotas
    )


@app.route("/creditos")
def creditos():

    data = con_sql.obtener_creditos()

    return render_template("creditos.html", creditos=data)


@app.route("/api/creditos")
def api():

    return jsonify(con_sql.obtener_creditos())


if __name__ == "__main__":
    app.run(debug=True)
