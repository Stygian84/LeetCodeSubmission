class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle=columnTitle[::-1]
        print(ord("A"))
        result=0
        for idx in range(len(columnTitle)):
            if idx==0:
                result+=ord(columnTitle[idx])-64
            else:
                result+=26**(idx)*(ord(columnTitle[idx])-64)
        
        return result
        