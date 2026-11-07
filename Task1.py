#32.	Input three side lengths and determine whether they form a valid triangle. If valid, classify it as equilateral, isosceles, or scalene.
a=float(input("Enter the lenth of side a  : "))
b=float(input("Enter the length of side b : "))
c=float(input("Enter the length of side c : "))
if a+b > c and a+c > b and b+c > a:
    print("The triangle is valid.")
    if a==b==c:
        print("The triangle is equilateral.")
    elif(a==b or b==c or a==c):
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")