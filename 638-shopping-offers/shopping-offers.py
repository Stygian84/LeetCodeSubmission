class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        m = len(needs)

        res = 0
        for i in range(m):
            res += needs[i]*price[i]

        def dfs(total,need):
            nonlocal res
            if total>res:
                return
            if need == [0]*m:
                res = min(res,total)
                return

            for item in special:
                new_need = need[:]
                flag = False #invalid
                
                non_zeroes = []
                for i in range(len(item)-1):   
                    new_need[i] -= item[i]
                    if new_need[i]<0:
                        flag = True
                        break
                    elif new_need[i]>0:
                        non_zeroes.append(i)
                
                if flag:
                    pass
                else:
                    #fill the non zeroes with price
                    temp_total = total+item[-1]
                    for idx in non_zeroes:
                        temp_total += new_need[idx]*price[idx]
                    
                    res = min(res,temp_total)

                    dfs(total + item[-1], new_need)
                



        dfs(0,needs)
        return res