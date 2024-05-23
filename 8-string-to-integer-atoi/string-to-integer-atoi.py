class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if len(s)==0:
            return 0
        sign=1
        if s[0]=="+":
            s=s[1:]
        elif s[0]=="-":
            s=s[1:]
            sign=-1
        numbers="1234567890"
        result=0
        leading=True
        for item in s:
            if item =="0" and leading:
                continue
            if item in numbers:
                leading=False
                result=result*10+int(item)
            else:
                break
        result*=sign
        if sign==-1:
            result=max(result,-2**31)
        else:
            result=min(result,2**31-1)
        return result