#python -m flask run --reload --debugger
import os
from flask import Flask, redirect, url_for, render_template, request
from datetime import date
from flask.helpers import make_response
import pandas as pd
from dataAnalysis.fifthItem import fifthItem
from dataAnalysis.firstItem import firstItem
from dataAnalysis.seventhItem import seventhItem
from dataAnalysis.ninthItem import ninthItem
from dataAnalysis.fifteenthItem import fifteenthItem
from dataAnalysis.secondItem import secondItem
from dataAnalysis.fourthItem import fourthItem
from dataAnalysis.twentyFifthItem import twentyFifthItem
from dataAnalysis.twentyFirstItem import twentyFirstItem
from dataAnalysis.eighthItem import eighthItem
from dataAnalysis.nineteenthItem import nineteenthItem
from dataAnalysis.thirdItem import thirdItem
from dataAnalysis.twentyThirdItem import twentyThirdItem
from dataAnalysis.twentyFourthItem import twentyFourthItem
from dataAnalysis.twentySecondItem import twentySecondItem
from dataAnalysis.twentiethItem import twentiethItem
from dataAnalysis.seventeenthItem import seventeenthItem
from dataAnalysis.sixteenthItem import sixteenthItem
from dataAnalysis.fourteenthItem import fourteenthItem
from dataAnalysis.eleventhItem import eleventhItem
from dataAnalysis.thirteenthItem import thirteenthItem
from dataAnalysis.sixthItem import sixthItem
from dataAnalysis.tenthItem import tenthItem
from dataAnalysis.twelfthItem import twelfthItem
from dataAnalysis.eighteenthItem import eighteenthItem

app = Flask(__name__)

headers = []
data = []
resultados = {}

tendencias = {
    "Infección por Covid-19 en un País": "trendsCovidPerCountry",
    "Número de infectados por día de un País": "trendsDailyInfectedPerCountry",
    "Vacunación de en un País": "trendsVaccinatedPerCountry",
    "Casos confirmados de Coronavirus en un departamento de un País": "trendsConfirmedPerState"
}

