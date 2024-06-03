class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptr=0
        for item in s:
            if ptr==len(t):
                return 0
            if item==t[ptr]:
                ptr+=1
                continue
        return len(t)-ptr
                

        '''temp_str=""
        max_length=0
        for item in s:
            temp_str+=item
            if t.startswith(temp_str):
                if len(temp_str)>max_length:
                    max_length=len(temp_str)
            elif t.startswith(item):
                if len(item)>max_length:
                    max_length=len(item)
            else:
                temp_str=item

        return len(t)-max_length       ''' 