class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        seen = set()
        if n == 1:
            return []

        res = []
        for bottom in range(2,n+1):

            for top in range(1,bottom):
                decimal = top/bottom
                if decimal in seen:
                    continue
                else:
                    seen.add(decimal)
                    res.append(f"{top}/{bottom}")

        return res