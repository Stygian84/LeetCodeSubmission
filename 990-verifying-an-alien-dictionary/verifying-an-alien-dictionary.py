class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dc={}
        for i in range(len(order)):
            dc[order[i]]=i
        
        def check_word(item1,item2,dc):
            length=min(len(item1),len(item2))
            for i in range(length):
                index1=dc[item1[i]]
                index2=dc[item2[i]]
                if index2<index1:
                    return False
                else:
                    if item1[i]!=item2[i]:
                        return True
            if len(item1)>length:
                return False
            return True

        for idx in range(len(words)-1):
            item1=words[idx]
            item2=words[idx+1]
            if check_word(item1,item2,dc)==False:
                return False
        return True
