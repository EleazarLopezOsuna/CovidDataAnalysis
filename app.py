#python -m flask run --reload --debugger
from flask import Flask, redirect, url_for, render_template, request
from datetime import date

app = Flask(__name__)

columnas = ['Columna1', 'Columna2', 'Columna3']

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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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
        columns = columnas
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