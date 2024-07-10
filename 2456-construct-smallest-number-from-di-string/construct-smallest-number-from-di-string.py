class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        stack = []
        next_digit = 1
        
        for ch in pattern:
            stack.append(str(next_digit))
            next_digit += 1
            
            if ch == 'I':
                while stack:
                    result.append(stack.pop())
                    
        stack.append(str(next_digit))
        while stack:
            result.append(stack.pop())
        
        return ''.join(result)
