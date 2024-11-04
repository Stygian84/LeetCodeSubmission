class Solution:
    def compressedString(self, word: str) -> str:
        
        comp = ""

        current = word[0]
        count = 1
        for i in range(1,len(word)):
            
            if count==9:
                comp += str(count)
                comp += current
                count = 0
             
            if word[i]==current:
                count+=1
            else:
                if count!=0:
                    comp += str(count)
                    comp += current
                current = word[i]
                count = 1
                
        comp += str(count)
        comp += current
        


        return comp