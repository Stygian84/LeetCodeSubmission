class ProductOfNumbers:

    def __init__(self):
        self.product = []

    def add(self, num: int) -> None:
        if num==0:
            self.product = [0]*(len(self.product)+1)
        
        elif num == 1:
            self.product.append(1)
        
        else:
            for i in range(len(self.product)):
                self.product[i]*=num
            self.product.append(num)

    def getProduct(self, k: int) -> int:
        return self.product[-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)