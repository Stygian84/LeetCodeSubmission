class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        if not arrays or len(arrays) < 2:
            return 0

        min_value, min_index = arrays[0][0], 0
        max_value, max_index = arrays[0][-1], 0
        res = 0

        for i in range(1, len(arrays)):
            res = max(res, abs(arrays[i][-1] - min_value))  
            res = max(res, abs(arrays[i][0] - max_value))   

            if arrays[i][0] < min_value:
                min_value, min_index = arrays[i][0], i
            if arrays[i][-1] > max_value:
                max_value, max_index = arrays[i][-1], i

        return res
