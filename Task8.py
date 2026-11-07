a=int(input("Enter first number : "))
b=int(input("Enter second number: "))
limit=int()
if a < b:
    limit=a
else:
    limit=b
gcd = 1
for i in range(1,limit+1):
    if a%i==0 and b%i==0:
        gcd=i
print("GCD = ", gcd)
