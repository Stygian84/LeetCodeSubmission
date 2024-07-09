class Solution:
    def minimizeResult(self, expression: str) -> str:
        min_result = math.inf
        result=""
        ls = expression.split("+")
        first_number = ls[0]
        second_number = ls[1]
        
        for i in range(len(first_number)):
            a = first_number[:i] 
            b = first_number[i:]
            for j in range(1,len(second_number)+1):
                c = second_number[:j]
                d = second_number[j:] 
                one = int(a) if a else 1
                two = int(b) if b else 1
                three = int(c) if c else 1
                four = int(d) if d else 1
                res = one*(two+three)*four
                if res < min_result:
                    min_result=res
                    result = a+"("+b+"+"+c+")"+d

        return result