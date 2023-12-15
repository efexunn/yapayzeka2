from FileService import FileManager as fm
from BayesService import BayesManager as bm

cultureArtFile = fm.FileManager('data/culture_arts.txt').ExtractWords()
healthFile = fm.FileManager('data/health.txt').ExtractWords()
politicsFile = fm.FileManager('data/politics.txt').ExtractWords()
sportsFile = fm.FileManager('data/sports.txt').ExtractWords()

wordList = set(cultureArtFile + healthFile + politicsFile + sportsFile)

wordList = list(wordList)
kelimeDict = {}

for item in wordList:
    cultureCount = cultureArtFile.count(item)
    healthCount = healthFile.count(item)
    politicsCount = politicsFile.count(item)
    sportsCount = sportsFile.count(item)

    kelimeDict[item] = {'culture':cultureCount, 'health':healthCount, 'politics':politicsCount, 'sports':sportsCount}


wordCountOnCategory = kelimeDict["obama"]['politics']
allWordCount = kelimeDict["obama"]['culture'] + kelimeDict["obama"]['health']  + kelimeDict["obama"]['politics'] + kelimeDict["obama"]['sports']
categoryTextLength = len(politicsFile)
allTextLength = (len(politicsFile) + len(healthFile) + len(sportsFile) + len(cultureArtFile))
print(bm.BayesManager().CalculateBayesianModel(wordCountOnCategory, allWordCount, categoryTextLength, allTextLength))

