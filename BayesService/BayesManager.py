import math
import random
import matplotlib.pyplot as plt
import numpy as np
class BayesManager:
    bayesDict = {}
    def __init__(self, cultureArtFile, healthFile, politicsFile, sportsFile, wordList, wordDict):
        self.cultureArtFile = cultureArtFile
        self.healthFile = healthFile
        self.politicsFile = politicsFile
        self.sportsFile = sportsFile
        self.wordList = wordList
        self.wordDict = wordDict

        self.allWordCount = len(self.wordDict)

        self.cultureFileLength = len(self.cultureArtFile)
        self.healthFileLength = len(self.healthFile)
        self.politicsFileLength = len(self.politicsFile)
        self.sportsFileLength = len(self.sportsFile)
        self.sumOfLengths = self.cultureFileLength + self.healthFileLength + self.politicsFileLength + self.sportsFileLength


    def CalculateBayesianModel(self, wordCountOnCategory, categoryTextLength):
        result = (wordCountOnCategory + 1) / (categoryTextLength + self.allWordCount)

        return result

    def ListAllTextsBayesianModel(self):
        for word in self.wordList:
            cultureBayes = self.CalculateBayesianModel(self.wordDict[word]['culture'], self.cultureFileLength)
            healthBayes = self.CalculateBayesianModel(self.wordDict[word]['health'], self.healthFileLength)
            politicsBayes = self.CalculateBayesianModel(self.wordDict[word]['politics'], self.politicsFileLength)
            sportsBayes = self.CalculateBayesianModel(self.wordDict[word]['sports'], self.sportsFileLength)
            self.bayesDict[word] = {'culture': cultureBayes, 'health': healthBayes, 'politics': politicsBayes, 'sports': sportsBayes}

        return self.bayesDict

    def CalculateJudgementScores(self, text):
        bayesScoreList = self.ListAllTextsBayesianModel()
        cultureScore = 0
        healthScore = 0
        politicsScore = 0
        sportsScore = 0
        for word in text:
            try:
               cultureScore += bayesScoreList[word]['culture']
               healthScore += bayesScoreList[word]['health']
               politicsScore += bayesScoreList[word]['politics']
               sportsScore += bayesScoreList[word]['sports']
            except:
                cultureScore += 0
                healthScore += 0
                politicsScore += 0
                sportsScore += 0
                continue

        cultureScore += (self.cultureFileLength / self.sumOfLengths)
        healthScore += (self.healthFileLength / self.sumOfLengths)
        politicsScore += (self.politicsFileLength / self.sumOfLengths)
        sportsScore += (self.sportsFileLength / self.sumOfLengths)

        cultureScore = math.log(cultureScore)
        healthScore = math.log(healthScore)
        politicsScore = math.log(politicsScore)
        sportsScore = math.log(sportsScore)

        maxScore = max(cultureScore, healthScore, politicsScore, sportsScore)

        if(maxScore == cultureScore):
            return "Culture Arts"
        elif(maxScore == healthScore):
            return "Health"
        elif(maxScore == politicsScore):
            return "Politics"
        elif(maxScore == sportsScore):
            return "Sports"


    def CreateBarChartByBayes(self,bayesDict):
        # Veri yapısı
        data = {}
        for i in range(10):
            rand = random.randint(1,4200)
            data[self.wordList[rand]] = {
                'culture' : bayesDict[self.wordList[rand]]['culture'],
                'health': bayesDict[self.wordList[rand]]['health'],
                'politics': bayesDict[self.wordList[rand]]['politics'],
                'sports': bayesDict[self.wordList[rand]]['sports']
            }
        # Kategoriler
        categories = list(data.keys())

        # Her bir kelimenin kategorideki değerleri
        culture_values = [data[word]['culture'] for word in categories]
        health_values = [data[word]['health'] for word in categories]
        politics_values = [data[word]['politics'] for word in categories]
        sports_values = [data[word]['sports'] for word in categories]

        bar_width = 0.1
        index = np.arange(len(categories))

        plt.bar(index, culture_values, bar_width, label='culture')
        plt.bar(index + bar_width, health_values, bar_width, label='health')
        plt.bar(index + 2 * bar_width, politics_values, bar_width, label='politics')
        plt.bar(index + 3 * bar_width, sports_values, bar_width, label='sports')

        plt.xlabel('Words')
        plt.ylabel('Count')
        plt.title('Category Counts by Word')

        plt.xticks(index + 1.5 * bar_width, categories)  # Kategorilerin ortasına yerleştir
        # plt.figure(figsize=(8, 4))
        plt.legend()
        plt.show()

    def FindCategoryOfText(self, testList):
        judgementList = []
        for i in range(len(testList)):
            judgementList.append(f"Metin {i+1} Türü : {self.CalculateJudgementScores(testList[i])}")

        self.CreateBarChartByBayes(self.ListAllTextsBayesianModel())
        return judgementList

