class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dc={}
        for item in arr1:
            dc[item]=dc.get(item,0)+1
        result=[]
        for item in arr2:
            result+=[item]*dc[item]
            dc[item]=0
        ls2=[]
        for key,value in dc.items():
            if value!=0:
                ls2+=[key]*value
        ls2.sort()
        result.extend(ls2)
        return result