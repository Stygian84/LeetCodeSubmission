class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ls=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dc={}
        for i in range(26):
            dc[chr(i+97)]=ls[i]
        result=[]
        for item in words:
            parsed=""
            for i in item:
                parsed+=dc[i]
            result.append(parsed)
        return len(set(result))