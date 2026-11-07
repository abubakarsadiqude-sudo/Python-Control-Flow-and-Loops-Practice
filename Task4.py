#36.	Generate the Fibonacci sequence up to N terms using a loop.
a=int(0)
b=int(1)
number=int(input("Enter a number : "))
for i in range(0,number+1):
    print(a," ")
    c=int(a+b)
    a=b
    b=c
