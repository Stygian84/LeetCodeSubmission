class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_string = s.lower()
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', lowercase_string)
        return not cleaned_string.find(cleaned_string[::-1])