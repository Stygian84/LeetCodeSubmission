class ProductOfNumbers:

    def __init__(self):
        self.product = [1]

    def add(self, num: int) -> None:
        if self.product[-1]==0:
            self.product = [0] * len(self.product)
            self.product.append(num)
        else:
            self.product.append(self.product[-1]*num)
        #print(self.product)

    def getProduct(self, k: int) -> int:
        if self.product[-k]!=0 and self.product[-k-1]==0:
            return self.product[-1]
        if self.product[-k-1]==0:
            return 0
        return self.product[-1] // self.product[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)