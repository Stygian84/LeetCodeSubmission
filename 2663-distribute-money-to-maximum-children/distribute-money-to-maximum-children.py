class Solution:
    def distMoney(self, money: int, children: int) -> int:
        
        money -= children
        if money<0:
            return -1

        if money // 7 == children and money % 7 == 0:
            return children
        if money // 7 == children - 1 and money % 7 == 3:
            return children - 2
            
        return min(children - 1, money // 7)
        '''if money<children:
            return -1
        if money==children:
            return 0

        res = money//8 #max no of children with 8
        if res == 0:
            return 0
        if children>res:
            leftover = money-res*8
            if leftover==4 or leftover==0:
                res-=1
        #check if possible
        if res*8 + (children-res)>money:
            return 0
        return res
        '''

        '''if money<children:
            return -1
        if money < 8+(children-1):
            return 0
        if children*8==money:
            return children
        
        amount = money//children
        leftover = money%amount
        count = 0
        increment = 8-amount
        
        print(amount,leftover,increment)
        return count'''