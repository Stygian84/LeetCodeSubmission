class Solution:
    def modifyString(self, s: str) -> str:
        def get_valid_letter(before, after):
            for letter in string.ascii_lowercase:
                if letter != before and letter != after:
                    return letter
        ls=list(s)
        
        for idx in range(len(ls)):
            if ls[idx] == "?":
                before = ls[idx - 1] if idx > 0 else None
                after = ls[idx + 1] if idx < len(ls) - 1 else None
                ls[idx] = get_valid_letter(before, after)
                    
        return "".join(ls)