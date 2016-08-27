import re
import string
import os
import json
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

with open('query.txt') as f:
    content = f.readlines()

queryAll=[]
queryResultAll=[]
stop_words=set(stopwords.words("english"))
leematizer=WordNetLemmatizer()

#for i in range(8):                # No of Queries
 #   queryResultAll.append([])


for queryLine in content:
    queryWordList = re.sub('['+string.punctuation+']', '', queryLine).split()
    queryWordList = queryWordList[1:]
    for word in queryWordList:
        if word in stop_words:
            queryWordList.remove(word)
    queryWordListLem=[]
    for word in queryWordList:
        queryWordListLem.append(leematizer.lemmatize(word))
    queryAll.append(queryWordListLem)


dict={}


for filename in os.listdir(os.getcwd()+'\Docs'):                                 #For every file in docs
    file=open(os.getcwd()+'\Docs\\'+filename,'r').read()
    file=re.sub('['+string.punctuation+']', '', file).split()
    for word in file:
        if word in stop_words:
            file.remove(word)
    textLem=[]
    for word in file:
        textLem.append(leematizer.lemmatize(word))

    textLem=set(textLem)
    textLem=list(textLem)

    for word in textLem:
        if word in dict.keys():
            dict[word].append(filename)
        else:
            dict[word]=[filename]
'''
for queryWordList in queryAll:
    #if len(queryWordList)!=0 and queryWordList[0] in dict.keys():
     #   queryResult=set(dict[queryWordList[0]])

    queryResult={}
    for queryWord in queryWordList:
        if queryWord in dict.keys():
            if len(queryResult)==0:
                queryResult=set(dict[queryWord])
            else:
                queryResult=queryResult.intersection(set(dict[queryWord]))

        else:
            queryResult={}
            break;

    queryResultAll.append(list(queryResult))

for i in range (len(queryAll)):
    print(queryAll[i],':',queryResultAll[i])

'''
json.dump(dict, open("text9.txt",'w'))