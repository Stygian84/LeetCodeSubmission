class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort(reverse=True)
        count=0
        while True and costs:
            current=costs.pop()
            if coins-current<0:
                break
            else:
                coins-=current
                count+=1
        return count