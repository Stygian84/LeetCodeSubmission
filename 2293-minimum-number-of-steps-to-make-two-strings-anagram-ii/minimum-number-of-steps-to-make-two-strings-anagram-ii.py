class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()

        i=0
        j=0
        n=len(s)
        m=len(t)

        count=0
        while i<n and j<m:
            item1=s[i]
            item2=t[j]
            if item1==item2:
                i+=1
                j+=1
                continue
            
            count+=1
            if item1<item2:
                i+=1
            else:
                j+=1
        
        count += len(s[i:])
        count += len(t[j:])
        return count

            
        '''countS=Counter(s)
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
        
        return count'''