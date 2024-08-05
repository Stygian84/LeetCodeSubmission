class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter  = Counter(nums)
        res = []
        n = len(nums)
        def backtrack(path, current):
            if len(path)==n:
                res.append(path[:])
                return
            
            for num in counter:
                if current.get(num,0) < counter[num]:
                    current[num]+=1
                    path.append(num)
                    backtrack(path,current)
                    path.pop()
                    current[num]-=1

        backtrack([],defaultdict(int))
        return res



