class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        temp_str=deque()
        max_length=0

        dc={} #store existing character
        for letter in s:
            if temp_str and letter not in dc.keys():
                pass
            else:
                max_length=max(max_length,len(temp_str))
                while letter in dc.keys():
                    del dc[temp_str.popleft()]
            temp_str.append(letter)
            dc[letter]=0
            
        max_length=max(max_length,len(temp_str))
        return max_length