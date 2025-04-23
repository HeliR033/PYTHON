def grades(x):
    if 0<=x<=39:
        return 'Grade:Fail'
    elif 40<=x<=44:
        return 'Grade:Pass'
    elif 45<=x<=49:
        return 'Grade: C'
    elif 50<=x<=54:
        return 'Grade: B'
    elif 55<=x<=59:
        return 'Grade: B+'
    elif 60<=x<=69:
        return 'Grade: A'
    elif 70<=x<=79:
        return 'Grade: A+'
    elif 80<=x<=100:
        return 'Grade: O'
    else:
        return "NA"
x = int(input("Enter grades of Math:"))
y = int(input("Enter grades of Computer:"))
z = int(input("Enter grades of Physics:"))
print("total:",x+y+z)
print("Average:",x+y+z/3)
print("Math",grades(x))
print("Computer",grades(y))
print("Physics",grades(z))
