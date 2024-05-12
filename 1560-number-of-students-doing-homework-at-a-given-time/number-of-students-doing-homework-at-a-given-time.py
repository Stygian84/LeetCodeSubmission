class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for idx in range(len(startTime)):
            if startTime[idx]<=queryTime<=endTime[idx]:
                count+=1
        return count