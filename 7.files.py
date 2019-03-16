#this progrme will open a file and will print only lines that
#meet with some critiria

fileH=''
count=0
line=''
mylines=list()

fileH=open('inputs'+"/mbox-short.txt")

print('this is my list')
print('=============')

for line in fileH:
    if '@uct.ac.za' not in line:
        continue
    line=line.strip()
    count=count+1
    mylines.append(line)


print('=============')
print('this is the no of rows '+str(count))
print('these are the rows that met with the condition',mylines)
