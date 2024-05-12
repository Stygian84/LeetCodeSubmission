class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        for item in accounts:
            if (sum(item)>max_wealth):
                max_wealth=sum(item)
        return max_wealth
