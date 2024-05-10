class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def bin_search(ls,target):
            left = 0
            right = len(ls) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if ls[mid] == target:
                    return True
                elif ls[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        left=0
        right=len(matrix)-1
        while left<=right:
            mid=(left+right)//2
            row=matrix[mid]
            if bin_search(row,target):
                return True
            elif target < row[0]:
                right = mid - 1
            else:
                left = mid + 1
        return False

        '''
        for row in matrix:
            lowest_number = row[0]
            highest_number = row[-1]
            if lowest_number<=target<=highest_number:
                if target in row:
                    return True
                else:
                    False
        '''