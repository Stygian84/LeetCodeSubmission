class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count=0
        minus=0
        for idx in range(len(batteryPercentages)):
            batteryPercentages[idx]-=minus
            if batteryPercentages[idx]>0:
                count+=1
                minus+=1
        return count