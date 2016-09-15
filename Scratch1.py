sentence = str(input("What is your sentence"))

sentenceList = sentence.split()

wordFreq = []
for w in sentenceList:
    wordFreq.append(sentenceList.count(w))

combinedDict = dict(zip(sentenceList, wordFreq))

#This finds the longest word in the sentenceList list
sortedWords = sorted(sentenceList, key=len)
longestWord =(sortedWords[-1])

for sentenceList,wordFreq in combinedDict.items():
    print('{:{}}:{}'.format(sentenceList, len(longestWord), wordFreq))
