class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        dc1={}
        dc2={}
        if len(s)!=len(goal):
            return False
        if s==goal:
            dc1={}
            for i in s:
                dc1[i]=dc1.get(i,0)+1
                if dc1[i]>=2:
                    return True
            return False
        first_idx=-1
        second_idx=-1
        count=0
        for a,b in zip(s,goal):
            if a!=b:
                if first_idx==-1:
                    first_idx=count
                elif second_idx==-1:
                    second_idx=count
                else:
                    return False
            count+=1
        if second_idx==-1:
            return False
        res=""
        res+=s[:first_idx]+s[second_idx]+s[first_idx+1:second_idx]+s[first_idx]+s[second_idx+1:]

        return res==goal