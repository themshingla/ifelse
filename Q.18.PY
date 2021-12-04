phy =int(input("enter the phy mark"))
chem=int(input("enter the chem mark"))
bio=int(input("enter the bio mark"))
maths=int(input("enter the maths mark"))
comp=int(input("enter the comp mark"))
total =phy+chem+bio+maths+comp
per=total/5
if per>=90:
    print("grade a")
elif per>=80:
    print("grade b")
elif per>=70:
    print("grade c ")
elif per>=60:
    print("grade d")
elif per>=40:
    print("grade e")
else:
    print("grade f")

