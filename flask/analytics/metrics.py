from bbdd.con_sql import obtener_historico
import pandas as pd

def obtener_metricas():
    datos = obtener_historico()

    if not datos:
        return {
            "total": 0,
            "media": 0,
            "niveles": []
        }

    columnas = [
        "id",
        "edad",
        "ingreso",
        "estudios",
        "estado_civil",
        "num_creditos",
        "probabilidad",
        "nivel",
        "fecha"
    ]

    df = pd.DataFrame(datos, columns=columnas)

    # total evaluaciones
    total = len(df)

    # probabilidad media
    media = round(df["probabilidad"].mean() * 100, 2)

    # distribución por nivel
    niveles = (
        df.groupby("nivel")
        .size()
        .reset_index(name="count")
        .values
        .tolist()
    )

    return {
        "total": total,
        "media": media,
        "niveles": niveles
    }