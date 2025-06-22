def calcular_horas_extras(salario: float, horas_extras: float) -> float:
    valor_hora = salario / 220
    adicional = valor_hora * 0.5  # 50% adicional (hora extra comum)
    return (valor_hora + adicional) * horas_extras
