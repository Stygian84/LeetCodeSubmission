class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dc = defaultdict(list) 
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.dc[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        res = []

        def traverse(node):
            if node:
                if node not in self.dead:
                    res.append(node)
                for children in self.dc[node]:
                    traverse(children)
                    
        traverse(self.king)
        return res

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()