import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from datetime import datetime

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
        print(self.data)

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
        plt.scatter(x, y, color='black')
        plt.plot(x, pred, color='blue')
        print('Prediccion ', regr.predict([[xToPredict]]))
        print('Error: ', mean_squared_error(y, pred))
        print('Coeficiente: ', regr.coef_)
        print('Determinacion: ', r2_score(y, pred))
        plt.show()