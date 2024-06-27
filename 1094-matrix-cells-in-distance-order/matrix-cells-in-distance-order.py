class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res=[]

        for c in range(cols):
            for r in range(rows):
                res.append([r,c])

        res.sort(key=lambda coord: abs(coord[0] - rCenter) + abs(coord[1] - cCenter))
        return res