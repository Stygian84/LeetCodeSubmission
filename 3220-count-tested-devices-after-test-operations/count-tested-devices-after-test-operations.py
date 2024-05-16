class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count=0
        for idx in range(len(batteryPercentages)):
            if batteryPercentages[idx]>0:
                count+=1
                for i in range(len(batteryPercentages[idx+1:])):
                    batteryPercentages[idx+1+i]=max(batteryPercentages[idx+1+i]-1,0)
        return count