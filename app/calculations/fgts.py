def calcular_fgts(salario: float, meses_trabalhados: int) -> dict:
    fgts = salario * 0.08 * meses_trabalhados
    multa = fgts * 0.4
    return {"fgts": round(fgts, 2), "multa": round(multa, 2)}
