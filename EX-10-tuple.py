# get dictionary of words and the no of time the appier in a file
# the sort the list by key

inputFile='romeo.txt'
inputPath='inputs/'
file=inputPath+inputFile

try:
    fileH=open('inputs/'+inputFile)
except:
    print('no such file '+file)
    exit()

fileH=open('inputs/'+inputFile)

wordCount=dict()


for line in fileH:
    line=line.strip()
    mywords=line.split()

    for Aword in mywords:
        wordCount[Aword]=wordCount.get(Aword,0) +1

        lst1=list()
        for (k,v) in wordCount.items():
            mytuple=(v,k)
            lst1.append(mytuple)
lst1.sort()
#print(lst1)

print(wordCount)








#print('===')
