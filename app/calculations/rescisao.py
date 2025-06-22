from app.calculations.ferias import calcular_ferias
from app.calculations.decimo_terceiro import calcular_decimo_terceiro

def calcular_rescisao(
    salario: float,
    dias_trabalhados_no_mes: int,
    meses_trabalhados: int,
    ferias_vencidas: bool,
    saldo_fgts: float
) -> dict:
    """
    Retorna um dicionário com todos os valores da rescisão.
    """
    saldo_salario = (salario / 30) * dias_trabalhados_no_mes
    aviso_previo = salario  # simplificado, 30 dias
    ferias_vencidas_valor = calcular_ferias(salario) if ferias_vencidas else 0
    ferias_proporcionais = ((salario / 12) * meses_trabalhados) + (((salario / 12) * meses_trabalhados) / 3)
    decimo_terceiro = calcular_decimo_terceiro(salario, meses_trabalhados)
    multa_fgts = saldo_fgts * 0.4

    total = saldo_salario + aviso_previo + ferias_vencidas_valor + ferias_proporcionais + decimo_terceiro + multa_fgts

    return {
        "saldo_salario": round(saldo_salario, 2),
        "aviso_previo": round(aviso_previo, 2),
        "ferias_vencidas": round(ferias_vencidas_valor, 2),
        "ferias_proporcionais": round(ferias_proporcionais, 2),
        "decimo_terceiro": round(decimo_terceiro, 2),
        "multa_fgts": round(multa_fgts, 2),
        "total": round(total, 2)
    }
