class Node:
    def __init__(self, key: int = -1, value = -1):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.least_recent = Node()
        self.recent = Node()
        self.least_recent.next = self.recent
        self.recent.prev = self.least_recent

    def appendNode(self, recently_used: Node) -> None:
        self.recent.prev.next = recently_used
        recently_used.prev = self.recent.prev
        recently_used.next = self.recent
        self.recent.prev = recently_used

        self.size += 1
    
    def removeNode(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        curr_node = self.cache[key]
        self.removeNode(curr_node)
        self.appendNode(curr_node)

        return curr_node.value

    def put(self, key: int, value: int) -> None:
        curr_node = self.cache[key] if key in self.cache else Node(key, value)
        if key in self.cache:
            curr_node.value = value
            self.removeNode(curr_node)
        else:
            self.cache[key] = curr_node

        self.appendNode(curr_node)
        if self.size > self.capacity:
            del self.cache[self.least_recent.next.key]
            self.removeNode(self.least_recent.next)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)