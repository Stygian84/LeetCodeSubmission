class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        res = math.inf
        minimum = math.inf
        n = len(toppingCosts)

        def backtrack(total,start):
            nonlocal minimum,res,target
            
            if abs(total - target) <= minimum:
                if abs(total - target) < minimum or total < res:
                    minimum = abs(total - target)
                    res = total
            
            if start == n or total >= target:
                return

            backtrack(total, start + 1)
            backtrack(total + toppingCosts[start], start + 1)
            backtrack(total + toppingCosts[start] * 2, start + 1)

        for b in baseCosts:
            backtrack(b,0)

        return res