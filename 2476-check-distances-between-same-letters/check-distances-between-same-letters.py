class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dc={}
        for i in range(len(s)):
            item=ord(s[i])-ord('a')
            if item not in dc:
                dc[item]=i
            else:
                dc[item]=i-dc[item]-1
        
        
        for key in dc.keys():
            if dc[key]!=distance[key]:
                return False
        return True