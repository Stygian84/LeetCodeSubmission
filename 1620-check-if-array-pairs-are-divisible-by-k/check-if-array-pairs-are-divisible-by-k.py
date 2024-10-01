class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        if sum(arr)%k!=0:
            return False
        
        freq = defaultdict(int)
        for num in arr:
            freq[((num%k)+k)%k]+=1

        for i in range(1,k):
            if freq[i]!=freq[k-i]:
                return False
        return True
        