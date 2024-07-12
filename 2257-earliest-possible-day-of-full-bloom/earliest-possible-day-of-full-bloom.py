class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        seeds = sorted(zip(growTime, plantTime), reverse=True)
        
        current_day = 0  
        max_bloom_day = 0 
        
        for grow, plant in seeds:
            current_day += plant  
            max_bloom_day = max(max_bloom_day, current_day + grow)  
        return max_bloom_day