class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        counter = defaultdict(int)
        rooms = [i for i in range(n)]

        occupied = [] # (end_time,room_idx)
        heapq.heapify(meetings) #min-heap based on start
        heapq.heapify(rooms)

        #sort meetings by start time
        #if any occupied rooms<=start_time, free the room and push back to rooms
        #if any rooms available, assign the meeting to the smallest room + counter of that room increases by 1
        #else (no rooms available), check the fastest time the room is being freed, free that room and occupy it
        res = -1
        maximum = -1
        while meetings:
            start,end = heapq.heappop(meetings)
            while occupied and occupied[0][0]<=start:
                _,free_room = heapq.heappop(occupied)
                heapq.heappush(rooms,free_room)
            
            # if at least 1 room is available, assign this meeting to that room
            if rooms:
                available = heapq.heappop(rooms)
                heapq.heappush(occupied,(end,available))
                counter[available]+=1

            #else free the earliest room and add the duration to the start time + assign this meeting to that room
            else:
                earliest,available = heapq.heappop(occupied)
                duration = earliest-start
                heapq.heappush(occupied,(end+duration,available))
                counter[available]+=1

            if counter[available]>maximum:
                res = available
                maximum=counter[available]
            elif counter[available]==maximum:\
                res = min(res,available)
            
            '''else:
                earliest = occupied[0][0]
                duration = earliest-start
                heapq.heappush(meetings,[start+duration, end+duration])
            '''
        return res