class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_ls=['qwertyuiop','asdfghjkl','zxcvbnm']
        result=[]
        idx=-1
        add=True
        for word in words:
            for index in range(len(row_ls)):
                if word[0].lower() in row_ls[index]:
                    idx=index
            if idx==-1:
                continue

            for letter in word:
                if letter.lower() not in row_ls[idx]:
                    add=False
                    continue
            if add:
                result.append(word)
            #reset var
            idx=-1
            add=True
        return result