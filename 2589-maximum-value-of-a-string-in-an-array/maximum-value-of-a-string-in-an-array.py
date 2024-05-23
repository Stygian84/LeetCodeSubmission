class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_length=0
        for item in strs:
            if item.isdigit():
                value=int(item)
            else:
                value=len(item)
            if value>max_length:
                max_length=value
        return max_length
    