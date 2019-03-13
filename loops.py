
# this for loops will print the largest number in an a list

theGreater=0


for i in [9,2,3,31,45]:
	print(i)
	if i>theGreater:
		theGreater=i
		

print('this is the largest '+str(theGreater))