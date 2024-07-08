class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:


        flattened_list = [item for sublist in matrix for item in sublist]
        flattened_list.sort()
        return flattened_list[k-1]