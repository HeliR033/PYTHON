l = int(input("Enter length of triangle:"))
b = int(input("Enter breath of traingle:"))
p = 2*(l+b)
a = l*b
if a>p:
    print("Area is greater than perimeter.")
else:
    print("Perimeter is greater than area.")
