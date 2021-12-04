#A shop will give a discount of 10% if  the co
# st of the purchased quantity is more tham 1000.
# ask the user for quantity, suppose,one unit will cost 100.judqe and print total cost for user.
# quantity =int (input ("enter the number"))
# cost=quantity*100
user=int(input("enter purchased quantity"))
if user>1000:
    discount=user*10/100
    print(discount,"is your discount")
else:
    print("no discount")