# register
# - username, email, password
# = generate user account

# login
# = (username or email) and password

# bank operations

import random
import time
import datetime
import sys

database = {}

def init():
    print(" == === == ** WELCOME TO EAZY BANKING ** == === ==\n")
    time.sleep(2)
    print("Do you have an account with us?")
    time.sleep(1.5)
    while True:
        try:
            haveAccount = int(input("1 (yes) \t2 (no) \n"))
            break
        except ValueError:
            print("Oops! That was no valid number. try again...")

    if (haveAccount == 1):
        login()
    elif (haveAccount == 2):
         register()
    else:
        print("Invalid input")
        init()


def login():

    print("***** LOGIN *****\n")

    isloginSuccessful = False

    while isloginSuccessful == False:

        print("Login with your Account number and Password")

        accountNumber_input = int(input("Account Number: "))
        password_input= input("\nPassword: ")

        for accountNumber, userdetails in database.items():
            if (accountNumber == accountNumber_input):
                if (userdetails[3] == password_input):
                    isloginSuccessful = True
                else:
                    print("Invalid Account Number or Password")
    bankOperations(userdetails)

   

def register():

    print("\n***** REGISTER *****\n")

    first_name = input("FIRST NAME: ")
    last_name = input("\nLAST NAME: ")
    email = input("\nEMAIL: ")
    password = input("\nCREATE A PASSWORD: ")
    confirm_password = input("\nCONFIRM PASSWORD: ")

    if (confirm_password != password):
        print("\nPassword does not match!!")
        register()
    else:
        accountNumber = generateAccountNumber()
        accountBalance = generateAccountBalance()

        database[accountNumber] = [ first_name, last_name, email, password, accountBalance]

    print("\nYour Account has been successfully created")
    time.sleep(1)
    print("== === == === == === == ===")
    print("Your account number is {}".format(accountNumber))
    print("== === == === == === == ===\n")
    time.sleep(1)

    login()


def bankOperations(user):
    print("\nWelcome {} {}".format(user[0], user[1]))
    login_time = datetime.datetime.now()
    print (login_time.strftime("\nLogged in : %Y-%m-%d %H:%M:%S\n"))

    print("What action do you want perform: ")
    selectedOption = int(input("1). Withdraw \t2). Deposit \t3). Complaint \t4). Logout \t5). Exit\n"))



    if (selectedOption == 1):
        withdraw(user)
    elif (selectedOption == 2):
        deposit(user)
    elif (selectedOption == 3):
        complaint()
    elif (selectedOption == 4):
        logout()
    else:
        exit()


def withdraw(user):
    print("***** WITHDRAWAL *****\n")
    
    print("Your current balance is ${}".format(user[4]))
    time.sleep(2)
    withdraw = int(input("How much would you like to withdraw: "))
    if withdraw > user[4]:
        print("Insufficient Fund")
    else:	
        print("Take your cash")
        time.sleep(2)
        new_balance = user[4] - withdraw
        print("Your new balance is ${}".format(new_balance))
    time.sleep(1.5)
    print("Do you want to perform another action?")
    
    while True:
        try:
            anotherAction = int(input("1 (yes) \t2 (no) \n"))
            break
        except ValueError:
            print("Oops! That was no valid number. try again...")


    if (anotherAction == 1):
        bankOperations(user)
    elif (anotherAction == 2):
         exit()
    else:
        print("Invalid input")



def deposit(user):
    print("***** DEPOSIT *****\n")

    print("Your current balance is ${}".format(user[4]))
    time.sleep(2)
    deposit = int(input("How much would you like to deposit? "))
    print("Transaction successful!")
    time.sleep(2)
    new_balance = user[4] + deposit
    print("Your new balance is ${}".format(new_balance))
    time.sleep(1.5)
    print("Do you want to perform another action?")
    
    while True:
        try:
            anotherAction = int(input("1 (yes) \t2 (no) \n"))
            break
        except ValueError:
            print("Oops! That was no valid number. try again...")


    if (anotherAction == 1):
        bankOperations(user)
    elif (anotherAction == 2):
         exit()
    else:
        print("Invalid input")

def complaint():
    print("\n***** COMPLAINT *****\n")

    input("What issue will you like to report? \n")
    time.sleep(1.5)
    print("Thank you for contacting us")
    time.sleep(1)
    print("Do you want to perform another action?")
    while True:
        try:
            anotherAction = int(input("1 (yes) \t2 (no) \n"))
            break
        except ValueError:
            print("Oops! That was no valid number. try again...")

    if (anotherAction == 1):
        bankOperations(user)
    elif (anotherAction == 2):
         exit()
    else:
        print("Invalid input")


def logout():
    print("Logging out...\n")
    time.sleep(3)
    login()


def exit():
    sys.exit("Thank you for banking with us")  


def generateAccountNumber():
     return random.randrange(1111111111, 9999999999)


def generateAccountBalance():
    return random.randrange(1111, 9999)




init()