class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance
        
    def valid(self, num) -> bool:
        return num < len(self.accounts)


    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1 -= 1
        account2 -= 1
        if not self.valid(account1) or not self.valid(account2):
            return False
        if self.accounts[account1] < money:
            return False
        
        self.accounts[account1] -= money
        self.accounts[account2] += money
        return True
        

    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        if not self.valid(account):
            return False
        self.accounts[account] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        if not self.valid(account):
            return False
        if self.accounts[account] < money:
            return False
        self.accounts[account] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
