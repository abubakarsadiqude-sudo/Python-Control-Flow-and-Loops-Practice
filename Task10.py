number=int(input("Enter a number : "))
org=int(number)
arm=int(0)
while(number>0):
    digit=int(number%10)
    arm=arm+(digit*digit*digit)
    number //= 10
if arm==org:
    print(org , " is a arm strong number .")
else:
    print(org , " is not a arm strong number")