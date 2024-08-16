class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        
        odd_part = self.beautifulArray(math.ceil(n / 2))
        even_part = self.beautifulArray(math.floor(n / 2))
        
        result = []
        
        for number in odd_part:
            result.append(2 * number - 1)  
        
        for number in even_part:
            result.append(2 * number)      
        
        return result