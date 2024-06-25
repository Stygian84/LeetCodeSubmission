class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)-1):
            dc=defaultdict(int)
            for item in words[i]:
                dc[item]+=1
            for j in range(i+1,len(words)):
                dc2=defaultdict(int)
                for item in words[j]:
                    dc2[item]+=1
                if dc.keys()==dc2.keys():
                    count+=1

        return count