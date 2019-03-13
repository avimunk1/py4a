#When you encounter a line that starts with “X-DSPAM-Confidence
#count the rows and sum the spam Confidence to get an everage

fileH=''
count=0
line=''
spamCon=0
Average=-1

fileH=input('Please type the file name:  ')
try:

    fileH=open(fileH)

except:
    print('no such file')
    exit()


for line in fileH:

    if 'X-DSPAM-Confidence:' not in line:
        #print('skipped')
        continue
    if line.find('0.')>-1:
        #print('st1')
        x=line.find('X-DSPAM-Confidence:')
        y=line.find('0.',x)

        spamCon=float(spamCon)+float(line[y:y+7])
        count=count+1
        #print(count,spamCon)
    if line.find('1.')>-1:
        #print('step2')
        x=line.find('X-DSPAM-Confidence:')
        y=line.find('1',x)
        #print(x,y)
        spamCon=float(spamCon)+float(line[y:y+7])
        count=count+1
try:
    Average=spamCon/count

except:
    print('general error',spamCon,count)
    exit()

print('Average spam confidence:',round(Average,12))
