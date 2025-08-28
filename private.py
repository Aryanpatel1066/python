class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private (via name mangling)

    def get_balance(self):        # public method to access private
        return self.__balance

account = BankAccount(5000)

# print(account.__balance)   # ❌ Error: AttributeError
print(account.get_balance())  # ✅ Correct way

# Trick: still accessible with name mangling
print(account._BankAccount__balance)  # 😬 Works, but not recommended
