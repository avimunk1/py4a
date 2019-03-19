#8.4 Open the file romeo.txt and read it line by line. For each line,
#split the line into a list of words using the split() method.
#The program should build a list of words. For each word on each line
#check to see if the word is already in the list and if not append it to the list. When the program completes,
#sort and print the resulting words in alphabetical order.

fileH=open('inputs/'+"romeo.txt")
word=list()

for line in fileH:
    line=line.strip()
    mywords=line.split()
    for Aword in mywords:
        if Aword not in word:
            word.append(Aword)
        else:
            continue

word.sort()
print(word)
#print('===')
