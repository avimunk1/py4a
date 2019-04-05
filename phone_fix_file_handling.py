#open the input file
#read the first line into list
#add the members into fileds
#open a new file for writing write the first line
#write the first line to the new file

inputFile="input_sample_2.csv"
outPutFile="fixedCustomersList.txt"

try:
    fileH=open('inputs/'+inputFile)
except:
    print('no such file'+inputFile)
    exit()

fileH=open('inputs/'+inputFile)
outFilH=open(outPutFile,"w+")

fileLine=list()
ExtId=''
FirstName=''
LastName=''
MobilePhone=''
AltPhone=''
newMobilePhone=''
newPhoneSatus=''
outFilH=open(outPutFile,"w+")
for line in fileH:
    fileLine=line.split(',')
    ExtId=fileLine[0]
    FirstName=fileLine[1]
    LastName=fileLine[2]
    MobilePhone=fileLine[3]
    AltPhone=fileLine[4]
    print(ExtId,FirstName,LastName,MobilePhone,AltPhone)
    outFilH.write(ExtId+',')
    outFilH.write(FirstName+',')
    outFilH.write(LastName+',')
    outFilH.write(MobilePhone+',')
    outFilH.write(LastName+'\n')
outFilH.close()
