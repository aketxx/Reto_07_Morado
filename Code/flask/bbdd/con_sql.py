import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "creditos.db")

def crear_tablas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predicciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            edad REAL,
            ingreso REAL,
            estudios TEXT,
            estado_civil TEXT,
            num_creditos REAL,
            tipo_amortizacion TEXT,
            probabilidad REAL,
            nivel TEXT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

# INSERTAR PREDICCIÓN

def insertar_prediccion(datos, probabilidad, nivel):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predicciones (
            edad,
            ingreso,
            estudios,
            estado_civil,
            num_creditos,
            tipo_amortizacion,
            probabilidad,
            nivel
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        datos["Edad"],
        datos["Ingreso"],
        datos["Nivel_Estudios"],
        datos["Estado_Civil"],
        datos["Num_Creditos"],
        datos["Tipo_Amortizacion"],
        probabilidad,
        nivel
    ))

    conn.commit()
    conn.close()

# OBTENER HISTORIAL

def obtener_historico():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM predicciones
        ORDER BY fecha DESC
    """)

    datos = cursor.fetchall()
    conn.close()
    return datos

crear_tablas()

# =====================================================
# TABLA USUARIOS
# =====================================================

def crear_tabla_usuarios():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    # Crear usuario admin por defecto si no existe
    cursor.execute("SELECT * FROM usuarios WHERE username = ?", ("admin",))
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO usuarios (username, password) VALUES (?, ?)",
            ("admin", "admin123")
        )

    conn.commit()
    conn.close()

def obtener_usuario(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
    user = cursor.fetchone()

    conn.close()
    return user

crear_tabla_usuarios()

def crear_usuario(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO usuarios (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False