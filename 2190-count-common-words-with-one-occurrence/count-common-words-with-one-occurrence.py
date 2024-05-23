class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dc1={}
        dc2={}
        for item in words1:
            dc1[item]=dc1.get(item,0)+1
        for item in words2:
            dc2[item]=dc2.get(item,0)+1
        count=0
        for item in dc1.keys():
            if dc1.get(item)==dc2.get(item)==1:
                count+=1
        return count