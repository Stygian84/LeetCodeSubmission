class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        #count freq
        #count sum freq
        # count from the back target-arr[i]
        #arr[i]+arr[j] = target-arr[k]

        n = len(arr)
        freq = defaultdict(int)
        sum_freq = defaultdict(int)
        total = 0

        for i in range(n):

            if -arr[i] in sum_freq:
                total+=sum_freq[-arr[i]]
        
            for k,v in freq.items():
                sum_freq[arr[i]+k-target]+=v
            freq[arr[i]]+=1

        return total % (10**9+7)