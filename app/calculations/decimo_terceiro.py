def calcular_decimo_terceiro(salario: float, meses_trabalhados: int) -> float:
    """
    Calcula o 13º salário proporcional.
    """
    if meses_trabalhados > 12:
        meses_trabalhados = 12
    return (salario / 12) * meses_trabalhados
