
# this for loops will print the number of elments in the eray and the largest one

myCounter=0
MyLargest='b'

for i in ['Z','a','b','c','11','11z','z']:
	myCounter=myCounter +1
	if i>MyLargest:
		MyLargest=i

print('the no of elemnts is '+ str(myCounter) +', the largest elemnt is '+ str(MyLargest))

