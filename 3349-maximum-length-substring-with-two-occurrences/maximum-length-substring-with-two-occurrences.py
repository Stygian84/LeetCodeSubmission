class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        result=[]
        current_string=""
        for idx in range(len(s)):
            current_letter=s[idx]
            current_string+=current_letter
            if current_string.count(current_letter)<=2:
                result.append(current_string)
                while current_string.count(current_letter)>2:
                    current_string=current_string[1:]
            else:
                while current_string.count(current_letter)>2:
                    current_string=current_string[1:]

        if result==[]:
            return len(s)
        
        print(result)
        max_length=1
        for item in result:
            if len(item)>max_length:
                max_length=len(item)
        return max_length