#3.1 Write a program to prompt the user for hours and rate per hour using input
# to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate 
#for all hours worked above 40 hours. 
#Use 45 hours and a rate of 10.50 per hour to test the program
# (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input - assume the user types numbers properly.


rate=0
totalHours=0
stdHours=40
extraHours=0
pay=0
error=False

rate=input('enter rate: ')
try:
    float(rate)*10
except:
    print('enter valid rate in format XX.0')
    error=True

totalHours=input('enter hours :')
try:
    int(totalHours)*1
except:
    print('enter valid hours')
    error=True

if not error:
    totalHours=float(totalHours)
    rate=float(rate)
    extraHours=(totalHours-stdHours)
    pay=(stdHours*rate) + (extraHours*rate*1.5)
    print(pay)

elif error:
    print('one or more inputs are invalid')




