class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0

        for j in range(1, n - 1):
            left_smaller = left_greater = right_smaller = right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                elif rating[i] > rating[j]:
                    left_greater += 1

            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                elif rating[k] > rating[j]:
                    right_greater += 1

            count += left_smaller * right_greater + left_greater * right_smaller

        return count

        '''n = len(rating)
        count = 0
        res = []
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) :
                        count+=1
                        res.append( (rating[i] , rating[j] , rating[k]) )
        print(res)
        return count'''