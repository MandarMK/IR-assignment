import re
import string
import os

with open('query.txt') as f:
    content = f.readlines()

queryAll=[]
queryResultAll=[]
for i in range(100):                # No of Queries
    queryResultAll.append([])


for queryLine in content:
    queryWordList = re.sub('['+string.punctuation+']', '', queryLine).split()
    queryWordList = queryWordList[1:]
    queryAll.append(queryWordList)

for filename in os.listdir(os.getcwd()+'\Docs'):                                 #For every file in docs
    file=open(os.getcwd()+'\Docs\\'+filename,'r').read()
    file=re.sub('['+string.punctuation+']', '', file).split()                   # FILE is now a list of all the words

    for i,queryWordList in enumerate(queryAll):
        if(set(queryWordList).issubset(file)):
            queryResultAll[i].append(filename)

print(queryResultAll)

