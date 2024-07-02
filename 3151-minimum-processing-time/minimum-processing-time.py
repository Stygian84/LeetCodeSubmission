class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        tasks.sort(reverse=True)
        processorTime.sort()
        
        n = len(processorTime)
        max_time = 0
        
        for i in range(len(tasks)):
            processor_index = i // 4
            current_time = tasks[i] + processorTime[processor_index]
            max_time = max(max_time, current_time)
        
        return max_time