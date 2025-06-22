from flask import Blueprint, render_template, request
from ..calculations.ferias import calcular_ferias
from ..calculations.decimo_terceiro import calcular_decimo_terceiro
from ..calculations.fgts import calcular_fgts
from ..calculations.horas_extras import calcular_horas_extras
from ..calculations.rescisao import calcular_rescisao
from types import SimpleNamespace

calculations = Blueprint('calculations', __name__)

@calculations.route('/ferias', methods=['GET', 'POST'])
def rota_calcular_ferias():
    resultado = None
    if request.method == 'POST':
        salario = float(request.form['salario'])
        resultado = calcular_ferias(salario)
    return render_template('calculos/ferias.html', resultado=resultado)

@calculations.route('/decimo_terceiro', methods=['GET', 'POST'])
def rota_calcular_decimo_terceiro():
    resultado = None
    if request.method == 'POST':
        salario = float(request.form['salario'])
        meses = int(request.form['meses'])
        resultado = calcular_decimo_terceiro(salario, meses)
    return render_template('calculos/decimo_terceiro.html', resultado=resultado)

@calculations.route('/fgts', methods=['GET', 'POST'])
def rota_calcular_fgts():
    resultado = None
    if request.method == 'POST':
        salario = float(request.form['salario'])
        meses = int(request.form['meses'])
        resultado = calcular_fgts(salario, meses)
    return render_template('calculos/fgts.html', resultado=resultado)

@calculations.route('/horas_extras', methods=['GET', 'POST'])
def rota_calcular_horas_extras():
    resultado = None
    if request.method == 'POST':
        salario = float(request.form['salario'])
        horas = float(request.form['horas_extras'])
        resultado = calcular_horas_extras(salario, horas)
    return render_template('calculos/horas_extras.html', resultado=resultado)

@calculations.route('/rescisao', methods=['GET', 'POST'])
def rota_calcular_rescisao():
    resultado = None
    if request.method == 'POST':
        salario = float(request.form['salario'])
        dias = int(request.form['dias_trabalhados'])
        meses = int(request.form['meses_trabalhados'])
        ferias_vencidas = "ferias_vencidas" in request.form
        saldo_fgts = float(request.form['saldo_fgts'])

        resultado_dict = calcular_rescisao(salario, dias, meses, ferias_vencidas, saldo_fgts)
        resultado = SimpleNamespace(**resultado_dict)
        
    return render_template('calculos/rescisao.html', resultado=resultado)