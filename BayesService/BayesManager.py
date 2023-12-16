import math
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

        cultureScore = math.log(cultureScore, 10)
        healthScore = math.log(healthScore, 10)
        politicsScore = math.log(politicsScore, 10)
        sportsScore = math.log(sportsScore, 10)

        maxScore = max(cultureScore, healthScore, politicsScore, sportsScore)

        if(maxScore == cultureScore):
            return "Culture Arts"
        elif(maxScore == healthScore):
            return "Health"
        elif(maxScore == politicsScore):
            return "Politics"
        elif(maxScore == sportsScore):
            return "Sports"


    def FindCategoryOfText(self, testList):
        judgementList = []
        for i in range(len(testList)):
            judgementList.append(f"Metin {i+1} Türü : {self.CalculateJudgementScores(testList[i])}")

        return judgementList

