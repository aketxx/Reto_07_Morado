 # Reto 07 - Sistema de Evaluación de Riesgo de Créditos

Proyecto de análisis de datos y machine learning para evaluar el **riesgo de impago de préstamos**, junto con una aplicación web desarrollada con **Flask** que permite analizar clientes, visualizar información financiera y predecir el riesgo de crédito.

# Estructura del Proyecto

```
Reto_07_Morado
│
───Code
│   │   Analisis_amortizaciones.ipynb
│   │   Clusters.ipynb
│   │   matematicas.ipynb
│   │   objetivo3_final.ipynb
│   │   Visualizacion.ipynb
│   │
│   ├───graficos
│   └───Graficos_Informe
│           10_var_pre_impago.png
│           comparacion_intereses.png
│           distribucion_cliente_segmento.png
│           distribucion_monto_inicial.png
│           importancia_variables.png
│           k_clusters_optimo.png
│           MC_mejor-modelo.png
│           output.png
│           real_vs_predicho_xgboost.png
│           Visualización_3D_Clusters.png
│
├───config_files
├───Datos
│   ├───Limpios
│   │       información_préstamos_limpio.xlsx
│   │
│   ├───Originales
│   │       Prestamos_Data_Alumnos_v3.xlsx
│   │
│   └───Transformados
└───flask
    │   server.py
    │
    ├───analytics
    │   │   amortizacion.py
    │   │   metrics.py
    │   │
    │   └───__pycache__
    │           amortizacion.cpython-312.pyc
    │           metrics.cpython-312.pyc
    │
    ├───bbdd
    │   │   con_sql.py
    │   │   creditos.db
    │   │
    │   └───__pycache__
    │           con_sql.cpython-312.pyc
    │
    ├───modelo
    │       modelo_ganador.pkl
    │       threshold.pkl
    │
    ├───static
    │   │   estilos.css
    │   │
    │   └───img
    │           lagun_aro.png
    │
    └───templates
            amortizacion.html
            auth.html
            dashboard.html
            evaluacion.html
            historico.html
            index.html
            layout.html
            login.html
            portada.html
            register.html
            resultado.html
            resultado_amortizacion.html
```



# Descripción del Proyecto

El objetivo del proyecto es analizar datos de préstamos para:

- Identificar **factores de riesgo de impago**
- Construir un **modelo de predicción**
- Visualizar información relevante
- Crear una **aplicación web interactiva** para consultar y evaluar créditos

# Análisis de Datos

Los notebooks incluidos en la carpeta `Code` contienen:

- **Análisis exploratorio de datos**
- **Limpieza y preparación del dataset**
- **Estudio de amortizaciones**
- **Visualizaciones y gráficos**
- **Entrenamiento del modelo predictivo**


# Modelo de Machine Learning

El modelo entrenado permite **predecir la probabilidad de impago de un préstamo**.

Archivos principales:
flask/modelo/modelo_ganador.pkl
flask/modelo/threshold.pkl


El modelo se utiliza dentro de la aplicación web para evaluar nuevos créditos.


 # Aplicación Web

La aplicación web está desarrollada con **Flask** y permite:
- Registro y login de usuarios
- Evaluación de riesgo de crédito
- Visualización de métricas
- Simulación de amortización
- Consulta de historial de créditos

Archivo principal:

```
flask/server.py
```

## Ejecutar la aplicación

```bash
cd flask
python server.py
```
La web se abrirá en:

http://127.0.0.1:5000
