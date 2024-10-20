class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        #TODO
        def evaluate(expr: str) -> bool:
            if expr == 't': 
                return True
            if expr == 'f':  
                return False
            
            if expr[0] == '!':  
                return not evaluate(expr[2:-1])
            elif expr[0] == '&': 
                return all(evaluate(sub_expr) for sub_expr in split_expr(expr[2:-1]))
            elif expr[0] == '|':  
                return any(evaluate(sub_expr) for sub_expr in split_expr(expr[2:-1]))

        def split_expr(expr: str):
            result = []
            balance = 0
            sub_expr = []
            for char in expr:
                if char == ',' and balance == 0:
                    result.append(''.join(sub_expr))
                    sub_expr = []
                else:
                    if char == '(':
                        balance += 1
                    elif char == ')':
                        balance -= 1
                    sub_expr.append(char)
            result.append(''.join(sub_expr))  
            return result

        return evaluate(expression)