class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        ls = []
        for i in range(len(times)):
            ls.append((times[i][0],times[i][1],i))
        heapq.heapify(ls)

        n = len(times)
        chair = [i for i in range(n)]
        heapq.heapify(chair)

        end = [] # (endtime,chair_idx)

        #sorted list by arrival time
        #if end < arrival time; free chair , push back to chair
        #get the smallest chair n assign to idx push to end
        #
        while ls:
            arrive,leave,idx = heapq.heappop(ls)
            while end and end[0][0]<=arrive:
                _,chair_idx = heapq.heappop(end)
                heapq.heappush(chair,chair_idx)
            
            available = heapq.heappop(chair)
            heapq.heappush(end,(leave,available))
            if targetFriend==idx:
                return available