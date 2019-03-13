
# a function that recived the user input and caculate salery includin 150%


def computepay(h,r):
	overTime=0
	salery=0
	h=int(h)
	r=float(r)
	if (h)>40:
		overTime=h-40
	salery=(h-overTime)*r+(overTime*r*1.5)
	
	return salery

hrs = input("Enter Hours:")
rate= input('please enter rate per hour')
p = computepay(hrs,10.5)
print('your salary will be '+str(p)+'$')


