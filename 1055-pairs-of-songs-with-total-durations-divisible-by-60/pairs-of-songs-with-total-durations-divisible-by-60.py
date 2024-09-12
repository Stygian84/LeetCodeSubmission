class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq = defaultdict(int)
        n = len(time)

        count = 0
        for i in range(n):
            for k in freq:
                if (time[i]+k) %60==0:
                    count+=freq[k]
            freq[time[i]]+=1
        
        return count
