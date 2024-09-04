#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string

def generate_password(length, complexity):
    """Generate a random password based on length and complexity."""
    if complexity == '1':
        # Simple: Lowercase letters only
        characters = string.ascii_lowercase
    elif complexity == '2':
        # Medium: Lowercase and uppercase letters
        characters = string.ascii_letters
    elif complexity == '3':
        # Strong: Lowercase, uppercase, digits
        characters = string.ascii_letters + string.digits
    elif complexity == '4':
        # Very strong: Lowercase, uppercase, digits, special characters
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level"

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")

    try:
        # Input length and complexity
        length = int(input("Enter the desired length of the password: "))
        
        print("\nChoose the complexity level:")
        print("1. Simple (Lowercase letters only)")
        print("2. Medium (Lowercase and Uppercase letters)")
        print("3. Strong (Lowercase, Uppercase, and Digits)")
        print("4. Very Strong (Lowercase, Uppercase, Digits, and Special Characters)")

        complexity = input("Enter the number of the complexity level: ")

        # Generate and display password
        password = generate_password(length, complexity)
        
        if password.startswith("Invalid"):
            print(password)
        else:
            print(f"\nGenerated Password: {password}")
    
    except ValueError:
        print("Invalid input: Please enter a numerical value for the length.")

if __name__ == "__main__":
    main()


# 
