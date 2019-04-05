#10.2 read  mbox-short.txt and figure out the distribution by hour of the day
#for each of the messages.
# print out the counts, sorted by hour

inputFile='mbox-short.txt'
inputPath='inputs/'

try:
    fileH=open(inputPath + inputFile)
except:
    print('no such file '+file)
    exit()

fileH=open(inputPath + inputFile)

wordCount=dict()
lst1=list()

for line in fileH:
    line=line.strip()
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        else:
            x=line.find(':')
            myhour=line[x-2:x]
            wordCount[myhour]=wordCount.get(myhour,0)+1

for k,v in wordCount.items():
    mytuple=(k,v)
    lst1.append(mytuple)
    lst1.sort()
for k,v in lst1:
    print (k,v)
