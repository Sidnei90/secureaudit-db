def calcular_ferias(salario: float) -> float:
    """
    Cálculo das férias com adicional de 1/3 constitucional.
    :param salario: valor do salário base
    :return: valor total das férias com adicional
    """
    if salario < 0:
        raise ValueError("Salário não pode ser negativo.")
    return salario + (salario / 3)
