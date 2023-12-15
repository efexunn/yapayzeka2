class BayesManager:
    def CalculateBayesianModel(self, wordCountOnCategory, allWordCount, categoryTextLength, allTextLength):
        result = ((wordCountOnCategory / categoryTextLength)*(categoryTextLength/allTextLength)) / (allWordCount / allTextLength)
        return result