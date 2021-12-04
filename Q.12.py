write a python program to check whether the triangle is equilateral,isosceles or scalene triangle
x= int(input("enter the number"))
y =int(input("enter the number"))
z= int(input("enter the number"))
if x==y==z:
    print("equilaterial")
elif x==y or z==x or y==z:
    print("isoseles")
else:
    print("scalene")   