class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        width = sum(wall[0])
        freq = defaultdict(int)
        
        # check which idx (per 1 unit) has gap (every total of length)
        for length in wall:
            temp = []
            total = 0
            for i in range(len(length)-1):
                total += length[i]
                freq[total]+=1
        
        if not freq:
            return len(wall)

        return len(wall) - max(freq.values())