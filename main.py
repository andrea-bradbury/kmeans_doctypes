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

class KeyWordXCount:
    def __init__(self, word, docType, count):
        self.word = word
        self.docType = docType
        self.count = count


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

# Create a master list of all Key Word Objects
for wordObject in allDocuments:
    file = KeyWord(wordObject.filename, wordObject.docType)
    masterKeyWords.append(file)

# Get count of master word list per doc type as a bar graph for each doc type
# Dictionary of words and doc types
docTypes = {
}
for i in masterKeyWords:
    docTypes[i.word] = masterKeyWords.count(i)
'''
for data in masterKeyWords:
    if data.word not in docTypes:
        docTypes[data.word] = masterKeyWords.count(data)
    else:
        docTypes.update({data.word: masterKeyWords.count(data)})
'''

# List of Dictionary keys
listOfDictionaryKeys = []
# list of Dictionary values
listOfDictionaryValues = []
for x in docTypes:
    listOfDictionaryKeys.append(x)
for x in docTypes:
  listOfDictionaryValues.append(docTypes[x])

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(listOfDictionaryKeys, listOfDictionaryValues)
plt.show()

# Filter master list of Key Word Objects into either unique words or common words
for wordObject in masterKeyWords:
    if wordObject.word not in uniqueWords:
        uniqueWords.append(wordObject.word)
        uniqueKeyWordObjects.append(wordObject)
    else:
        commonKeyWordObjects.append(wordObject)
        commonWordsList.append(wordObject.word)

# Get unique words
# These are either:
# - unique primary key words,
# - primary keywords that appear mulitple times but for the same doc type
# - or outliers
for word in uniqueKeyWordObjects:
    if word.word not in commonWordsList:
        actualUniqueDataPoints.append(word)
    else:
        for data in uniqueKeyWordObjects:
            if data.word in commonWordsList:
                for dataP in commonKeyWordObjects:
                    if data.docType == dataP.docType and data not in primaryKeyWordsForADocType:
                        primaryKeyWordsForADocType.append(data)



print("Master Words: ")
for dataPoint in masterKeyWords:
    print("Word: " + str(dataPoint.word) + ", Doc Type: " + str(dataPoint.docType))
print("\n")

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