@app.route("/trends/vaccinatedPerCountry")
def trendsVaccinatedPerCountry():
    return render_template('/trends/vaccinatedPerCountry.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/trends/dailyInfectedPerCountry")
def trendsDailyInfectedPerCountry():
    return render_template('/trends/dailyInfectedPerCountry.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/trends/covidPerCountry")
def trendsCovidPerCountry():
    return render_template('/trends/covidPerCountry.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/trends/confirmedPerState")
def trendsConfirmedPerState():
    return render_template('/trends/confirmedPerState.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

tasas = {
    "Comportamiento de casos activos conforme al número de muertes por continente": "ratesCasosActivosMuertesContinente",
    "Mortalidad por coronavirus (COVID-19) en un país": "ratesMortalidadPais",
    "Crecimiento de casos en relación con nuevos casos diarios y tasa de muerte": "ratesCrecimientoCasosNuevosTasaMuerte"
}

@app.route("/rates/casosActivosMuertesContinente")
def ratesCasosActivosMuertesContinente():
    return render_template('/rates/casosActivosMuertesContinente.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/rates/mortalidadPais")
def ratesMortalidadPais():
    return render_template('/rates/mortalidadPais.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/rates/crecimientoCasosNuevosTasaMuerte")
def ratesCrecimientoCasosNuevosTasaMuerte():
    return render_template('/rates/crecimientoCasosNuevosTasaMuerte.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

predicciones = {
    "Infertados en un País": "predictionInfectadosPais",
    "Mortalidad por COVID en un Departamento": "predictionMortalidadDepartamento",
    "Mortalidad por COVID en un País": "predictionMortalidadPais",
    "Casos de un país para un año": "predictionCasosPaisYear",
    "Muertes en el último día del primer año de infecciones en un país": "predictionMuertesUltimoDiaPrimerYearPais",
    "Casos confirmados por día": "predictionCasosConfirmadosDia",
    "Casos y muertes en todo el mundo": "predictionCasosMuertesGlobal"
}

@app.route("/predictions/infectadosPais")
def predictionInfectadosPais():
    return render_template('/predictions/infectadosPais.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/predictions/mortalidadDepartamento")
def predictionMortalidadDepartamento():
    return render_template('/predictions/mortalidadDepartamento.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/predictions/mortalidadPais")
def predictionMortalidadPais():
    return render_template('/predictions/mortalidadPais.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/predictions/casosPaisYear")
def predictionCasosPaisYear():
    return render_template('/predictions/casosPaisYear.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/predictions/muertesUltimoDiaPrimerYearPais")
def predictionMuertesUltimoDiaPrimerYearPais():
    return render_template('/predictions/muertesUltimoDiaPrimerYearPais.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/predictions/casosConfirmadosDia")
def predictionCasosConfirmadosDia():
    return render_template('/predictions/casosConfirmadosDia.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/predictions/casosMuertesGlobal")
def predictionCasosMuertesGlobal():
    return render_template('/predictions/casosMuertesGlobal.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

analisis = {
    "Número de muertes por coronavirus en un País": "analysisNumeroMuertesPais",
    "Comparativo de Vacunaciópn entre 2 paises": "analysisComparacionVacunacionPaises",
    "Comparativo entres 2 o más paises o continentes": "analysisComparacionPaisesContinentes"
}

@app.route("/analysis/numeroMuertesPais")
def analysisNumeroMuertesPais():
    return render_template('/analysis/numeroMuertesPais.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/analysis/comparacionVacunacionPaises")
def analysisComparacionVacunacionPaises():
    return render_template('/analysis/comparacionVacunacionPaises.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/analysis/comparacionPaisesContinentes")
def analysisComparacionPaisesContinentes():
    return render_template('/analysis/comparacionPaisesContinentes.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

porcentajes = {
    "Hombres infectados por covid-19 en un País desde el primer caso activo": "porcentagesHombresInfectadosPais",
    "Muertes frente al total de casos en un país, región o continente": "porcentagesMuertesCasosPaisRegionContinente"
}

@app.route("/percentages/hombresInfectadosPais")
def porcentagesHombresInfectadosPais():
    return render_template('/percentages/hombresInfectadosPais.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/percentages/muertesCasosPaisRegionContinente")
def porcentagesMuertesCasosPaisRegionContinente():
    return render_template('/percentages/muertesCasosPaisRegionContinente.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

muertes = {
    "Muertes promedio por casos confirmados y edad de covid 19 en un País": "deathsPromedioCasosEdad",
    "Muertes según regiones de un país - Covid 19": "deathsRegionPais"
}

@app.route("/deaths/promedioCasosEdad")
def deathsPromedioCasosEdad():
    return render_template('/deaths/promedioCasosEdad.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/deaths/regionPais")
def deathsRegionPais():
    return render_template('/deaths/regionPais.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

otros = {
    "Indice de Progresión de la pandemia": "othersIndiceProgresionPandemia",
    "Comportamiento y clasificación de personas infectadas por COVID-19 por municipio en un País": "othersComportamientoClasificacionInfectadosMunicipioPais",
    "Factores de muerte por COVID-19 en un país": "othersFactoresMuertesPais",
    "Comparación entre el número de casos detectados y el número de pruebas de un país": "othersComparacionCasosDetectadosNumeroPruebas",
}

@app.route("/others/indiceProgresionPandemia")
def othersIndiceProgresionPandemia():
    return render_template('/others/indiceProgresionPandemia.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/others/comportamientoClasificacionInfectadosMunicipioPais")
def othersComportamientoClasificacionInfectadosMunicipioPais():
    return render_template('/others/comportamientoClasificacionInfectadosMunicipioPais.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/others/factoresMuertesPais")
def othersFactoresMuertesPais():
    return render_template('/others/factoresMuertesPais.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/others/comparacionCasosDetectadosNumeroPruebas")
def othersComparacionCasosDetectadosNumeroPruebas():
    return render_template('/others/comparacionCasosDetectadosNumeroPruebas.html', 
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        columns = headers
    )

@app.route("/")
def home():
    return render_template(
        'index.html',
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d")
    )

@app.route("/preLoadDataCSV", methods=['GET', 'POST'])
def preLoadDataCSV():
    if request.method == 'POST':
        global data
        data = pd.read_csv('preload.csv')
        headers.clear()
        for col_name in data.columns: 
            headers.append(col_name)
    return render_template(
        'index.html',
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d")
    )

@app.route("/preLoadDataXLS", methods=['GET', 'POST'])
def preLoadDataXLS():
    if request.method == 'POST':
        global data
        data = pd.read_excel('preload.xlsx')
        headers.clear()
        for col_name in data.columns: 
            headers.append(col_name)
    return render_template(
        'index.html',
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d")
    )

@app.route("/preLoadDataJSON", methods=['GET', 'POST'])
def preLoadDataJSON():
    if request.method == 'POST':
        global data
        data = pd.read_json('preload.json')
        headers.clear()
        for col_name in data.columns: 
            headers.append(col_name)
    return render_template(
        'index.html',
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d")
    )

@app.route("/loadData", methods=['GET', 'POST'])
def loadData():
    global data
    if request.method == 'POST':
        file = request.files['upload']
        file_ext = os.path.splitext(file.filename)[1]
        if (file_ext == '.csv'):
            data = pd.read_csv(file)
            headers.clear()
            for col_name in data.columns: 
                headers.append(col_name)
        elif (file_ext == '.json'):
            data = pd.read_json(file)
            headers.clear()
            for col_name in data.columns: 
                headers.append(col_name)
        elif (file_ext in ['.xls', '.xlsx']):
            data = pd.read_excel(file)
            headers.clear()
            for col_name in data.columns: 
                headers.append(col_name)
    return render_template(
        'index.html',
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d")
    )

@app.route("/firstItemAnalysis", methods=['GET', 'POST'])
def firstItemAnalysis():
    global data
    analysis1 = firstItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaInfectados'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/seventhItemAnalysis", methods=['GET', 'POST'])
def seventhItemAnalysis():
    global data
    analysis1 = seventhItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaInfectados'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/ninthItemAnalysis", methods=['GET', 'POST'])
def ninthItemAnalysis():
    global data
    analysis1 = ninthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaVacunados'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/fifteenthItemAnalysis", methods=['GET', 'POST'])
def fifteenthItemAnalysis():
    global data
    analysis1 = fifteenthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaDepartamento'],
        request.form['nombreDepartamento'],
        request.form['columnaCasos'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/secondItemAnalysis", methods=['GET', 'POST'])
def secondItemAnalysis():
    global data
    analysis1 = secondItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaInfectados'],
        request.form['columnaDias'],
        request.form['inputPrediccion'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/fourthItemAnalysis", methods=['GET', 'POST'])
def fourthItemAnalysis():
    global data
    analysis1 = fourthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaDepartamento'],
        request.form['nombreDepartamento'],
        request.form['columnaMuertos'],
        request.form['columnaDias'],
        request.form['inputPrediccion'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/fifthItemAnalysis", methods=['GET', 'POST'])
def fifthItemAnalysis():
    global data
    analysis1 = fifthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaMuertos'],
        request.form['columnaDias'],
        request.form['inputPrediccion'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/twentyFifthItemAnalysis", methods=['GET', 'POST'])
def twentyFifthItemAnalysis():
    global data
    analysis1 = twentyFifthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaInfectados'],
        request.form['columnaDias'],
        request.form['inputPrediccion'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/twentyFirstItemAnalysis", methods=['GET', 'POST'])
def twentyFirstItemAnalysis():
    global data
    analysis1 = twentyFirstItem(
        request.form['columnaInfectados'],
        request.form['columnaMuertes'],
        request.form['columnaDias'],
        request.form['inputPrediccion'],
        data
    )
    resultados = analysis1.analysis1()
    resultados2 = analysis1.analysis2()
    res = render_template(
        'dualReport.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados,
        analysisResult2 = resultados2
    )
    return res

@app.route("/eighthItemAnalysis", methods=['GET', 'POST'])
def eighthItemAnalysis():
    global data
    analysis1 = eighthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaInfectados'],
        request.form['columnaDias'],
        request.form['inputYear'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/nineteenthItemAnalysis", methods=['GET', 'POST'])
def nineteenthItemAnalysis():
    global data
    analysis1 = nineteenthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaMuertes'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/thirdItemAnalysis", methods=['GET', 'POST'])
def thirdItemAnalysis():
    global data
    analysis1 = thirdItem(
        request.form['columnaInfectados'],
        request.form['columnaDias'],
        data
    )
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/twentyThirdItemAnalysis", methods=['GET', 'POST'])
def twentyThirdItemAnalysis():
    global data
    analysis1 = twentyThirdItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaFactor'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/twentyFourthItemAnalysis", methods=['GET', 'POST'])
def twentyFourthItemAnalysis():
    global data
    analysis1 = twentyFourthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaInfectados'],
        request.form['columnaPruebas'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis1()
    resultados2 = analysis1.analysis2()
    res = render_template(
        'dualReport.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados,
        analysisResult2 = resultados2
    )
    return res

@app.route("/twentySecondItemAnalysis", methods=['GET', 'POST'])
def twentySecondItemAnalysis():
    global data
    analysis1 = twentySecondItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaInfectados'],
        request.form['columnaMuertes'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/twentiethItemAnalysis", methods=['GET', 'POST'])
def twentiethItemAnalysis():
    global data
    analysis1 = twentiethItem(
        request.form['columnaInfectadosDiarios'],
        request.form['columnaInfectadosAcumulados'],
        request.form['columnaMuertes'],
        request.form['columnaDias'],
        data
    )
    resultados = analysis1.analysis1()
    resultados2 = analysis1.analysis2()
    res = render_template(
        'dualReport.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados,
        analysisResult2 = resultados2
    )
    return res

@app.route("/seventeenthItemAnalysis", methods=['GET', 'POST'])
def seventeenthItemAnalysis():
    global data
    analysis1 = seventeenthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaInfectados'],
        request.form['columnaMuertes'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/sixteenthItemAnalysis", methods=['GET', 'POST'])
def sixteenthItemAnalysis():
    global data
    analysis1 = sixteenthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaRegion'],
        request.form['nombreRegion'],
        request.form['columnaInfectados'],
        request.form['columnaMuertes'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/fourteenthItemAnalysis", methods=['GET', 'POST'])
def fourteenthItemAnalysis():
    global data
    analysis1 = fourteenthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaRegion'],
        request.form['nombreRegion'],
        request.form['columnaMuertes'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/eleventhItemAnalysis", methods=['GET', 'POST'])
def eleventhItemAnalysis():
    global data
    analysis1 = eleventhItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaGenero'],
        request.form['columnaInfectados'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/thirteenthItemAnalysis", methods=['GET', 'POST'])
def thirteenthItemAnalysis():
    global data
    analysis1 = thirteenthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaEdad'],
        request.form['columnaCasos'],
        request.form['columnaMuertes'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis1()
    resultados2 = analysis1.analysis2()
    res = render_template(
        'dualReport.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados,
        analysisResult2 = resultados2
    )
    return res

@app.route("/sixthItemAnalysis", methods=['GET', 'POST'])
def sixthItemAnalysis():
    global data
    analysis1 = sixthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaMuertos'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis()
    res = render_template(
        'report.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados
    )
    return res

@app.route("/tenthItemAnalysis", methods=['GET', 'POST'])
def tenthItemAnalysis():
    global data
    analysis1 = tenthItem(
        request.form['columnaPais'],
        request.form['nombrePais1'],
        request.form['nombrePais2'],
        request.form['columnaVacunados'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis1()
    resultados2 = analysis1.analysis2()
    res = render_template(
        'dualReport.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados,
        analysisResult2 = resultados2
    )
    return res

@app.route("/twelfthItemAnalysis", methods=['GET', 'POST'])
def twelfthItemAnalysis():
    global data
    analysis1 = twelfthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente1'],
        request.form['nombreContinente2'],
        request.form['columnaPais'],
        request.form['nombrePais1'],
        request.form['nombrePais2'],
        request.form['columnaMuertes'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis1()
    resultados2 = analysis1.analysis2()
    res = render_template(
        'dualReport.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados,
        analysisResult2 = resultados2
    )
    return res

@app.route("/eighteenthItemAnalysis", methods=['GET', 'POST'])
def eighteenthItemAnalysis():
    global data
    analysis1 = eighteenthItem(
        request.form['columnaContinente'],
        request.form['nombreContinente'],
        request.form['columnaPais'],
        request.form['nombrePais'],
        request.form['columnaDepartamento'],
        request.form['nombreDepartamento'],
        request.form['columnaMunicipio'],
        request.form['nombreMunicipio'],
        request.form['columnaComportamiento'],
        request.form['columnaClasificacion'],
        request.form['columnaInfectados'],
        request.form['columnaDias'],
        data
    )
    analysis1.dataFilter()
    resultados = analysis1.analysis1()
    resultados2 = analysis1.analysis2()
    res = render_template(
        'dualReport.html',
        results = resultados,
        analysis = analisis,
        deaths = muertes,
        others = otros,
        percentages = porcentajes,
        predictions = predicciones,
        rates = tasas,
        trends = tendencias,
        today = date.today().strftime("%Y-%m-%d"),
        analysisResult = resultados,
        analysisResult2 = resultados2
    )
    return res

if __name__ == "__main__":
    app.run()