#33.	Create a menu-driven program that repeatedly offers: check even/odd, calculate square, calculate cube, or exit. Use a loop and conditional statements.
while True:
    print("====== Menu ======")
    print("1. Check Even Odd number.")
    print("2. Calculate square. ")
    print("3. Calculate Cube.")
    print("4.Exit the program")
    choice=int(input("Enter your choice : "))
    if choice==1:
        number=int(input("Enter a number : "))
        if number % 2 == 0:
            print(number, "is an even number.")
        else:
            print(number , "is an odd number.")
    elif choice == 2:
        number=int(input("Enter a number : "))
        print("Square of number is " , number*number)
    elif choice==3:
        num=int(input("Enter a number : "))
        print("Cube of number is " , num*num*num)
    elif choice==4:
        exit()
    else:
        print("Invalid choice .")
           