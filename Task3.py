#	Print all prime numbers between 2 and N. Do not use external libraries.
num=int(input("Enter a number : "))
count=int(0)
for i in range(2,num+1):
    count=int(0)
    for n in range(1,i+1) :
        if i % n == 0:
            count=count+1
    if count==2:
        print(i , " ")

