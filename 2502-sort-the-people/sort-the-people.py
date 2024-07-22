class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dc={}
        for idx in range(len(names)):
            dc[heights[idx]]=names[idx]
        heights.sort(reverse=True)
        result=[]
        for item in heights:
            result.append(dc[item])
        return result
        
        