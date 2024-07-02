class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        tasks.reverse()
        processorTime.sort()

        j=0
        count=0
        max_value=0

        for i in range(len(tasks)):
            max_value=max(max_value,tasks[i]+processorTime[j])
            
            if count==4:
                count=0
                j+=1
                max_value=max(max_value,tasks[i]+processorTime[j])
            
            count+=1
        
        return max_value