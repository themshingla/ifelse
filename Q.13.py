write a python program to calculate profite or loss
cp =int (input ("enter the cost price"))
sp = int (input ("enter the selling price"))
if(sp>cp):
    # amount=sp+cp
    print=("the profit ")
elif (sp<cp):
    # amount=sp-cp
    print("the loss ")
else:
    print ("no loss no profit")

if cp>sp:
    amount=cp-sp
    print("loss",amount,"rs")
elif sp>cp:
    amount=sp+cp
    print("profit",amount,"rs") 
else:
    print("no profit no loss")

take three user input two for number and for symbol and make in using if else.
num1=int (input("enter the number"))
num2=int(input("enter the number"))
ch=input("enter the any symbol")
if ch=="+":
    print(num1+num2)
elif ch=="*":
    print(num2*num1)
elif ch=="-":
    print(num1-num2)
else:
    print("nothing")

num1=int(input ("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
if num1>num2 and num1>num3:
    print(num1,"num1 is max")
elif num2>num1 and num2>num3:
    print(num2,"num2 is max")
elif num3>num1 and num3>num2:
    print(num3,"num3 is max")
else:
    print("invalid condition")

varx=int (input('enter the number'))
if varx%5==0 and varx%15==0:
    print ("divisible by 5 and15")
else:
    ("not divisible")
    
    