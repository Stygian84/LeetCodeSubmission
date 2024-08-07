class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        res = math.inf
        minimum = math.inf
        n = len(toppingCosts)

        def backtrack(topping,total,start):
            nonlocal minimum,res,target
            
            if abs(total-target)<=minimum:
                minimum = abs(total-target)
                if abs(res-target) == minimum:
                    res=min(res,total)
                else:
                    res = total

            if start == n:
                return

            for i in range(start,len(toppingCosts)):
                t = toppingCosts[i]
                backtrack(topping,total,i+1)
                if i not in topping:
                    topping.add(i)
                    backtrack(topping,total+t,i+1)
                    backtrack(topping,total+t*2,i+1)
                    topping.remove(i)

        for b in baseCosts:
            backtrack(set(),b,0)

        return res