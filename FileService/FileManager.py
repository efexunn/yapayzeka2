class FileManager:
    text: ''

    # Constructor içerisinde parameter olarak gönderilendosya açılıyor.
    # Tüm karakterler lower hale getirilerek 'text' isimli değişkene atanıyor.
    def __init__(self, filePath):
        with open(filePath, 'r', encoding='utf-8-sig') as file:
           satirlar = file.readlines()
           self.text = ''.join(satirlar).lower()

    # Ödev pdf'inde verilen ingilizce bağlaçlar vb. listelenmesi.
    baglaclar = ["the", "all", "off", "of", "or", "but", "and", "through", "though",
                 "although",
                 "then", "not", "in", "out", "on", "about", "too", "yet", "nor", "either", "neither",
                 "so", "therefore", "moreover", "furthermore", "however", "also", "hence", "to", "at",
                 "from", "with", "by", "as", "this", "that", "these", "those", "between",
                 "only",
                 "for", "a", "an", "into", "non", "no", "yes", "up", "down", "even", "ever", "am",
                 "is", "are", "was", "were", "will", "i", "he", "she", "we", "they", "it", "you", "my",
                 "its", "his", "her", "their", "our", "your", "have", "has", "be", "been", "do", "does",
                 "not", "thus", "would", "could", "can", "until", "him", "me", "them", "us", "if",
                 "unless", "who", "when", "where", "which", "whether", "what", "why", "whoever",
                 "whatever", "whom", "had", "away", "did", "there", "whose", "more", "most", "co",
                 "re", "la", "le", "any", "other", "each", "much", "than", "some", "every", "thing",
                 "else", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "vs"]

    # Noktalama işaretleri
    noktalamalar = [
        ",", ".", ";", ":", "-", "_", "“", "”", "‘", "’"
    ],

    # Yukarıdaki filtrelemerden kalan değerleri ve boş elemanları temizlemek için kullanılan liste
    garbage = [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "#", "$", "%", "'", ".", ",", ";", ":", "“", "”", "‘", "’"
    ]

    # Model olarak alınan text dosyalarındaki satır atlama boşluklarını kaldırır ve '#' işaretinden olacak şekilde
    # metinlere ayırır.
    def SeperateText(self, textFile):
        textFile = textFile.replace("\n", " ")
        textFile = textFile.split("#")
        return textFile


    # Yukarıda bulunan baglacları okunan dosya içerisinden silen ve yerine boşluk koyan fonksiyon
    def RemoveBaglacFromTxtFile(self,textFile):
        for baglac in self.baglaclar:
            textFile = textFile.replace(f' {baglac} ', ' ')
        return textFile

    # Yukarıda bulunan noktalama listesini okunan metin içinden kaldıran fonskyion
    def RemoveNoktalamaFromTxtFile(self,textFile):
        for noktalamalar in self.noktalamalar:
            textFile = textFile.replace(f'{noktalamalar} ', ' ')
        return textFile

    # Metni kelimelerin oluşturduğu bir listeye ayıran fonksiyon
    def StringToArray(self,textFile):
       return textFile.split()

    # Metinden ayıklanamayan sayı gibi değerleri metinden silen fonksiyon
    def RemoveGarbageFromArray(self, arr):
        for i in range(len(arr)):
            for sayi in self.garbage:
                arr[i] = arr[i].replace(f"{sayi}", "")
        return arr

    # Boş kalan elemanları listeden kaldıran fonksiyon
    def RemoveEmptyStringFromArray(self, arr):
        return list(filter(lambda x : x != "", arr))

    # Gönderilen örnek metinleri YUKARIDAKİ FONKSİYONLARI KULLANARAK parçalayıp listeleyen fonksiyon
    def ExtractWords(self):
        textFile = self.text
        textFile = self.RemoveBaglacFromTxtFile(textFile)
        textFile= self.RemoveNoktalamaFromTxtFile(textFile)
        textFile = self.StringToArray(textFile)
        textFile = self.RemoveGarbageFromArray(textFile)
        result = self.RemoveEmptyStringFromArray(textFile)
        return result

    # Test için gönderilen txt dosyasını 12 ayrı metine ve o metinleri de kelimelerin olduğu bir sözlüğe ayıran fonksiyon.
    def ExtractToTextListsToWords(self):
        textFile = self.text
        textFile = self.SeperateText(textFile)
        textFile = self.RemoveEmptyStringFromArray(textFile)
        for i in range(len(textFile)):
            temp = self.RemoveBaglacFromTxtFile(textFile[i])
            temp = self.RemoveNoktalamaFromTxtFile(temp)
            temp = self.StringToArray(temp)
            temp = self.RemoveGarbageFromArray(temp)
            temp = self.RemoveEmptyStringFromArray(temp)
            textFile[i] = temp
        return textFile




























