class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dc = Counter(answers)

        total = 0
        for c in dc:          
            if dc[c]<c:
                total += 1+c
            else:
                group = math.ceil(dc[c]/(c+1))
                total += group*(c+1)
        
        
            
            
        return total
        