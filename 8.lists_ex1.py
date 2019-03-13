#prompt the user for value, if its a number add it to the list,
#if not prompt for a number

numberList=list()


while True:
    userNnumber=input('plesase emter a number: ')
    if userNnumber=='done':break
    try:
        int(userNnumber)*3
    except:
        print('enter numbers only')
        continue

    userNnumber=int(userNnumber)
    numberList.append(userNnumber)

    numberList[len(numberList)-2]=12
    print(numberList,sum(numberList))
