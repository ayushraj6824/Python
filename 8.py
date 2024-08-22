class Account:
    def __init__(self,bal,acc) -> None:
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance =self.balance-amount
        print("Rs.",amount,"was debited")
        print("total balance= ",self.get_balance())

    def credit(self,amount):
        self.balance =self.balance + amount
        print("Rs.",amount,"was credited")
        print("total balance= ",self.get_balance())

    def get_balance(self):
        return self.balance


acc1=Account(10000,123456)
acc1.debit(198)
acc1.credit(677)
