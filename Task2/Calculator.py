#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Simple Calculator with Exit Option

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter the number of the operation you want to perform (or '5' to exit): ")
        
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                # Input numbers
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                # Perform calculation based on choice
                if choice == '1':
                    result = add(num1, num2)
                    operation = "+"
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = "-"
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = "*"
                elif choice == '4':
                    result = divide(num1, num2)
                    operation = "/"
                
                # Display result
                print(f"\nResult: {num1} {operation} {num2} = {result}")
            
            except ValueError:
                print("Invalid input: Please enter numerical values.")
        else:
            print("Invalid choice: Please select a valid option.")

if __name__ == "__main__":
    main()



# In[ ]:




