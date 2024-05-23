class Solution:
    def countValidWords(self, sentence: str) -> int:
        tokens=sentence.split()
        def isValid(word):
            hypen_count=0
            punctuations="!,."
            for i in range(len(word)):
                if word[i].isdigit():
                    return False
                elif i!=len(word)-1 and word[i] in punctuations:
                    return False
                elif word[i]=="-":
                    hypen_count+=1
                    if hypen_count>1:
                        return False
                    elif i==0 or i==len(word)-1:
                        return False
                    elif (not word[i-1].islower()) or (not word[i+1].islower()):
                        return False
                elif not word[i].islower() and i!=len(word)-1:
                    return False
            return True
        count=0
        for item in tokens:
            if isValid(item):
                count+=1
        return count
                