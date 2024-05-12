class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dict1 = {}
        connotation="!?',;."
        for letter in connotation:
            paragraph=paragraph.replace(letter," ")
        ls=paragraph.split()
        for item in ls:
            if item.lower() not in banned:
                dict1[item.lower()]=dict1.get(item.lower(),0)+1
        max_values=0
        result=""
        print(dict1)
        for key,values in dict1.items():
            if values>max_values:
                result=key
                max_values=values
        return result