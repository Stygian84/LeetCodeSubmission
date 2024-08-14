class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ending_column = len(matrix[0])
        for row in matrix:
            if row[0]<=target<=row[-1]: #might be in this row

                for j in range(ending_column):
                    if row[j]==target:
                        return True
                    elif row[j]>target:
                        ending_column = j
                        break
        return False