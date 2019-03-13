#this progrme will open a file and will print only lines that
#meet with some critiria

fileH=''
count=0
line=''

fileH=open('mbox-short.txt')

print('this is my list')
print('=============')

for line in fileH:
    if '@uct.ac.za' not in line:
        continue
    line=line.strip()
    count=count+1
    print(line)

print('=============')
print('this is the no of rows '+str(count))

#im making changes
