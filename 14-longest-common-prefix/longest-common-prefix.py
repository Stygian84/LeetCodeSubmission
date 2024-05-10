class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        min_length=math.inf
        for item in strs:
            if len(item)<min_length:
                min_length=len(item)
        for i in range(min_length):
            prefix+=strs[0][i]
            print(prefix,i)
            for word in strs:
                if word[i]!=prefix[i]:
                    return prefix[:-1]
        return prefix