class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        s = set()

        for num in arr1:
            str_num = str(num)
            for i in range(len(str_num)):
                s.add(str_num[:i+1])
        
        #print(s)
        res = 0
        for num in arr2:
            str_num = str(num)
            for i in range(len(str_num)):
                if str_num[:i+1] in s:
                    res = max(res,i+1)
        return res