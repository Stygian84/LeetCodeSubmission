class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_count = [0] * 121  
        for age in ages:
            age_count[age] += 1
        
        res = 0
        
        for a in range(1, 121):
            count_a = age_count[a]
            for b in range(1, 121):
                count_b = age_count[b]
                
                if a * 0.5 + 7 >= b:
                    continue  
                if a < b:
                    continue  
                
                res += count_a * count_b
                
                if a == b:
                    res -= count_a
        
        return res