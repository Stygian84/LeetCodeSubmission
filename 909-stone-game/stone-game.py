class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        '''n = len(piles)
        def dfs(alice,bob,total,arr):
            nonlocal n
            if total==n:
                return alice>bob
            
            first = arr[0]
            last = arr[-1]
            new_arr = arr[1:-1]
            
            return (dfs(alice+last,bob+first,total+2,new_arr) or dfs(alice+first,bob+last,total+2,new_arr))
        
        return dfs(0,0,0,piles)'''
