class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        count=1
        total=0
        for item in cost:
            if count==3:
                count=1
                continue
            total+=item
            count+=1
        return total