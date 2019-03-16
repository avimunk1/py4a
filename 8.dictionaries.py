#this will create a new dictuinery, will add new names to it and count


dicCountnames=dict()

names=open('inputnames.txt')


for name in names:
    name=name.strip()
    if len(name)<2:
        continue

    if name not in dicCountnames:
        dicCountnames[name]=1
    else:
        dicCountnames[name]=dicCountnames[name]+1


print(dicCountnames)
