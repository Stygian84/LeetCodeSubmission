class Solution:
    def trimMean(self, arr: List[int]) -> float:
        length=len(arr)
        arr.sort()
        percent=int(round(0.05*length,0))
        new_arr=arr[percent:-percent]

        return sum(new_arr)/len(new_arr)