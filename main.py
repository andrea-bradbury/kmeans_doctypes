import re

class FileName:
    def __init__(self, filename, fileExtension, docType):
        self.filename = filename
        self.fileExtension = fileExtension
        self.docType = docType

    def __str__(self):
        print("{ \n" +
            self.word + "\n" +
            self.docType + "\n}")

class KeyWord:
    def __init__(self, word, docType):
        self.word = word
        self.docType = docType


    def __str__(self):
        print(self.word + self.docType)


# Reads file
df = open("AllFilesAndDocTypes.txt", "r")

# Format file contents into FileName Objects of each word in the filename
allDocuments = []
try:
    for line in df:
        data = line.split(",")
        fileNameAndExtension = data[0].split(".")
        separateWords = re.sub('[^A-Za-z0-9]+', ' ', fileNameAndExtension[0])
        separateWords = separateWords.split(" ")
        docType = data[1].split("\n")
        for word in separateWords:
            fileNameData = FileName(word.upper(), fileNameAndExtension[1], docType[0])
            allDocuments.append(fileNameData)
except:
    df.close()

# Master list of all KeyWord Objects
masterKeyWords = []

# A list of unique words from all file names irrespective of doctype
uniqueWords = []

# A list of KeyWord objects that appear more than once in all file names irrespective of doctype
commonKeyWordObjects = []

# A list of the common words that appear more than once in all the file names irrespective of doctype
commonWordsList = []

# A list of the first occurence of unique KeyWord objects
uniqueKeyWordObjects = []

# A list of completely unique KeyWord objects data points.
# These will always be primary terms but could be outliers
actualUniqueDataPoints = []

# A list of common KeyWord objects per doctype - These have potential to be primary key words for that doc type
primaryKeyWordsForADocType = []

for wordObject in allDocuments:
    masterKeyWords.append(wordObject)

for wordObject in masterKeyWords:
    if wordObject.filename not in uniqueWords:
        primaryWord = KeyWord(wordObject.filename, wordObject.docType)
        uniqueWords.append(wordObject.filename)
        uniqueKeyWordObjects.append(primaryWord)
    else:
        notUnique = KeyWord(wordObject.filename, wordObject.docType)
        commonKeyWordObjects.append(notUnique)
        commonWordsList.append((notUnique.word))


for word in uniqueKeyWordObjects:
    if word.word not in commonWordsList:
        actualUniqueDataPoints.append(word)
    else:
        pass

for data in uniqueKeyWordObjects:
    if data.word in commonWordsList:
        for dataP in commonKeyWordObjects:
            if data.docType == dataP.docType and data not in primaryKeyWordsForADocType:
                primaryKeyWordsForADocType.append(data)


print("Unique words: " + str(uniqueWords))
print("Common word list: " + str(commonWordsList))
print("\n")
print("CommonKeyWordObjects: ")
for commonWord in commonKeyWordObjects:
    print("Word: " + str(commonWord.word) + ", Doc type: " + str(commonWord.docType))


print("\n")
print("Unique Data Point:")
for uniqueDataPoint in uniqueKeyWordObjects:
    print("Word: " + str(uniqueDataPoint.word) + ", Doc Type: " + str(uniqueDataPoint.docType))


print("\n")
print("Actual unique data points (Primary key words):")
for dataPoint in actualUniqueDataPoints:
    print("Word: " + str(dataPoint.word) + ", Doc Type: " + str(dataPoint.docType))

print("\n")
print("Common Primary Key words for a doc type (Primary key words):")
for dataPoint in primaryKeyWordsForADocType:
    print("Word: " + str(dataPoint.word) + ", Doc Type: " + str(dataPoint.docType))