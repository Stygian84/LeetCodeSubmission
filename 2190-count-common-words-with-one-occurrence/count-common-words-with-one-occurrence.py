class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        inter=set(words1)&set(words2)
        count=0
        for item in inter:
            if words1.count(item)==1 and words2.count(item)==1:
                count+=1
        return count