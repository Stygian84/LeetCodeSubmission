class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        s=set()

        for word in words:
            odd=[]
            even=[]
            for i in range(len(word)):
                if i%2==0:
                    even.append(word[i])
                else:
                    odd.append(word[i])
            odd.sort()
            even.sort()
            combined = "".join(odd) + "".join(even)
            s.add(combined)

        return len(s)