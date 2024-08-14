class MagicDictionary:

    def __init__(self):
        self.dc = defaultdict(list)   

    def buildDict(self, dictionary: List[str]) -> None:
        for item in dictionary:
            self.dc[len(item)].append(item)

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        if n in self.dc:

            for item in self.dc[n]:
                count = 0
                for a,b in zip(searchWord,item):
                    if a!=b:
                        count+=1
                    if count>1:
                        break
                        
                else:
                    if count == 1:
                        return True

        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)