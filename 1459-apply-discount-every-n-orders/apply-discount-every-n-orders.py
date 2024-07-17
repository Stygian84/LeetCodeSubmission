class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.table = {}
        self.counter = 1
        for a,b in zip(products,prices):
            self.table[a]=b        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        
        bill = 0
        for a,b in zip(product,amount):
            bill += self.table[a]*b
        
        if self.counter == self.n:
            bill*= (100-self.discount)/100
            self.counter = 1
        else:
            self.counter+=1
        return bill

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)