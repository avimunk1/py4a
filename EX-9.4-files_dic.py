

inputFile='mbox-short.txt'


try:
    fileH=open(inputFile)
except:
    print('no such file '+inputFile)
    exit()

fileH=open(inputFile)

senders=dict()
prevWord='notFrom'

for line in fileH:
    line=line.strip()
    mywords=line.split()
    #print(mywords)
    for Aword in mywords:
        if prevWord.lower()=='from:':
            if Aword not in senders:
                senders[Aword]=1
                #print(Aword)
            else:
                senders[Aword]=senders[Aword]+1
        prevWord=Aword

winner=None

for Value in senders:
    currentv=senders.get(Value)

    if winner==None:
        winner=Value
    if currentv>senders.get(winner):
        winner=Value

print(winner,senders.get(winner))








#print('===')
