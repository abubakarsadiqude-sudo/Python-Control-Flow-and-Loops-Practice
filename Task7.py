#39.	Print a number pattern where row 1 contains 1, row 2 contains 1 2, row 3 contains 1 2 3, continuing up to N rows.
number = int(input("Enter the number of rows : "))
for i in range(0,number):
    for j in range(0 , i+1):
        print(j+1 , end="")
    print()
  
