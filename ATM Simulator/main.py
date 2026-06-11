Balance = 0

def CheckBalance():
    print(f"Your Balance is: {Balance}")


def deposit():
    global Balance
    amount = int(input("Enter your amount: "))
    Balance = Balance + amount
    print(f"Your Balance is Deposit in your Account!!")


def withdraw():
    global Balance
    amount = int(input("Enter your Amount: "))
    if amount > Balance:
        print("Insufficient Balance!")
    else:
        Balance = Balance - amount
        print("Successfully Withdrawn!")



while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    menu = int(input("\nWhat do you Want: "))

    if menu == 1:
        CheckBalance()
    elif menu == 2:
        deposit()
    elif menu == 3:
        withdraw()
    elif menu == 4:
        print("Thankyouu For using Shraddha's ATM!")
        break