import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from datetime import datetime
import json

class firstItem():

    def __init__(self, continentColumn, continentName, countryColumn, countryName, infectedColumn, dayColumn, predictionDay, data):
        self.continentColumn = continentColumn
        self.continentName = continentName
        self.countryColumn = countryColumn
        self.countryName = countryName
        self.infectedColumn = infectedColumn
        self.dayColumn = dayColumn
        self.predictionDate = predictionDay
        self.data = data

    def dataFilter(self):
        if(self.continentColumn != ''):
            isContinent = self.data[self.continentColumn] == self.continentName
            self.data = self.data[isContinent]
        if(self.countryColumn != ''):
            isCountry = self.data[self.countryColumn] == self.countryName
            self.data = self.data[isCountry]

    def analysis(self):
        transformedDate = []
        for date in self.data[self.dayColumn]:
            formatedDate = datetime.now()
            try:
                formatedDate = datetime.strptime(date, '%d/%m/%Y')
            except:
                formatedDate = datetime.strptime(date, '%Y/%m/%d')
            transformedDate.append(int(datetime.timestamp(formatedDate)))
        self.data[self.dayColumn] = transformedDate
        x = np.asarray(self.data[self.dayColumn]).reshape(-1, 1)
        y = self.data[self.infectedColumn]
        formatedDate = datetime.now()
        try:
            formatedDate = datetime.strptime(self.predictionDate, '%d-%m-%Y')
        except:
            formatedDate = datetime.strptime(self.predictionDate, '%Y-%m-%d')
        xToPredict = int(datetime.timestamp(formatedDate))
        regr = linear_model.LinearRegression()
        regr.fit(x, y)
        pred = regr.predict(x)
        prediction = regr.predict([[xToPredict]])
        mse = mean_squared_error(y, pred)
        coef = regr.coef_
        r2 = r2_score(y, pred)
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
        jsonString = self.generateJSON(labels, setValues, predictedValues)
        return jsonString

    def generateJSON(self, labels, setValues, predictedValues):
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
        graphName = '"graphName": "Tendencia de la infeccion por Covid-19 para ' + self.countryName + '" '
        output = '{' + labelsOutput + setValuesOutput + predictedValuesOutput + graphName + '}'
        return json.loads(output)

    def generateConclution(self, formatedDate, prediction, mse, r2, coef):
        dt_obj = datetime.fromtimestamp(formatedDate).strftime('%d-%m-%y')
