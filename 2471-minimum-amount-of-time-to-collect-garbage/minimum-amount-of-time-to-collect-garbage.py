class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        #paper, metal , glass
        n = len(garbage)
        time = 0
        latest = [0,0,0] #p,m,g

        for i in range(n-1,-1,-1):
            if latest[0]==0 and "P" in garbage[i]:
                latest[0]=i
            if latest[1]==0 and "M" in garbage[i]:
                latest[1]=i
            if latest[2]==0 and "G" in garbage[i]:
                latest[2]=i
        
        time += len("".join(garbage))

        prefix_sum = [0]*(n-1)
        for j in range(len(travel)):
            prefix_sum[j] = prefix_sum[j-1]+travel[j]

        time+=prefix_sum[-1]*3
        #print(prefix_sum)
        #print(latest)

        #print(time)
        for i in range(3):
            if latest[i]==0:
                time -= prefix_sum[-1]
            else:
                time -= prefix_sum[-1] - prefix_sum[latest[i]-1]
            #print(time)
        
        return time