class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        node = self.store[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            old = self.store[key]

            old.prev.next = old.next
            old.next.prev = old.prev

            del self.store[key]

        node = Node(key, value)
        self.store[key] = node

        node.prev = self.right.prev
        node.next = self.right
        node.prev.next = node
        self.right.prev = node

        if len(self.store) > self.capacity:
            lru = self.left.next
            self.left.next.next.prev = self.left
            self.left.next = self.left.next.next
            del self.store[lru.key]


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(1, 10)
    assert cache.get(1) == 10
    assert cache.get(2) == 2
