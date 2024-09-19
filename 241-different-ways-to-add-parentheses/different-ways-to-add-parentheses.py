class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        
        def compute(expr):
            if expr in memo:
                return memo[expr]
            
            result = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])
                    
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                result.append(left + right)
                            elif char == '-':
                                result.append(left - right)
                            elif char == '*':
                                result.append(left * right)
            
            if not result:
                result.append(int(expr))
            
            memo[expr] = result
            return result
        
        return compute(expression)