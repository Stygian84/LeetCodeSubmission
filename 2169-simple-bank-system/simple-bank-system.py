class Bank:

    def __init__(self, balance: List[int]):
        self.balance = [0]+balance
        self.length = len(balance)
        print(self.balance,self.length)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        
        if (1<=account1<=self.length and 1<=account2<=self.length  
            and money<=self.balance[account1]):

            self.balance[account2]+=money
            self.balance[account1]-=money
            return True
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        if 1<=account<=self.length:
            self.balance[account]+=money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 1<=account<=self.length and money<=self.balance[account]:
            self.balance[account]-=money
            return True
        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)