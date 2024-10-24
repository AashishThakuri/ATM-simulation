import datetime
balance = 10000
password = 1234

def current_balance():
    current_time = datetime.datetime.now()
    print(current_time) 
    print(f"your current balance is RS.{balance}")

def deposit():
    global balance
    n = float(input("Enter amount to deposit:"))
    if(n !=0):
        confirm = input(f"Do you want to confirm {n}: (yes/no;)")
    if(confirm=="yes"):
        balance += n
        print("Deposited successfully")
    elif(confirm=="no"):
        print(n)
    else:
        print("Transcation Cancelled")
        
def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw"))
    if(amount<=balance):
        balance -=amount
        print(f" RS.{amount} withdrawn successfully")
        print("Thank you for using Our ATM, Happy Nice Day Nigga")
        return True
    elif(amount>balance):
        print("Insufficient balance!")


def change_password():
    current_password = int(input("Enter your current password"))
    if(current_password==password):
        New_password = int(input("Enter your new password:"))
        confirm = input(f"Do you want to confirm:(yes/no)")
    if(confirm == "yes"):
        password ==New_password
        print("password changes successfully")
    elif(confirm =="no"):
        print("Your password is unchanged")
    else:
        print("Something went wrong")                      
    
        
        
def ATM():
    while True:
        Enter_password = int(input("Enter your password"))
        if(Enter_password == password):
            print("Access Granted")
            break
        else:
            print("Incorrect password")
            
            
    while True:        
        print("\n--- ATM MENU ---")
        print("1. Current Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change_Password")
        print("5. Exit")
        
        choice = input("Choose an option (1-5):")
        if(choice=='1'):
         current_balance()
        elif(choice=='2'):
          deposit()
        elif(choice=='3'):
         withdraw()
         break
        elif(choice =="4"):
            change_password()
        elif(choice=='5'):
          print("Thank you for using Our ATM, Happy Nice Day Nigga")
          break
        else:
          print("Invalid Option")
      

ATM()

 
 

    



