from FileService import FileManager as fm
from BayesService import BayesManager as bm

cultureArtFile = fm.FileManager('data/culture_arts.txt').ExtractWords()
healthFile = fm.FileManager('data/health.txt').ExtractWords()
politicsFile = fm.FileManager('data/politics.txt').ExtractWords()
sportsFile = fm.FileManager('data/sports.txt').ExtractWords()

testFileTextList = fm.FileManager('data/testData.txt').ExtractToTextListsToWords()

#Training metinlerinde bulunan farklı her kelimenin listelenmesi
wordList = set(cultureArtFile + healthFile + politicsFile + sportsFile)
wordList = list(wordList)

#Kelimelerin hangi metinde kaç defa geçtiğini sayan ve bunu dictionary halinde tutan dictionary
wordDict = {}

for item in wordList:
    cultureCount = cultureArtFile.count(item)
    healthCount = healthFile.count(item)
    politicsCount = politicsFile.count(item)
    sportsCount = sportsFile.count(item)

    wordDict[item] = {'culture':cultureCount, 'health':healthCount, 'politics':politicsCount, 'sports':sportsCount}

# Bayes manager object
bayesManager = bm.BayesManager(cultureArtFile, healthFile, politicsFile, sportsFile, wordList, wordDict)

result = bayesManager.FindCategoryOfText(testFileTextList)

for item in result:
    print(item)
