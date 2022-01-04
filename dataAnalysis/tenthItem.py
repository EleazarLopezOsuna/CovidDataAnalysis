import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from datetime import datetime
import json
import math

class tenthItem():

    def __init__(self, countryColumn, firstCountryName, secondCountryName, vaccinedColumn, dayColumn, data):
        self.countryColumn = countryColumn
        self.firstCountryName = firstCountryName
        self.secondCountryName = secondCountryName
        self.dayColumn = dayColumn
        self.vaccinedColumn = vaccinedColumn
        self.data = data.dropna(subset=[countryColumn, vaccinedColumn, dayColumn])
        self.firstSet = self.data
        self.secondSet = self.data

    def dataFilter(self):
        isCountry = self.data[self.countryColumn] == self.firstCountryName
        self.firstSet = self.data[isCountry]
        isCountry = self.data[self.countryColumn] == self.secondCountryName
        self.secondSet = self.data[isCountry]

    def analysis1(self):
        transformedDate = []
        savedDayColumn = self.firstSet[self.dayColumn]
        for date in self.firstSet[self.dayColumn]:
            formatedDate = datetime.now()
            try:
                formatedDate = datetime.strptime(date, '%d/%m/%Y')
            except:
                formatedDate = datetime.strptime(date, '%Y/%m/%d')
            transformedDate.append(int(datetime.timestamp(formatedDate)))
        self.firstSet[self.dayColumn] = transformedDate
        self.firstSet = self.firstSet.drop_duplicates(subset=[self.dayColumn], keep='last')
        x = np.asarray(self.firstSet[self.dayColumn]).reshape(-1, 1)
        self.firstSet[self.dayColumn] = savedDayColumn
        y1 = self.firstSet[self.vaccinedColumn]
        regr = linear_model.LinearRegression()
        regr.fit(x, y1)
        pred1 = regr.predict(x)
        mse1 = math.sqrt(mean_squared_error(y1, pred1))
        coef1 = regr.coef_
        intercept1 = regr.intercept_
        r21 = r2_score(y1, pred1)

        transformedDate = []
        savedDayColumn = self.secondSet[self.dayColumn]
        for date in self.secondSet[self.dayColumn]:
            formatedDate = datetime.now()
            try:
                formatedDate = datetime.strptime(date, '%d/%m/%Y')
            except:
                formatedDate = datetime.strptime(date, '%Y/%m/%d')
            transformedDate.append(int(datetime.timestamp(formatedDate)))
        self.secondSet[self.dayColumn] = transformedDate
        self.secondSet = self.secondSet.drop_duplicates(subset=[self.dayColumn], keep='last')
        x = np.asarray(self.secondSet[self.dayColumn]).reshape(-1, 1)
        self.secondSet[self.dayColumn] = savedDayColumn
        y2 = self.secondSet[self.vaccinedColumn]
        regr = linear_model.LinearRegression()
        regr.fit(x, y2)
        pred2 = regr.predict(x)
        mse2 = math.sqrt(mean_squared_error(y2, pred2))
        coef2 = regr.coef_
        intercept2 = regr.intercept_
        r22 = r2_score(y2, pred2)


        labels = []
        for label in x:
            dt_obj = datetime.fromtimestamp(label[0]).strftime('%d-%m-%y')
            labels.append(dt_obj)
        setValues = []
        for value in y1:
            setValues.append(value)
        predictedValues = []
        for value in pred1:
            predictedValues.append(value)
        jsonString = self.generateJSON1(labels, setValues, predictedValues, mse1, r21, coef1, mse2, r22, coef2, intercept1, intercept2)
        return jsonString

    def generateJSON1(self, labels, setValues, predictedValues, mse1, r21, coef1, mse2, r22, coef2, intercept1, intercept2):
        labelsOutput = '"labels": ['
        contador = 0
        for label in labels:
            if contador == 0:
                labelsOutput += '"' + str(label) + '"'
            else:
                labelsOutput += ', "' + str(label) + '"'
            contador += 1
        labelsOutput += '], '
        setValuesOutput = '"setValues": ['
        contador = 0
        for value in setValues:
            if contador == 0:
                setValuesOutput += '"' + str(value) + '"'
            else:
                setValuesOutput += ', "' + str(value) + '"'
            contador += 1
        setValuesOutput += '], '
        predictedValuesOutput = '"predictedValues": ['
        contador = 0
        for value in predictedValues:
            if contador == 0:
                predictedValuesOutput += '"' + str(value) + '"'
            else:
                predictedValuesOutput += ', "' + str(value) + '"'
            contador += 1
        predictedValuesOutput += '], '
        graphName = '"graphName": "Predicciones de casos en todo el mundo", '
        conclutionOutput = self.generateConclution1(mse1, r21, coef1, mse2, r22, coef2, intercept1, intercept2)
        output = '{' + labelsOutput + setValuesOutput + predictedValuesOutput + graphName + conclutionOutput + '}'
        return json.loads(output)

    def generateConclution1(self, mse1, r21, coef1, mse2, r22, coef2, intercept1, intercept2):
        output = '"conclution": {'
        header = '"header": ["Eleazar Jared Lopez Osuna", "Facultad de Ingenieria", "Universidad de San Carlos de Guatemala", "Guatemala, Guatemala", "eleazarjlopezo@gmail.com"],'
        leftColumn = '"leftColumn": "'
        leftColumn += '   En base a los resultados obtenidos, se obseva que ' + self.firstCountryName
        leftColumn += ' tiene un coeficiente de regresion lineal de ' + str(np.round(coef1, 4)) 
        leftColumn += ', ademas su error cuadratico medio es de ' + str(np.round(mse1, 4))
        leftColumn += ', tambien se hizo un calculo del coeficiente de determinacion el cual arrojo un valor de ' + str(np.round(mse1, 4))
        leftColumn += '. Mientras que para ' + self.secondCountryName
        leftColumn += ' se obtuvo que el coeficiente de regresion lineal equivale a ' + str(np.round(coef2, 4))
        leftColumn += ', por otro lado el error cuadratico medio es de ' + str(np.round(mse2, 4))
        leftColumn += ', asimismo, se obtuvo el valor del coeficiente de determinacion el cual fue de ' + str(np.round(mse1, 4)) + '.", '
        rightColumn = '"rightColumn": "'
        rightColumn += '   Haciendo uso de herramientas de analisis de datos y python como motor de procesamiento, se entraron '
        rightColumn += 'dos modelos los cuales son los siguientes: Para ' + self.firstCountryName
        rightColumn += ': y = ' + str(np.round(coef1, 4)) + ' X + (' + str(np.round(intercept1, 4)) + '), '
        rightColumn += 'para ' + self.secondCountryName + ': y = ' + str(np.round(coef2, 4)) + ' X + (' + str(np.round(intercept2, 4)) + '). '
        rightColumn += 'Haciendo un analisis sobre los datos proporcionados por los coeficientes de determinacion obtenemos que para ' + self.firstCountryName 
        rightColumn += ' el modelo esta ajustado de manera correcta. ' if(r21 > 0.7) else ' el modelo no esta ajustado de la mejor manera. '
        rightColumn += 'y ' + self.secondCountryName
        rightColumn += ' el modelo esta ajustado de manera correcta.", ' if(r22 > 0.7) else ' el modelo no esta ajustado de la mejor manera.", '
        bottomColumn = '"bottomColumn": "'
        bottomColumn += '   Conforme a los datos recopilados anteriormente podemos decir con certeza que las vacunas en ' + self.firstCountryName
        bottomColumn += ' crece con '
        bottomColumn += 'mayor ' if(coef1 > coef2) else 'menor '
        bottomColumn += 'velocidad que en ' + self.secondCountryName + '. Ademas, sabemos que en los datos obtenidos para ' + self.firstCountryName
        bottomColumn += ' podemos confiar con '
        bottomColumn += 'mayor ' if(r21 > r22) else 'menor '
        bottomColumn += 'certeza que en ' + self.secondCountryName + '. Por ultimo, gracias al calculo de los errores cuadraticos medios sabemos que '
        bottomColumn += 'los datos calculados para ' + self.firstCountryName + ' tiene un error '
        bottomColumn += 'mayor ' if(mse1 > mse2) else 'menor '
        bottomColumn += ' que los datos calculados para ' + self.secondCountryName + '" '
        output += header + leftColumn + rightColumn + bottomColumn + '}'
        return output

    def analysis2(self):
        transformedDate = []
        for date in self.secondSet[self.dayColumn]:
            formatedDate = datetime.now()
            try:
                formatedDate = datetime.strptime(date, '%d/%m/%Y')
            except:
                formatedDate = datetime.strptime(date, '%Y/%m/%d')
            transformedDate.append(int(datetime.timestamp(formatedDate)))
        self.secondSet[self.dayColumn] = transformedDate
        self.secondSet = self.secondSet.drop_duplicates(subset=[self.dayColumn], keep='last')
        x = np.asarray(self.secondSet[self.dayColumn]).reshape(-1, 1)
        y = self.secondSet[self.vaccinedColumn]
        regr = linear_model.LinearRegression()
        regr.fit(x, y)
        pred = regr.predict(x)
        labels = []
        for label in x:
            dt_obj = datetime.fromtimestamp(label[0]).strftime('%d-%m-%y')
            labels.append(dt_obj)
        setValues = []
        for value in y:
            setValues.append(value)
        predictedValues = []
        for value in pred:
            predictedValues.append(value)
        jsonString = self.generateJSON2(labels, setValues, predictedValues)
        return jsonString

    def generateJSON2(self, labels, setValues, predictedValues):
        graphName = '"graphName": "Predicciones de muertes en todo el mundo", '
        labelsOutput = '"labels": ['
        contador = 0
        for label in labels:
            if contador == 0:
                labelsOutput += '"' + str(label) + '"'
            else:
                labelsOutput += ', "' + str(label) + '"'
            contador += 1
        labelsOutput += '], '
        setValuesOutput = '"setValues": ['
        contador = 0
        for value in setValues:
            if contador == 0:
                setValuesOutput += '"' + str(value) + '"'
            else:
                setValuesOutput += ', "' + str(value) + '"'
            contador += 1
        setValuesOutput += '], '
        predictedValuesOutput = '"predictedValues": ['
        contador = 0
        for value in predictedValues:
            if contador == 0:
                predictedValuesOutput += '"' + str(value) + '"'
            else:
                predictedValuesOutput += ', "' + str(value) + '"'
            contador += 1
        predictedValuesOutput += ']'
        output = '{' + graphName + labelsOutput + setValuesOutput + predictedValuesOutput + '}'
        return json.loads(output)