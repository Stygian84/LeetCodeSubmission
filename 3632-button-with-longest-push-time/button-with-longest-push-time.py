class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        maximum_time = events[0][1]
        index = events[0][0]

        n = len(events)
        for i in range(1,n):
            button = events[i][0]
            duration = events[i][1]-events[i-1][1]

            if duration > maximum_time:
                index = button
                maximum_time = duration
            elif duration == maximum_time:
                index = min(index,button)
        
        return index