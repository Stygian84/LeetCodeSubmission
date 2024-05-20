class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dc={}
        result=""
        map1=key.replace(" ","")
        count=0
        for letter in key.replace(" ",""):
            if letter not in dc:
                dc[letter]=chr(count+97)
                count+=1
        print(dc)
        for item in message:
            if item == " ":
                result+=" "
            else:
                result+=dc[item]
        return result

        