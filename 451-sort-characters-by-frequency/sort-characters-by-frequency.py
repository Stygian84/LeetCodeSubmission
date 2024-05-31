class Solution:
    def frequencySort(self, s: str) -> str:
        dc={}
        for letter in s:
            dc[letter]=dc.get(letter,0)+1
        sorted_dict = dict(sorted(dc.items(), key=lambda item: item[1], reverse=True))   
        print(sorted_dict)
        res=""
        for key,values in sorted_dict.items():
            res+=key*values
        return res