import sqlite3 as sqlite

BBDD = "creditos.db"


def crear_tablas():

    con = sqlite.connect(BBDD)
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        nombre TEXT NOT NULL,
        email TEXT PRIMARY KEY,
        pw TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS creditos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        edad INTEGER,
        ingreso REAL,
        estudios TEXT,
        monto REAL
    )
    """)

    con.commit()
    con.close()

def usuario_existe(email):

    con = sqlite.connect(BBDD)
    cur = con.cursor()

    cur.execute("SELECT email FROM usuarios WHERE email=?", (email,))
    res = cur.fetchone()

    con.close()

    return res is not None


def insertar_usuario(nombre, email, pw):

    con = sqlite.connect(BBDD)
    cur = con.cursor()

    cur.execute(
        "INSERT INTO usuarios VALUES (?,?,?)",
        (nombre, email, pw)
    )

    con.commit()
    con.close()


def obtener_creditos():

    con = sqlite.connect(BBDD)
    cur = con.cursor()

    cur.execute("SELECT * FROM creditos")
    data = cur.fetchall()

    con.close()

    return data


def filtrar_creditos(edad, ingreso, estudios):

    con = sqlite.connect(BBDD)
    cur = con.cursor()

    cur.execute("""
    SELECT * FROM creditos
    WHERE edad>=? AND ingreso>=? AND estudios=?
    """, (edad, ingreso, estudios))

    data = cur.fetchall()
    con.close()

    return data
