x1 = int(input("give x coordinate for the centre of circle:"))
y1 = int(input("give y coordinate for the centre of circle:"))
r = int(input("radius:"))
x2 = int(input("give x coordinate for the point of circle:"))
y2 = int(input("give y coordinate for the point of circle:"))
pc = sqrt(pow(x2-x1,2)+pow(y2-y1,2))
if pc>r:
    print("point lies outside the circle")
elif pc==r:
    print("point lies on the circle")
else:
    print("point lies inside the circle:")
