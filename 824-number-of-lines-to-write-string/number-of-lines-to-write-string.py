class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        max_length=100
        line=1
        for item in s:
            length=widths[ord(item)-97]
            if max_length-length<0:
                line+=1
                max_length=100-length
                continue
            max_length-=length
        return [line,100-max_length]
        