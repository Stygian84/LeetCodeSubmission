class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        freq = Counter(nums)

        count=0
        
        for key in freq.keys():
            if k==0:
                if freq[key]>1:
                    count+=1

            else:
                if key+k in freq:
                    count+=1

        return count
        