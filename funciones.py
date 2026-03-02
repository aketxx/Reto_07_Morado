def cargar_librerias_proyecto():
    """
    Importa todas las librerías necesarias para el proyecto
    de análisis y modelado de préstamos.
    """

    # =============================
    # Librerías base
    # =============================
    global np, pd, os, time
    import numpy as np
    import pandas as pd
    import os
    import time

    # =============================
    # Visualización
    # =============================
    global px, go
    import plotly.express as px
    import plotly.graph_objects as go

    # =============================
    # Model Selection & Preprocessing
    # =============================
    global train_test_split, GridSearchCV
    global StandardScaler, PCA
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA

    # =============================
    # Métricas
    # =============================
    global accuracy_score, classification_report, roc_auc_score
    global recall_score, precision_score, make_scorer
    global silhouette_score, precision_recall_curve
    global auc, roc_curve, confusion_matrix

    from sklearn.metrics import (
        accuracy_score,
        classification_report,
        roc_auc_score,
        recall_score,
        precision_score,
        make_scorer,
        silhouette_score,
        precision_recall_curve,
        auc,
        roc_curve,
        confusion_matrix
    )

    # =============================
    # Modelos
    # =============================
    global KMeans, AgglomerativeClustering
    global NearestCentroid
    global LogisticRegression
    global RandomForestClassifier, StackingClassifier, AdaBoostClassifier
    global GaussianNB, DecisionTreeClassifier
    global XGBClassifier

    from sklearn.cluster import KMeans, AgglomerativeClustering
    from sklearn.neighbors import NearestCentroid
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import (
        RandomForestClassifier,
        StackingClassifier,
        AdaBoostClassifier
    )
    from sklearn.naive_bayes import GaussianNB
    from sklearn.tree import DecisionTreeClassifier
    from xgboost import XGBClassifier

    # =============================
    # Desbalanceo
    # =============================
    global SMOTE, ImbPipeline
    from imblearn.over_sampling import SMOTE
    from imblearn.pipeline import Pipeline as ImbPipeline

    print("Todas las librerías han sido cargadas correctamente.")

def limpiar_prestamos(
    ruta_entrada="../Datos/Originales/Prestamos_Data_Alumnos_v3.xlsx",
    ruta_salida="../Datos/Limpios/información_préstamos_limpio.xlsx"
):
    """
    Limpia el dataset de préstamos aplicando filtros de calidad y consistencia.

    Parámetros:
    ----------
    ruta_entrada : str
        Ruta del archivo Excel original
    ruta_salida : str
        Ruta donde se guardará el archivo limpio

    Retorna:
    -------
    df : pandas.DataFrame
        DataFrame limpio
    """

    df = pd.read_excel(ruta_entrada)


    df = df.dropna(subset=["Prima"]).copy()


    df = df[df["Proposito"] == "Vivienda"]


    df = df[df["Prima"] != 800].copy()


    df["Meses_Maximos"] = (df["Edad"] - 16) * 12


    df_invalidos = df[df["Meses_Empleo"] > df["Meses_Maximos"]]

    df = df[df["Meses_Empleo"] <= df["Meses_Maximos"]]
    df = df.drop(columns="Meses_Maximos")


    df = df[(df["Edad"] >= 16) & (df["Edad"] <= 100)]


    df["Tipo_Jornada_Laboral"] = (
        df["Tipo_Jornada_Laboral"]
        .str.strip()
        .str.lower()
        .replace({"autonomo": "autónomo"})
    )


    df = df[df["Ingresos"] > 0]


    df = df[df["Monto_Inicial"] > 0]


    df = df[
        (df["Ratio_Deuda_Ingresos"] >= 0) &
        (df["Ratio_Deuda_Ingresos"] <= 1)
    ]

    df = df[
        (df["Ratio_Interes"] > 0) &
        (df["Ratio_Interes"] <= 100)
    ]


    condiciones_invalidas = (
        ((df["Edad"] < 19) & (df["Estudios"] == "grado")) |
        ((df["Edad"] < 20) & (df["Estudios"] == "máster")) |
        ((df["Edad"] < 25) & (df["Estudios"] == "doctorado"))
    )

    df_estudios_invalidos = df[condiciones_invalidas]


    df.to_excel(ruta_salida, index=False)

    print("Limpieza completada")
    print(f"Filas finales: {df.shape[0]}")
    print(f"Columnas finales: {df.shape[1]}")
    print(f"Registros con estudios inconsistentes: {len(df_estudios_invalidos)}")

    return df

def cargar_prestamos(ruta="../Datos/Originales/Prestamos_Data_Alumnos_v3.xlsx"):
    """
    Carga el dataset de préstamos desde un archivo Excel.

    Parámetros:
    ----------
    ruta : str
        Ruta del archivo Excel

    Retorna:
    -------
    df : pandas.DataFrame
        DataFrame con los datos cargados
    """

    df = pd.read_excel(ruta)

    print("Archivo cargado correctamente")
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")

    return df