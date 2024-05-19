class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr=sorted(arr)
        dc={}
        rank=1
        for item in sorted_arr:
            if item in dc:
                pass
            else:
                dc[item]=rank
                rank+=1
        result=[]
        for item in arr:
            result.append(dc[item])
        return result