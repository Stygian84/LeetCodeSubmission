class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def permute(result,start):
            if start == len(s):
                res.append(result)
                return
            
            x = s[start]
            if x.isalpha():
                permute(result + x.lower(), start + 1)
                permute(result + x.upper(), start + 1)
            else:
                permute(result + x, start + 1)

        permute("",0)
        return res