class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        skip=False
        for idx in range(len(arr)):
            if skip:
                skip=False
                continue
            if arr[idx]==0:
                arr[idx+1:] = arr[idx:-1]
                arr[idx] = 0
                skip=True
        
        