class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid = len(arr)//2
            left_sorted = merge_sort(arr[:mid])
            right_sorted = merge_sort(arr[mid:])

            return merge(left_sorted, right_sorted)
        
        def merge(left,right):
            result = []
            i,j=0,0

            while i<len(left) and j<len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        return merge_sort(nums)