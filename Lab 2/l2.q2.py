#largest and smallest value out of three
x=int(input("Enter an integer:"))
y=int(input("Enter another integer:"))
z=int(input("Enter another integer:"))
if x>y and x>z:
    print("Largest number:",x)
elif y>x and y>z:
    print("Largest number:",y)
else:
    print("Largest number:",z)

if x<y and x<z:
    print("Smallest number:",x)
elif y<x and y<z:
    print("Smallest number:",y)
else:
    print("Smallest number:",z)
