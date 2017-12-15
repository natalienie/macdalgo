import quandl
import pandas as pd
import numpy as np
import time
import pickle
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


class machine_learning_algo(object):

    def __init__(self, stock_name, feature, feature_len, interval):

        self.api = '5DJz3EfSFxJq2RYxe1ZA'
        self.name = stock_name
        self.col = training_feature
        self.feature_len = feature_len
        self.interval = interval
        dataframe = self.concate_get_macd()
        self.patternStorage()


    def concate_get_macd(self):

        df = quandl.get('WIKI/stock_name', api_key=self.api)
        short_ave = df['Adj. Close'].rolling(12).mean()
        long_ave = df['Adj. Close'].rolling(26).mean()
        diff = short_ave - long_ave
        dea = diff.rolling(9).mean()
        macd = diff - dea
        df[MACD] = macd
        df.dropna(axis=1, inplace=True)
        dataf = df[['Adj. Close'], ['Adj. Volume'], ['MACD']]
        return dataf.to_pickle('data.pickle')

    def percentChange(self, startpoint, currentpoint):

        x = ((float(currentpoint)-startpoint)/abs(startpoint))*100.00
            #if x == 0.0:
                #return 0.0000000001
            #else:
        return x
        #except:
            #return 0.0001

    def patternStorage(self):

        patterAr = []
        performanceAr = []
        data = pd.read_pickle(dataframe)
        x = len(data) - len(self.feature_len) - 20
        y = self.feature_len + 1
        currentStance = 'none'
        while y < x:
            pattern = []

            for i in range(1, y):
                pi = self.percentChange(data['self.col'][y-self.feature_len], data['self.col'][y-i])
                pattern.append(pi)

                outcomeRange = data['Adj. Close'][y+20: y+30]
                currentpoint = data['Adj. Close'][y]
                #try:

                outcome = 0
                for num in outcomeRange:
                    outcome  += num
                avgOutcome = outcome / len(outcomeRange)

                   #print(str(e))
                   #avgOutcome = 0

                futureoutcome = percentChange(currentPoint, avgOutcome)
                performanceAr.append(futureoutcome)

            y += self.interval
            print(len(patterAr))
            print(len(performanceAr))


    def currentPattern(self):

        patForRec = []

        for i in range(1, y):
            cpi = self.percentChange(data['self.col'][-y], data['self.col'][-y+i])
            patForRec.append(cpi)
        return patForRec
        #print(patForRec)


    def patterRecognition(self):
        y = self.feature_len + 1
        for eachPattern in patternAr:
            sim = 0
            for i in range(1, y):
                sim_i = 100.00 - abs(percentChange(eachPattern[i-1], self.currentPattern()[i-1]))
                sim += sim_i
            howSim = sim / float(y)

            if howSim > 70:
                patdex = patternAr.index(eachPattern)
                print(patdex)

        xp = [i for i in range(1, y)]
        fig = plt.figure()
        plt.plot(xp, self.currentPattern())
        plt.plot(xp, eachPattern)
        plt.show()
