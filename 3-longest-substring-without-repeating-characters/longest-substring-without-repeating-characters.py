class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        temp_str=deque()
        max_length=0

        dc=set() #store existing character
        for letter in s:
            if temp_str and letter not in dc:
                pass
            else:
                max_length=max(max_length,len(temp_str))
                while letter in dc:
                    dc.remove(temp_str.popleft())
                    #del dc[temp_str.popleft()]
            temp_str.append(letter)
            #dc[letter]=0
            dc.add(letter)
            
        max_length=max(max_length,len(temp_str))
        return max_length