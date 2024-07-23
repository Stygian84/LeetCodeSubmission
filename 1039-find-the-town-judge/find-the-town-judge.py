class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a=set() #people who trust (cannot be judge)
        b=defaultdict(int) #people who are trusted

        for c,d in trust:
            a.add(c)
            b[d]+=1


        for i in range(1,n+1):
            if i not in a:
                if b[i]==n-1:
                    return i
        return -1