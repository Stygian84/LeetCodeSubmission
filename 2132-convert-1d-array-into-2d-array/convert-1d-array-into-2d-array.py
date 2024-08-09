class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m*n!=len(original):
            return []

        res = []
        temp_array = []

        for i in range(m*n):
            temp_array.append(original[i])
            if (i+1)%n==0:
                res.append(temp_array)
                temp_array=[]

        return res