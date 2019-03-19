#9.4 Write a program to read through the mbox-short.txt and
#figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines
#as the person who sent the mail. The program creates a Python dictionary
#that maps the sender's mail address to a count of the number of times they
#appear in the file. After the dictionary is produced, the program reads
#through the dictionary using a maximum loop to find the most prolific committer.

inputFile="mbox-short.txt"

try:
    fileH=open('inputs/'+inputFile)
except:
    print('no such file'+inputFile)
    exit()

fileH=open('inputs/'+inputFile)

senders=list()
prevWord='notFrom'
for line in fileH:
    line=line.strip()
    mywords=line.split()
    for Aword in mywords:
        if Aword not in senders:
            if prevWord.lower()=='from':
                senders.append(Aword)
        prevWord=Aword


print(senders)
#print('===')
