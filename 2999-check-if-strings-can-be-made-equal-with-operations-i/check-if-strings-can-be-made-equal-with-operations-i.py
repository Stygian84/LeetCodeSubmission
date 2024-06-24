class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1_zero=set()
        s2_zero=set()
        s1_one=set()
        s2_one=set()


        i=0
        for a,b in zip(s1,s2):
            if a!=b:
                if i%2==0:
                    s1_zero.add(a)
                    s2_zero.add(b)
                else:
                    s1_one.add(a)
                    s2_one.add(b)
            i+=1

        return s1_zero==s2_zero and s1_one==s2_one
        