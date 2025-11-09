print('Calculator using Python-Daron Lauray')
#A simple calculator that can be customized for any calculation
value= input(' what do you want to do?: +,-,*,^ or /')

a= int(input('first number'))
b= int(input('second number'))

atot= float(a+b)
stot= float(a-b)
mtot= float(a*b)
dtot= float(a/b)
exptot= float(a**b)
def add():  
    print(f"answer is {round(atot,2)}")
def subtract():
    print(f"answer is {round(stot,2)}")
def multiply():
    print(f"answer is {round(mtot,2)}")
def divide():
    print(f"answer is {round(dtot,2)}")
def exp():
    print(f"answer is {round(exptot,2)}")
if value == "+":
    add()
elif value == "-":
    subtract()
elif value == "*":
    multiply()
elif value == "/":
    divide()
elif value == "^":
    exp()
else: print('input the function without spaces, and only input the mode symbol')
