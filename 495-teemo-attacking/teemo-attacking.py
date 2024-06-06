class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count=0
        ls=[]
        for item in timeSeries:
            if ls and ls[-1]>item:
                count+=item+duration-ls[-1]
            else:
                count+=duration
            ls.append(item+duration)
        return count