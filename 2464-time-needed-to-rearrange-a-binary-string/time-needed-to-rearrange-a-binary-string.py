class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:

        res = 0
        count = 0
        for item in s:
            if item=="0":
                count+=1
            else:
                if count>0:
                    res=max(res+1,count)
        return res
        '''n = len(s)
        ls = list(s)

        flag_count = 1
        count = 0
        while flag_count>0:
            flag_count=0
            flag = False

            count += 1

            for i in range(n-1):
                if flag:
                    flag = False
                    continue
                if ls[i]=="0" and ls[i+1]=="1":
                    ls[i],ls[i+1] = ls[i+1],ls[i]
                    flag = True
                    flag_count += 1


        return count-1'''