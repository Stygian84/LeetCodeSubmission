class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        freq={0:0,1:0,2:0}
        for value in stones:
            freq[value%3]+=1
        
        if freq[0] %2==0:
            if freq[1]>=1 and freq[2]>=1:
                return True
            return False
        else:
            return abs(freq[1]-freq[2])>2