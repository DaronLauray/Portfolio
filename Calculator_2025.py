print('Calculator using Python-Daron Lauray')
#A simple calculator that can be customized for any calculation
import sys
import math
#sys.maxsize
sys.set_int_max_str_digits(100000000)

value=0
while value != "done":
    value= input(' what do you want to do?: +,-,*,^,/ or done')
    
    def add():  
        print(f"answer is {(round(atot,2))}")
    def subtract():
        print(f"answer is {(round(stot,2))}")
    def multiply():
        print(f"answer is {(round(mtot,2))}")
    def divide():
        print(f"answer is {(round(dtot,2))}")
    def exp():
        print(f"answer is {(round(exptot,2))}")

 
    a= int(input('first number'))
    b= int(input('second number'))

    atot= int(a+b)
    stot= int(a-b)
    mtot= int(a*b)
    dtot= int(a/b)
    exptot= int(a**b)

   

   
    if value == "+":
        add()
    elif value == "-":
        subtract()
        
    elif value== "*":
        multiply()
        
    elif value == "/":
        divide()
        
    elif value == "^":
        exp()
    
    else: print('input the function without spaces, and only input the mode symbol')
    