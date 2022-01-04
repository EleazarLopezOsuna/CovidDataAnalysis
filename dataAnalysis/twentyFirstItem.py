import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from datetime import datetime
import json
import math

class twentyFirstItem():

    def __init__(self, infectedColumn, deathsColumn, dayColumn, predictionDay, data):
        self.infectedColumn = infectedColumn
        self.deathsColumn = deathsColumn
        self.dayColumn = dayColumn
        self.predictionDate = predictionDay
        self.data = data.dropna(subset=[infectedColumn, deathsColumn, dayColumn])

    def analysis1(self):
        transformedDate = []
        savedDayColumn = self.data[self.dayColumn]
        for date in self.data[self.dayColumn]:
            formatedDate = datetime.now()
            try:
                formatedDate = datetime.strptime(date, '%d/%m/%Y')
            except:
                try:
                    formatedDate = datetime.strptime(date, '%Y/%m/%d')
                except:
                    try:
                        formatedDate = datetime.strptime(date, '%Y-%m-%d')
                    except:
                        formatedDate = datetime.strptime(date, '%Y-%m-%d')
            transformedDate.append(int(datetime.timestamp(formatedDate)))
        self.data[self.dayColumn] = transformedDate
        self.data = self.data.drop_duplicates(subset=[self.dayColumn], keep='last')
        x = np.asarray(self.data[self.dayColumn]).reshape(-1, 1)
        self.data[self.dayColumn] = savedDayColumn
        y1 = self.data[self.infectedColumn]
        formatedDate = datetime.now()
        try:
            formatedDate = datetime.strptime(self.predictionDate, '%d-%m-%Y')
        except:
            formatedDate = datetime.strptime(self.predictionDate, '%Y-%m-%d')
        xToPredict = int(datetime.timestamp(formatedDate))
        regr = linear_model.LinearRegression()
        regr.fit(x, y1)
        pred1 = regr.predict(x)
        prediction1 = regr.predict([[xToPredict]])
        mse1 = math.sqrt(mean_squared_error(y1, pred1))
        coef1 = regr.coef_
        intercept1 = regr.intercept_
        r21 = r2_score(y1, pred1)


        y2 = self.data[self.deathsColumn]
        formatedDate = datetime.now()
        try:
            formatedDate = datetime.strptime(self.predictionDate, '%d-%m-%Y')
        except:
            formatedDate = datetime.strptime(self.predictionDate, '%Y-%m-%d')
        xToPredict = int(datetime.timestamp(formatedDate))
        regr = linear_model.LinearRegression()
        regr.fit(x, y2)
        pred2 = regr.predict(x)
        prediction2 = regr.predict([[xToPredict]])
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
        jsonString = self.generateJSON1(labels, setValues, predictedValues, formatedDate, prediction1, mse1, r21, coef1, prediction2, mse2, r22, coef2, intercept1, intercept2)
        return jsonString

    def generateJSON1(self, labels, setValues, predictedValues, formatedDate, prediction1, mse1, r21, coef1, prediction2, mse2, r22, coef2, intercept1, intercept2):
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
        conclutionOutput = self.generateConclution1(formatedDate, prediction1, mse1, r21, coef1, prediction2, mse2, r22, coef2, intercept1, intercept2)
        output = '{' + labelsOutput + setValuesOutput + predictedValuesOutput + graphName + conclutionOutput + '}'
        return json.loads(output)

    def generateConclution1(self, formatedDate, prediction1, mse1, r21, coef1, prediction2, mse2, r22, coef2, intercept1, intercept2):
        output = '"conclution": {'
        header = '"header": ["Eleazar Jared Lopez Osuna", "Facultad de Ingenieria", "Universidad de San Carlos de Guatemala", "Guatemala, Guatemala", "eleazarjlopezo@gmail.com"],'
        leftColumn = '"leftColumn": "'
        leftColumn += '   En base a la informacion proporcionada y aplicando metodos analiticos mediante el uso de software, se obtuvieron los '
        leftColumn += 'siguientes valores: \\nEl coeficiente de regresion lineal obtenido '
        leftColumn += 'fue de ' + str(np.round(coef1, 4)) + '\\nEl error cuadratico medio (ECM) es de ' + str(np.round(mse1, 4))
        leftColumn += '\\nLa prediccion obtenida para la fecha ' + str(formatedDate) + ' es de ' + str(np.round(prediction1, 4)) + ' casos. '
        leftColumn += '\\nEn base a la informacion proporcionada y aplicando metodos analiticos mediante el uso de software, se obtuvieron los '
        leftColumn += 'siguientes valores: \\nEl coeficiente de regresion lineal obtenido '
        leftColumn += 'fue de ' + str(np.round(coef2, 4)) + '\\nEl error cuadratico medio (ECM) es de ' + str(np.round(mse2, 4))
        leftColumn += '\\nLa prediccion obtenida para la fecha ' + str(formatedDate) + ' es de ' + str(np.round(prediction2, 4)) + ' muertos.", '
        rightColumn = '"rightColumn": "   Mediante el uso de librerias tales como pandas, sklearn, scipy, numpy y flask '
        rightColumn += 'y los datos proporcionados, se creo un modelo de regresion lineal el cual es capaz de realizar predicciones '
        rightColumn += 'sobre el comportamiento de los casos en todo el mundo. El modelo tiene un coeficiente de determinacion de '
        rightColumn += str(np.round(r21, 4)) + ' lo cual indica que '
        rightColumn += 'el modelo esta ajustado de manera correcta. ' if(r21 > 0.7) else 'el modelo no esta ajustado de la mejor manera. '
        rightColumn += 'El modelo fue entrenado mediante la ecuacion y = ' + str(np.round(coef1, 4)) + 'X +' + '(' + str(np.round(intercept1, 4)) + ')'
        rightColumn += '\\nMediante el uso de librerias tales como pandas, sklearn, scipy, numpy y flask '
        rightColumn += 'y los datos proporcionados, se creo un modelo de regresion lineal el cual es capaz de realizar predicciones '
        rightColumn += 'sobre el comportamiento de los muertos en el mundo. El modelo tiene un coeficiente de determinacion de '
        rightColumn += str(np.round(r22, 4)) + ' lo cual indica que '
        rightColumn += 'el modelo esta ajustado de manera correcta. ' if(r22 > 0.7) else 'el modelo no esta ajustado de la mejor manera. '
        rightColumn += 'El modelo fue entrenado mediante la ecuacion y = ' + str(np.round(coef2, 4)) + 'X +' + '(' + str(np.round(intercept2, 4)) + ')", '
        bottomColumn = '"bottomColumn": "'
        bottomColumn += '   Conforme a la informacion presentada en los puntos anteriores, se puede concluir que para la fecha ' + str(formatedDate)
        bottomColumn += ' se espera que la proporcion entre casos y muertes sea de ' + str(prediction2/prediction1) + ' lo que significa que por cada '
        bottomColumn += 'caso se tendran ' + str(prediction2/prediction1) + ' muertes."'
        output += header + leftColumn + rightColumn + bottomColumn + '}'
        return output

    def analysis2(self):
        transformedDate = []
        for date in self.data[self.dayColumn]:
            formatedDate = datetime.now()
            try:
                formatedDate = datetime.strptime(date, '%d/%m/%Y')
            except:
                try:
                    formatedDate = datetime.strptime(date, '%Y/%m/%d')
                except:
                    try:
                        formatedDate = datetime.strptime(date, '%Y-%m-%d')
                    except:
                        formatedDate = datetime.strptime(date, '%Y-%m-%d')
            transformedDate.append(int(datetime.timestamp(formatedDate)))
        self.data[self.dayColumn] = transformedDate
        self.data = self.data.drop_duplicates(subset=[self.dayColumn], keep='last')
        x = np.asarray(self.data[self.dayColumn]).reshape(-1, 1)
        y = self.data[self.deathsColumn]
        formatedDate = datetime.now()
        try:
            formatedDate = datetime.strptime(self.predictionDate, '%d-%m-%Y')
        except:
            formatedDate = datetime.strptime(self.predictionDate, '%Y-%m-%d')
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