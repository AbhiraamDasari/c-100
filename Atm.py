class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Your balance is :-")
        print("NewNotes = 100")
        print("Coins = 200")
        print("notes = 300")

    def withdrawl1(self,NewNotes):
        new_amount = 100 - NewNotes
        print("You have withdrawn amount "+str(NewNotes) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl2(self,Coins):
        new_amount = 200 - Coins
        print("You have withdrawn amount "+str(Coins) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl3(self,notes):
        new_amount = 300 - notes
        print("You have withdrawn amount "+str(notes) + ". Your remaining balance is "+ str(new_amount))        


def main():
    print("Welcome to Central Bank!")
    Account = input("Please enter your acount image or number: ")
    Card_number = input("Insert your key number:- ")
    pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("1. Add NewNotes")
        print("2. Add Coins")
        print("3. Add notes")
        choose = int(input("1. Add NewNotes  2. Add Coins 3. Add notes: "))
        if (choose == 1):
           NewNotes = int(input("Enter the amount:- "))
           new_user.withdrawl1(NewNotes)
        if (choose == 2):
           Coins = int(input("Enter the amount:- "))
           new_user.withdrawl2(Coins)    
        if (choose == 3):
           notes = int(input("Enter the amount:- "))
           new_user.withdrawl3(notes)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()