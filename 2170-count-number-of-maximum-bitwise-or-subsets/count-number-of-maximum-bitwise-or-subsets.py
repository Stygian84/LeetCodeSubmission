class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        def genSubset(arr,res,subset,index):
            freq[res]+=1

            for i in range(index,len(arr)):
                subset.append(arr[i])

                genSubset(arr, res | arr[i], subset, i+1)
                
                subset.pop()
        
        subset = []
        res = 0
        idx = 0
        genSubset(nums,res,subset,idx)
        #print(freq)

        return freq[max(freq.keys())]