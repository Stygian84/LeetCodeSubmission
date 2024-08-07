class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count1 = Counter(s1)
        count2 = defaultdict(int)

        n = len(s1)
        m = len(s2)
        
        for i in range(m):
            count2[s2[i]] += 1

            if i>= n:
                if count2[s2[i-n]]==1:
                    count2.pop(s2[i-n])
                else:
                    count2[s2[i-n]]-=1
            if count1==count2:
                return True
        return False