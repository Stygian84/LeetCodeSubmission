class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # n rows of seats and each row has 10 columns
        # 1-indexed
        m = 10

        res = 0
        seen = {}
        for row,col in reservedSeats:
            if row in seen:
                seen[row].add(col)
            else:
                seen[row] = set([col])
        
        #if only 1 or/and 10 , res += 2
        #else, res += 1 if 2345 / 6789 / 4567
        for row in seen:
            if seen[row] == set([1]) or seen[row] == set([10]) or seen[row] == set([1,10]):
                res += 2
            else:
                flag = True
                for i in range(2,6):
                    if i in seen[row]:
                        flag = False
                
                if flag:
                    res += 1
                    continue

                flag = True
                for j in range(4,8):
                    if j in seen[row]:
                        flag = False
                
                if flag:
                    res += 1
                    continue

                flag = True
                for k in range(6,10):
                    if k in seen[row]:
                        flag = False
                if flag:
                    res += 1
                    continue
                print(res)

        res += 2*(n-len(seen))
        return res