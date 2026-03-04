from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import joblib
import os
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from bbdd.con_sql import insertar_prediccion, obtener_historico, obtener_usuario, crear_usuario
from analytics.metrics import obtener_metricas
import sqlite3

app = Flask(__name__)
app.secret_key = "reto07_secret"

# ================= LOGIN =================

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth"

class Usuario(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

def obtener_usuario_por_id(user_id):
    from bbdd.con_sql import DB_PATH
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

@login_manager.user_loader
def load_user(user_id):
    user = obtener_usuario_por_id(user_id)
    if user:
        return Usuario(user[0], user[1])
    return None

# ================= MODELO =================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
modelo = joblib.load(os.path.join(BASE_DIR, "modelo", "modelo_ganador.pkl"))
threshold = joblib.load(os.path.join(BASE_DIR, "modelo", "threshold.pkl"))

def preparar_input(data_dict):
    df = pd.DataFrame([data_dict])
    df = pd.get_dummies(df)
    df = df.reindex(columns=modelo.feature_names_in_, fill_value=0)
    df = df.astype("float32")
    return df

# ================= RUTAS =================

@app.route("/")
def portada():
    return render_template("portada.html")

# 🔹 Ruta combinada Login / Registro
# ================= AUTENTICACIÓN =================

@app.route("/auth")
def auth():
    return render_template("auth.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = obtener_usuario(username)

        if user and user[2] == password:
            usuario = Usuario(user[0], user[1])
            login_user(usuario)
            return redirect(url_for("evaluacion"))

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        creado = crear_usuario(username, password)

        if creado:
            return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("portada"))

@app.route("/evaluacion")
@login_required
def evaluacion():
    return render_template("evaluacion.html")

@app.route("/evaluar", methods=["POST"])
@login_required
def evaluar():
    datos = {
        "Edad": float(request.form["edad"]),
        "Ingreso": float(request.form["ingreso"]),
        "Nivel_Estudios": request.form["estudios"],
        "Estado_Civil": request.form["estado_civil"],
        "Num_Creditos": float(request.form["num_creditos"]),
        "Tipo_Amortizacion": request.form["tipo_amortizacion"]
    }

    X = preparar_input(datos)
    proba = modelo.predict_proba(X)[:, 1][0]

    if proba < 0.30:
        nivel = "BAJO RIESGO"
        clase_css = "verde_fuerte"
    elif proba < 0.60:
        nivel = "RIESGO MEDIO"
        clase_css = "morado"
    else:
        nivel = "ALTO RIESGO"
        clase_css = "rojo"

    insertar_prediccion(datos, proba, nivel)

    return render_template(
        "resultado.html",
        probabilidad=round(proba * 100, 2),
        nivel=nivel,
        clase_css=clase_css
    )

@app.route("/historico")
@login_required
def historico():
    datos = obtener_historico()
    return render_template("historico.html", datos=datos)

@app.route("/dashboard")
@login_required
def dashboard():
    datos = obtener_metricas()
    return render_template("dashboard.html", datos=datos)

if __name__ == "__main__":
    app.run(debug=True)