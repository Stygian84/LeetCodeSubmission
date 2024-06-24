class Solution:
    def countAndSay(self, n: int) -> str:
        
        ls=["1"]

        def parse(x):
            result=""
            count=1
            current_digit=x[0]
            for digit in x[1:]:
                if digit==current_digit:
                    count+=1
                else:
                    result+=str(count)
                    result+=str(current_digit)
                    count=1
                    current_digit=digit
            result+=str(count)
            result+=str(current_digit)
            return result
        
        for i in range(n-1):
            ls.append(parse(ls[-1]))
        return ls[-1]
        