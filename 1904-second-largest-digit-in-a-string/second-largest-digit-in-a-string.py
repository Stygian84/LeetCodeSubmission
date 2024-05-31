class Solution:
    def secondHighest(self, s: str) -> int:
        ls=[]
        for item in s:
            try:
                num=int(item)
                if num not in ls:
                    ls.append(num)
            except:
                pass
        if len(set(ls))==1 or ls==[]:
            return -1
        ls.sort()
        return ls[-2]
