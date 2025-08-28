# wrapping data and function into a single unit(object)

# problem1: create account class with 2 attributes balance and account no
# create methods for debit,credit and printing the balance


class Account:
    # data (state)
    def __init__(self,balance,accountNo):
        self.balance=balance
        self.accountNo=accountNo
    # methond (behavior)
    def debitBalance(self):
        amount = int(input("Enter balance to debit: "))

        if amount > self.balance:  # prevent overdraft
            print("❌ Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Rs {amount} was debited")
            print(f"Total balance remaining: {self.balance}")
        # methond (behavior)

    def credigBalance(self):
        amount = int(input("enter a amount to credit"))
        self.balance+=amount
        print(f"RS amount{amount} was credited")
        print(f"total balance remaining was{self.balance}")
            # methond (behavior)

    def checkBalance(self):
        print("your total balance was",self.balance)


accountObj = Account(500,123)
while True:
    print("\n----- MENU -----")
    print("1. Debit")
    print("2. Credit")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("enter your choice"))
    match choice:
      case 1:
        accountObj.debitBalance()
      case 2:
        accountObj.credigBalance()
      case 3:
        accountObj.checkBalance()
      case 4:
        print("Exiting... ✅")
        break
      case _:
        print("❌ Invalid choice! Please try again.")
 