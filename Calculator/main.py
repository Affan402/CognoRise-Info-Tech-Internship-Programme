def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an Operation: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        choice = int(input("Enter your choice (1/2/3/4): "))
        
        if choice in [1, 2, 3, 4]:
            try:
                num1 = float(input("Enter First Number: "))
                num2 = float(input("Enter Seecond Number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue
            
            if choice == 1:
                result = num1 + num2
                operator = "+"
            elif choice == 2:
                result = num1 - num2
                operator = "-"
            elif choice == 3:
                result = num1 * num2
                operator = "*"
            elif choice == 4:
                if num2 != 0:
                    result = num1 / num2
                    operator = "/"        
                else:
                    print("Error: Division by zero is not allowed")
                    continue
            print(f"{num1} {operator} {num2} = {result}")
            break
        else:
            print("Invalid choice! Please select a valid operation.") 
            

calculator()                                                                                
