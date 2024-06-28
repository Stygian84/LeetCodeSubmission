class Solution:
    def maxScore(self, s: str) -> int:
        count_one=s.count("1")

        max_total=0
        count_zero=0


        for i in range(len(s)-1):

            if s[i]=="1":
                count_one-=1
            else:
                count_zero+=1
            max_total=max(max_total,count_zero+count_one)
        
        return max_total