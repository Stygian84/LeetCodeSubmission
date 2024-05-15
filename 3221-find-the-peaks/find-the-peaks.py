class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        result=[]
        for idx in range(1,len(mountain)-1):
            first=mountain[idx-1]
            second=mountain[idx]
            third=mountain[idx+1]
            print(first,second,third)
            if second>first and second > third:
                result.append(idx)
        return result
        