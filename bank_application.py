account_no = 0
cusname = ""
bcode = 0
mobile = 0
bal = 0

def createAccount():
    global account_no,cusname,bcode,mobile,bal
    account_no = int(input("Enter acount number: "))
    cusname = input("Enter customer name: ")
    bcode = int(input("Enter branch code: "))
    mobile = int(input("Enter mobile number: "))
    bal = int(input("Enter balance: "))

def showAccount():
    print("Account number: ", account_no)
    print("Customer name: ", cusname)
    print("Branch code: ", bcode)
    print("Mobile number: ", mobile)

def withdraw(amount):
    global bal
    bal = bal - amount

    return bal

def deposit(amount):
    global bal
    bal = bal + amount

    return bal

def chckBalance():
    global bal
    print("Balance: ", bal)

# main
ch1 = 'y'
while ch1 == 'y':
    print("1. Create account")
    print("2. Show account")
    print("3. Withdraw")
    print("4. Deposit")
    print("5. Check Balance")
    ch = int(input("Select any option: "))

    if ch == 1:
        createAccount()
    elif ch == 2:
        showAccount()
    elif ch == 3:
        wd = int(input("Enter amount to withdraw: "))
        print("Total: ", withdraw(wd))
    elif ch == 4:
        depo = int(input("Enter amount to deposit: "))
        print("Total :", deposit(depo))
    elif ch == 5:
        chckBalance()
    else:
        print("Please select any 4 options available above")

    ch1 = input("do you want to continue...... press y: ")