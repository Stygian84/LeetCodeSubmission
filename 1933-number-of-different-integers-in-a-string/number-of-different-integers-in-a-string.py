class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        dc={}
        current_num=""
        for item in word:
            if item.isdigit():
                current_num+=item
            else:
                if current_num!="":
                    current_num=int(current_num)
                    dc[current_num]=dc.get(current_num,0)+1
                    current_num=""
        
        if current_num!="":
            current_num=int(current_num)
            dc[current_num]=dc.get(current_num,0)+1
            current_num=""
        return len(dc)