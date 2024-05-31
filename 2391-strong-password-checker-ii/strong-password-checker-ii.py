class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        lower_count=0
        upper_count=0
        digit_count=0
        special_count=0
        special="!@#$%^&*()-+"
        prev_char=None
        for item in password:
            if item.islower():
                lower_count+=1
            if item.isupper():
                upper_count+=1
            if item.isdigit():
                digit_count+=1
            if item in special:
                special_count+=1
            if item==prev_char:
                return False
            prev_char=item
        if lower_count>0 and upper_count>0 and digit_count>0 and special_count>0:
            return True
        return False

        