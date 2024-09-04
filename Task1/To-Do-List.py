#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import datetime

# Connect to SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY,
                    date TEXT,
                    type TEXT,
                    category TEXT,
                    amount REAL,
                    description TEXT
                )''')

def add_transaction(transaction_type):
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input(f"Enter the {transaction_type} category: ")
    amount = float(input(f"Enter the {transaction_type} amount: "))
    description = input(f"Enter a description (optional): ")

    cursor.execute('''INSERT INTO transactions (date, type, category, amount, description)
                      VALUES (?, ?, ?, ?, ?)''', (date, transaction_type, category, amount, description))
    conn.commit()
    print(f"{transaction_type.capitalize()} added successfully!")

def view_transactions():
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Date: {row[1]}, Type: {row[2]}, Category: {row[3]}, Amount: {row[4]}, Description: {row[5]}")

def view_summary():
    cursor.execute("SELECT type, SUM(amount) FROM transactions GROUP BY type")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Type: {row[0]}, Total Amount: {row[1]}")

def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_transaction('income')
        elif choice == '2':
            add_transaction('expense')
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            view_summary()
        elif choice == '5':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()


# In[ ]:




