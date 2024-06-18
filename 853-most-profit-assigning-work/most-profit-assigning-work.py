class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        #combine diff and profit ans sort based on diff
        combined_arr=[]
        for d,p in zip(difficulty,profit):
            combined_arr.append([d,p])
        combined_arr.sort()

        max_profit_up_to = []
        max_profit = 0
        for d, p in combined_arr:
            max_profit = max(max_profit, p)
            max_profit_up_to.append((d, max_profit))

        
        def binSearch(arr,val):
            l=0
            r=len(arr)-1
            res=None
            while l<=r:
                mid=(l+r)//2
                if arr[mid][0]<=val:
                    res=arr[mid]
                    l=mid+1
                else:
                    r=mid-1
            return res


        print(combined_arr)
        total=0
        for power in worker:
            if power<combined_arr[0][0]:
                continue
            best_profit=binSearch(max_profit_up_to, power)[1]
            if best_profit is not None:
                total+=best_profit

        return total