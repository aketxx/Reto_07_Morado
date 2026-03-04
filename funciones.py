import os
import pandas as pd
import sys

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
    global calinski_harabasz_score, davies_bouldin_score, silhouette_samples

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
        confusion_matrix,
        calinski_harabasz_score,
        davies_bouldin_score,
        silhouette_samples
    )

    # =============================
    # Modelos de clustering
    # =============================
    global KMeans, AgglomerativeClustering, DBSCAN

    from sklearn.cluster import (
        KMeans,
        AgglomerativeClustering,
        DBSCAN
    )

    # =============================
    # Modelos de clasificación
    # =============================
    global NearestCentroid
    global LogisticRegression
    global RandomForestClassifier, StackingClassifier, AdaBoostClassifier
    global GaussianNB, DecisionTreeClassifier
    global XGBClassifier

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

# 1. CARGAR DATOS
def cargar_y_preparar_datos(ruta_archivo):
    df = pd.read_excel(ruta_archivo)
    # Filtrar solo vivienda y copiar para evitar warnings
    df_viv = df[df['Proposito'].astype(str)
                .str.contains('Vivienda', case=False, na=False)].copy()
    # Label
    df_viv['Impago_Label'] = df_viv['Impago'].map({0:0, 1:1})
    return df_viv

# Ajusta esta ruta si es necesario
ruta_real = os.path.join('..', 'Datos', 'Limpios', 'información_préstamos_limpio.xlsx')

if os.path.exists(ruta_real):
    df = cargar_y_preparar_datos(ruta_real)
else:
    print(f" ATENCIÓN: No se encuentra el archivo en {ruta_real}")
    df = pd.DataFrame()