class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        #store index of all seated seats
        filled = []
        n = len(seats)
        for i in range(n):
            if seats[i]==1:
                filled.append(i)
        
        #try to slot in in between any consecutive 2 seated seats
        dist = -1
        for i in range(1, len(filled)):
            if filled[i]-filled[i-1]>1 and (filled[i] - filled[i-1])//2> dist:
                dist = (filled[i] - filled[i-1])//2
        #dist//=2 #divide by 2 because its in between 2 seats
        #check if first seat or last seat is zero, then try to slot in that position
        if seats[0] == 0:
            dist = max(filled[0], dist)
        if seats[-1] == 0:
            dist = max((n-1)-filled[-1], dist)
        
        return dist
        '''n = len(seats)

        index = []
        zero = 0
        for i in range(len(seats)):
            if seats[i]==1:
                index.append(i)
            else:
                zero+=1
        if zero==1:
            return 1
        # if only 1 person, check last/first
        if len(index)==1:
            return max(index[0]-0, n-index[0]-1)
        
        maximum_dist = -1
        for i in range(1,len(index)):
            pos = (index[i]-index[i-1])//2
            if index[i]-index[i-1]==2:
                maximum_dist=1
                continue
                
            if i == len(index)-1:
                diff = pos-index[i-1]
            else:
                diff = max(pos-index[i-1],index[i]-pos)
            #print(pos,diff)
            if diff == 0 :
                continue
            if diff>maximum_dist:
                maximum_dist = diff
        
        return maximum_dist'''