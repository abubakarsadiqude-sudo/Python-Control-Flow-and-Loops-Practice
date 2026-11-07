#41.	Find the least common multiple (LCM) of two positive integers without importing a module.
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
lcm=int()
if a>b:
    lcm=a
else:
    lcm=b
for i in range(lcm , (a*b)+1):
    if i%a==0 and i%b==0:
        lcm=i 
        break
print("Lcm = " , lcm)
