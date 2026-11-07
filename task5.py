#37.	Print the following right-angled star pattern for a user-entered number of rows: * on the first row, ** on the second, and so on
number = int (input("Enter the number of rows : "))
for i in range(0,number+1):
    for j in range(0,i):
          print("*", end="")
    print()