class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas=sum(gas)
        sum_cost=sum(cost)
        if (sum_cost>sum_gas):
            return -1
        total = 0 
        res = 0    
        
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1
        
        return res