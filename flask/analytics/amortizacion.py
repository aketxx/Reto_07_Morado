def amortizacion_frances(capital, interes_anual, meses):

    i = interes_anual / 12

    cuota = capital * (i * (1 + i)**meses) / ((1 + i)**meses - 1)

    saldo = capital
    intereses_totales = 0

    for _ in range(meses):
        intereses = saldo * i
        amortizacion = cuota - intereses
        saldo -= amortizacion
        intereses_totales += intereses

    return cuota, intereses_totales


def amortizacion_aleman(capital, interes_anual, meses):

    i = interes_anual / 12

    amortizacion_constante = capital / meses
    saldo = capital
    intereses_totales = 0

    for _ in range(meses):
        intereses = saldo * i
        saldo -= amortizacion_constante
        intereses_totales += intereses

    cuota_inicial = amortizacion_constante + capital * i

    return cuota_inicial, intereses_totales