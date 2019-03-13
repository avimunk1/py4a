#3.3 Write a program to prompt for a score between 0.0 and 1.0. 
#If the score is out of range, print an error. 
#If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. 
#For the test, enter a score of 0.85.



myscore='Invlid Input'
score=input('enter score: ')

try:
    float(score)*1
except:
    print('enter valid score between 0.0 and 1.0')
    exit()

score=float(score)

if 0.9<=score<=1.0: myscore='A'
elif 0.8<=score<0.9: myscore='B'
elif 0.7<=score<0.8: myscore='C'
elif 0.6<=score<0.7: myscore='D'
elif 0.0<=score<0.6: myscore='F'
elif score > 1.0: myscore='invlid score score should be less than 1.0'
elif score < 0.0: myscore='invlid score score should be more than 0.0'    
print(myscore)

