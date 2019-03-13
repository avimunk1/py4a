
# this for loop will print the average of all items in the arrey


runningSum=None 
CountItems=0
myAverage=0

for i in [-100,200,-300]:
	if runningSum is None:
		runningSum=i

	elif runningSum is not None:
		runningSum=runningSum+i
		CountItems=CountItems+1

myAverage=runningSum/CountItems
print('the averge is ' +str(myAverage))