class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        max_black=0
        for i in range(len(blocks)-k+1):
            cnt=blocks[i:i+k].count("B")
            if cnt>max_black:
                max_black=cnt
        return k-max_black