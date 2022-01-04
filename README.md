#Covid Data Analysis with Machine Learning using Python3 as backend
## User and Technical Manual
* [User Manual](#User-Manual)
* [Technical Manual](#Technical-Manual)

## User Manual <a name="User-Manual"></a>
First thing first, we need to upload a file with all the data.
We can select files within our disk and then click on "Load File" button or use the preload file corresponding to (owid-covid-data) with date 1/3/2022.
##### Data Load Page
![DataLoadPage](https://drive.google.com/uc?export=view&id=1qpabskfs7rg8M3jO0sN0VG43esLqdJsp)
In the navigation bar there are 7 distincts types of analysis and within them the options increase, below there is a list with all the analysis that we can do.
1. Analysis
1.1 Número de muertes por coronavirus en un País
1.2 Comparativo de Vacunaciópn entre 2 paises
1.3 Comparativo entres 2 o más paises o continentes
2. Deaths
2.1 Muertes promedio por casos confirmados y edad de covid 19 en un País
2.2 Muertes según regiones de un país - Covid 19
3. Others
3.1 Indice de Progresión de la pandemia
3.2 Comportamiento y clasificación de personas infectadas por COVID-19 por municipio en un País
3.3 Factores de muerte por COVID-19 en un país
3.4 Comparación entre el número de casos detectados y el número de pruebas de un país
4. Percentages
4.1 Hombres infectados por covid-19 en un País desde el primer caso activo
4.2 Muertes frente al total de casos en un país, región o continente
5. Predictions
5.1 Infertados en un País
5.2 Mortalidad por COVID en un Departamento
5.3 Mortalidad por COVID en un País
5.4 Casos de un país para un año
5.5 Muertes en el último día del primer año de infecciones en un país
5.6 Casos confirmados por día
5.7 Casos y muertes en todo el mundo
6. Rates
6.1 Comportamiento de casos activos conforme al número de muertes por continente
6.2 Mortalidad por coronavirus (COVID-19) en un país
6.3 Crecimiento de casos en relación con nuevos casos diarios y tasa de muerte
7. Trends
7.1 Infección por Covid-19 en un País
7.2 Número de infectados por día de un País
7.3 Vacunación de en un País
7.4 Casos confirmados de Coronavirus en un departamento de un País

Once all the data is loaded we can select one of the options and we must set the required parameters for the analysis.

##### Setting parameters examples
![ParameterExample1](https://drive.google.com/uc?export=view&id=17ZD86stUizNtSbkOmWr1iwza_NtxPFiL)
![ParameterExample2](https://drive.google.com/uc?export=view&id=1MP8UA9aI1lh7xd8Mi2hUSfWFzZopGU5c)

When all paremeters are loaded we must click on "Calcular" and the analysis process will start.
After a short period of wait, a new page will load, the result page, in which we could get 2 different results
1. Simple analysis: This type of analysis will draw only 1 graph and give results about 1 variable alone
![SimpleAnalysisResult](https://drive.google.com/uc?export=view&id=1ISg0xS0li6nSHfewO3hogcK11yKa7esz)

2. Dual analysis: This type of analysis will draw 2 graphs and give results for 2 variables. In addition will have a little conclusion about the analysis of both variables.
![DualAnalysisResult1](https://drive.google.com/uc?export=view&id=1E56FJHnToWpB2mU0VM0HEFIHRoUFdmnT)
![DualAnalysisResult2](https://drive.google.com/uc?export=view&id=19uEMxFeUXHtUB_nw64rXk7iLJw6YBVyO)

In both cases will have the "Guardar como PDF" button at the end. When clicked the report will automatically be downloaded into your computer with a little bit more of information.
![SimpleAnalysisReport](https://drive.google.com/uc?export=view&id=1S7r8aKgBd3YG4XpwfSno9nrdL_KY4TkP)
![DualAnalysisReport](https://drive.google.com/uc?export=view&id=1I4dchxwp6oiPePvJaFIchc0SUpTo3VUe)

For data integrity we must reload our files before do another analysis.

##### Analysis options requirements
1. Tendencia de la infección por Covid-19 en un País
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais
        * Nombre
    * Nuevos infectados

2. Predicción de Infertados en un País
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais
        * Nombre
    * Dia a predecir
    * Infectados acumulados

3. Indice de Progresión de la pandemia
    * Dia
    * Infectados totales

4. Predicción de mortalidad por COVID en un Departamento
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais [opcional]
        * Nombre [opcional]
    * Departamento
        * Nombre
    * Dia a predecir
    * Muertos

5. Predicción de mortalidad por COVID en un País
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais
        * Nombre
    * Dia a predecir
    * Muertos acumulados

6. Análisis del número de muertes por coronavirus en un País
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais
        * Nombre
    * Muertos acumulados

7. Tendencia del número de infectados por día de un País
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais?
        * Nombre
    * Nuevos infectados

8. Predicción de casos de un país para un año
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais
        * Nombre
    * Año a predecir
    * Infectados totales

9. Tendencia de la vacunación de en un País
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais
        * Nombre
    * Nuevos vacunados

10. Analisis Comparativo de Vacunacion entre 2 paises
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais
        * Nombre
    * Pais
        * Nombre
    * Nuevos vacunados

11. Porcentaje de hombres infectados por covid 19 en un País desde el primer caso activo
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais
        * Nombre
    * Nuevos infectados
    * Genero

12. Analisis Comparativo entres 2 paises o continentes
    * Dia
    * Continente
        * Continente 1 y Continente 2
    * Pais
        * Pais 1 y Pais 2
    * Muertes acumuladas

13. Muertes promedio por casos confirmados y edad de covid 19 en un País
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais
        * Nombre
    * Edad
    * Casos nuevos

14. Muertes según regiones de un país  Covid 19
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais [opcional]
        * Nombre [opcional]
    * Region
        * Nombre
    * Dia a predecir
    * Muertes

15. Tendencia de casos confirmados de Coronavirus en un departamento de un País
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais [opcional]
        * Nombre [opcional]
    * Departamento
        * Nombre
    * Casos confirmados

16. Porcentaje de muertes frente al total de casos en un país, región o continente
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais [opcional]
        * Nombre [opcional]
    * Region [opcional]
        * Nombre [opcional]
    * Dia a predecir
    * Infectados acumulados
    * Muertes acumuladas

17. Tasa de comportamiento de casos activos en relación al número de muertes en un continente
    * Dia
    * Continente
        * Nombre
    * Dia a predecir
    * Casos activos
    * Muertes acumuladas

18. Comportamiento y clasificación de personas infectadas por COVID-19 por municipio en un País
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais [opcional]
        * Nombre [opcional]
    * Departamento [opcional]
        * Nombre [opcional]
    * Municipio
        * Nombre
    * Infectados
    * Comportamiento
    * Clasificacion
    * Dia a predecir

19. Predicción de muertes en el último día del primer año de infecciones en un país
    * Dia
    * Continente [opcional]
        * Nombre [opcional]
    * Pais
        * Nombre
    * Muertes
    * Dia a predecir (31/dic/2020)

20. Tasa de crecimiento de casos de COVID-19 en relación con nuevos casos diarios y tasa de muerte por COVID-19
    * Dia
    * Infectados totales
    * Infectados diarios
    * Muertes totales
    * Dia a predecir

21. Predicciones de casos y muertes en todo el mundo
    * Dia
    * Infectados totales
    * Muertos totales
    * Dia a predecir

22. Tasa de mortalidad por coronavirus (COVID-19) en un país
    * Continente [opcional]
        * Nombre [opcional]
    * Pais
        * Nombre
    * Dia
    * Infectados totales
    * Muertos totales
    * Dia a predecir

23. Factores de muerte por COVID-19 en un país
    * Continente [opcional]
        * Nombre [opcional]
    * Pais
        * Nombre
    * Dia
    * Factor de muerte
    * Muertos totales
    * Dia a predecir

24. Comparación entre el número de casos detectados y el número de pruebas de un país
    * Continente [opcional]
        * Nombre [opcional]
    * Pais
        * Nombre
    * Dia
    * Infectados totales
    * Pruebas totales

25. Predicción de casos confirmados por día
    * Continente
        * Nombre
    * Pais
        * Nombre
    * Dia
    * Infectados diarios
    * Dia a predecir

## Technical Manual <a name="Technical-Manual"></a>
This project is using python3 as backend, and libraries such as
* click
* colorama
* cycler
* datetime
* Flask
* fonttools
* gunicorn
* itsdangerous
* Jinja2
* joblib
* json
* kiwisolver
* MarkupSafe
* math
* matplotlib
* numpy
* packaging
* pandas
* Pillow
* pyparsing
* python-dateutil
* pytz
* scikit-learn
* scipy
* six
* sklearn
* threadpoolctl
* Werkzeug
* wkhtmltopdf

For the analysis of data scikit-learn comes in handy and modules suck as 
* linear_model
* metrics
    * mean_squared_error
    * r2_score

##### PYTHON item structure
Within the files there is a class that represents each item for the basics analysis, those who generates 1 graph, the class has methods such as
* \_\_init\_\_: for example will ask for the next parameters such as:
    1. continentColumn
    2. continentName
    3. countryColumn
    4. countryName
    5. infectedColumn
    6. dayColumn
    7. predictionDay
    8. data
* dataFilter: this method ask none
* analysis: this method ask none
* generateJSON: this method ask for the analysis values
* generateConclution: this method ask for the analysis values

##### HTML item structure
For the html part, we have one form per file but all of them extends from index and within index we use the navbar template. We send our parameters through POST method for python to analyze them.

##### HTML report structure
Here we ask for the JSON data generated by our Python item file. We need the JSON data to feed our graphs with JavaScript. 
* For plotting we use a JavaScript library, Chart.js, specifically the LineCharts module
* For saving the canvas generated by Chart.js as PDF we use another JavaScript library, html2canvas.js

##### Application cycle
![SimpleAnalysisReport](https://drive.google.com/uc?export=view&id=1iWOwFqVbv_1gVJ5SgAgiXPUEE8r47f6L)