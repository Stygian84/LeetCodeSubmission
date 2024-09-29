class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None
class AllOne:

    def __init__(self):
        self.key_count = {} 
        self.count_node = {} 
        self.head = Node(float('-inf'))  
        self.tail = Node(float('inf'))   
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_node[node.count]

    def _add_node_after(self, new_node, prev_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        self.count_node[new_node.count] = new_node

    def inc(self, key: str) -> None:
        count = self.key_count.get(key, 0)
        new_count = count + 1
        self.key_count[key] = new_count

        if new_count not in self.count_node:
            new_node = Node(new_count)
            if count == 0:
                self._add_node_after(new_node, self.head)
            else:
                self._add_node_after(new_node, self.count_node[count])
        
        self.count_node[new_count].keys.add(key)

        if count > 0:
            self.count_node[count].keys.remove(key)
            if not self.count_node[count].keys:
                self._remove_node(self.count_node[count])

    def dec(self, key: str) -> None:
        count = self.key_count[key]
        new_count = count - 1

        if new_count > 0:
            self.key_count[key] = new_count
            if new_count not in self.count_node:
                new_node = Node(new_count)
                self._add_node_after(new_node, self.count_node[count].prev)
            self.count_node[new_count].keys.add(key)
        else:
            del self.key_count[key]

        self.count_node[count].keys.remove(key)
        if not self.count_node[count].keys:
            self._remove_node(self.count_node[count])

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()