class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS=Counter(s)
        countT=Counter(t)

        count = 0

        for letter in s:
            if letter not in countT:
                count+=1
            else:
                if countT[letter]==0:
                    count+=1
                else:
                    countT[letter]-=1

        for letter in t:
            if letter not in countS:
                count+=1
            else:
                if countS[letter]==0:
                    count+=1
                else:
                    countS[letter]-=1
        
        return count