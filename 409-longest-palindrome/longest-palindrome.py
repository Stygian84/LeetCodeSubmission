class Solution:
    def longestPalindrome(self, s: str) -> int:
        dc={}
        for item in s:
            dc[item]=dc.get(item,0)+1
        total=0
        has_odd=False
        for key,value in dc.items():
            if len(dc)==1:
                return value
            if value%2==1:
                has_odd=True
            if value>1:
                total+=(value//2)*2
        if has_odd:
            total+=1
        return total
        