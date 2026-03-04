def calcular_metricas(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    y_true_arr = np.array(y_true)
    y_pred_arr = np.array(y_pred)

    # Evita división por 0 por seguridad
    eps = 1e-8
    mape = np.mean(np.abs((y_true_arr - y_pred_arr) / np.maximum(np.abs(y_true_arr), eps))) * 100

    return rmse, mae, r2, mape