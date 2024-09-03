class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        

        freq = Counter(num)
        ls = []

        maximum = -1
        for k,v in freq.items():
            if v%2==1 and int(k)>maximum:
                maximum = int(k)
            if v>1:
                ls += [k]*(v//2)

        ls.sort(reverse=True)
        
        if maximum!=-1:
            res = ls + [str(maximum)] + ls[::-1]
        else:
            res = ls + ls[::-1]
        


        result = "".join(res).lstrip("0").rstrip("0")
        if result:
            return result
        return "0"