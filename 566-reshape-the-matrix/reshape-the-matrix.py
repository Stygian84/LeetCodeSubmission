class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        def flatten_array(arr):
            flattened = []
            for item in arr:
                if isinstance(item, list):
                    flattened.extend(flatten_array(item))
                else:
                    flattened.append(item)
            return flattened

        flat = flatten_array(mat)
        if len(flat) != r*c:
            return mat
            
        res = [[0]*c for _ in range(r)]
        
        idx=0
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = flat[idx]
                idx+=1
        
        return res