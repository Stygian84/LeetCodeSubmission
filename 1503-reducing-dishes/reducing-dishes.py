class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
            
        n=len(satisfaction)
        max_satisfaction=0
        current_sum=0
        total=0
        
        for i in range(n-1, -1, -1):
            current_sum += satisfaction[i]
            total += current_sum
            max_satisfaction = max(max_satisfaction, total)
        
        return max_satisfaction