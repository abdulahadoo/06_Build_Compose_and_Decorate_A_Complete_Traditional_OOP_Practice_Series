class Bank:
    bank_name =  "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder :{self.account_holder},Bank :{Bank.bank_name}")  

user1 = Bank("AD")
user2 = Bank("Pagal") 

user1.display()
user2.display()

Bank.change_bank_name("World Bank")


user1.display()
user2.display()

