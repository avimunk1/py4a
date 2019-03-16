#this will create a new dictuinery, will add new names to it and count


dicCountnames=dict()
countChar=dict()
#names = open('inputs'+"/inputnames.txt")
fpath = ('inputs'+"/inputnames.txt")
#print('names=',names)
#print('fpath=',fpath)
names=open(fpath)


for name in names:
    name=name.strip()
    name=name.lower()
    if len(name)<2:
        continue
    if name not in dicCountnames:
        dicCountnames[name]=1
    else:
        dicCountnames[name]=dicCountnames[name]+1
        for letter in name:
            if letter not in countChar:
                countChar[letter]=1
            else:
                countChar[letter]=countChar[letter]+1

print(countChar)
print(dicCountnames)
