class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        total=mean*(len(rolls)+n)-sum(rolls)
        if total/n>6 or total/n<1:
            return []


        base=total//n
        remainder=total%n
        value_of_max_extra=remainder//n+1
        number_of_max_extra=remainder%n

        res=[total//n+value_of_max_extra]*number_of_max_extra + [total//n]*(n-number_of_max_extra)

        
        return res