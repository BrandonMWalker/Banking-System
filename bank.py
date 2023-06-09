import mysql.connector
import sqlite3

# Connect to the database
connection=sqlite3.connect("BMW.db")

# Create a cursor
cursor = connection.cursor()

#When creating the database
cursor.execute("CREATE TABLE IF NOT EXISTS Accounts(name VARCHAR(255),PIN INT, Balance INT,Accountnumber INT)")
connection.commit()

#Check balance function
def check_balance(account_number, pin):
    # Execute SQL query
    query = f"SELECT Balance FROM Accounts WHERE AccountNumber= {account_number} AND PIN={pin}"
    cursor.execute(query)
    result = cursor.fetchone()

    # Print balance
    if result:
        print("Your balance is:", result[0])
    else:
        print("Invalid account number or PIN")

# Deposit function
def deposit(account_number, pin, amount):
    # Execute SQL query
    query = f"UPDATE Accounts SET Balance=Balance + {amount} WHERE AccountNumber={account_number} AND PIN={pin}"
    cursor.execute(query)
    connection.commit()

    print("Deposit successful")

# Withdraw function
def withdraw(account_number, pin, amount):
    # Execute SQL query
    query = f"SELECT Balance FROM Accounts WHERE AccountNumber={account_number} AND PIN={pin}"
    cursor.execute(query)
    result = cursor.fetchone()

    # Check balance and update if sufficient
    if result and result[0] >= amount:
        query = f"UPDATE Accounts SET Balance=Balance-{amount} WHERE AccountNumber={account_number} AND PIN={pin}"
        cursor.execute(query)
        connection.commit()

        print("Withdrawal successful")
    else:
        print("Insufficient balance or invalid account number or PIN")

# Create new account function
def create_account(name, pin, balance, account_number):

    
    # Execute SQL query
    # cursor.execute("INSERT INTO Accounts VALUES('Brandon' ,1234,100, 12)")
    query = f"INSERT INTO Accounts VALUES('{name}' , {pin}, {balance}, {account_number})"
    cursor.execute(query)
    connection.commit()

    print("Account created successfully")

# Close account function
def close_account(account_number):
    # Execute SQL query
    query = f"DELETE FROM Accounts WHERE AccountNumber={account_number}"
    cursor.execute(query)
    connection.commit()

    print("Account closed successfully")

# Modify account function
def modify_account(account_number, name, pin , balance):
    # Execute SQL query
    query = "UPDATE Accounts SET"#first part of query
    values = []
    if name is not None:
        query += f" Name= '{name}',"
        values.append(name)
    if pin is not None:
        query += f" PIN={pin},"
        values.append(pin)

    if balance is not None:

        query += f" Balance={balance}"

    query = query.rstrip(",") + f" WHERE AccountNumber={account_number}" #update an account that has this specific account number
    values.append(account_number)
    cursor.execute(query)
    connection.commit()

    print("Account modified successfully")




#Main script 
if __name__ == "__main__":

    # create_account('BMW' , 1245 , 700 , 1)
    create_account('AAA' , 4444 , 1222  ,5)
    # check_balance(1 , 1245) testing
    # deposit(1 , 1245 , 800) testing
    # withdraw(1 ,1245, 900) testing
    # check_balance(1,1245)
    # modify_account(1 , 'BMW' , 1245 , 840) #test
    # close_account(1)
  
    #Close
    connection.close()


    
    

