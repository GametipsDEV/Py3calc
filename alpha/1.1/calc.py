import math
# this is the selection code! codename part SELECT
select = input('''Please select what function you want to use
+ for Addition
- for Subtraction
/ for Devision
* for Multiplication
SQRT for squareroot please change second number to zero
HYPO for hypotenuse solver
Here : ''') 

#this is were the user input's the numbers
NUM1 = input("Please put first number here : ")
NUM2 = input("Please put second number here : ")

#all results are calculated here because if it's in the "if" part's the program will not 

#run codename part CALC

#addition
def add():
 ADD3 = float(NUM1) + float(NUM2)
 print (ADD3)




#subtraction
def sub():
 SUB3 = float(NUM1) - float(NUM2)
 print (SUB3)




#devition
def dev():
 DEV3 = float(NUM1) / float(NUM2)
 print (DEV3)




#multiplication
def mul():
 MUL3 = float(NUM1) * float(NUM2)
 print (MUL3)




#SQRT
def sqrt():
 SQRT = math.sqrt(float(NUM1))
 print (SQRT)




#HYPO
def hypo():
 HYPO1 = float(NUM1) ** 2
 HYPO2 = float(NUM2) ** 2
 HYPO3 = float(HYPO1) + float(HYPO2)
 HYPO4 = math.sqrt(float(HYPO3))
 print (HYPO4)



#this is the if part for addition it calls the function. codename part A
if select == '+':

 add()

#this is the subtraction part always just print's the result. codename part S
if select == '-':

 sub()

#codename part D
if select == '/':

 dev()

#codename part M
if select == '*':

 mul()

#codename part SQRT
if select == 'SQRT':
 
 sqrt()

#codename part HYPO
if select == 'HYPO':
 
 hypo()
