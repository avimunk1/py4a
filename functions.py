
# this function calculate salery based of no of hours and rate per hour
def slrCalac(hours,rate):
		mypay=int(hours)*int(rate)
		return(mypay)

# this function will get the user input and make sure it's numeric
def MyInput(myMessage):
		myReturn=input(myMessage+' ')
		
		if not str.isnumeric(myReturn):
			myMessage='please enter a valid numeric value'
			myReturn=MyInput(myMessage)

		return(myReturn)


myMessage='type your rate per hour'
myRate=MyInput(myMessage)


myMessage='type no of hours'
myHours=MyInput(myMessage)


mySalery=slrCalac(myHours,myRate)
print('-----------------------------')
print('your hour rate is ' +myRate)
print('you worked ' +myHours +' hours this month')
print('your salary this mont will be '+ str(mySalery))
print('-----------------------------')




