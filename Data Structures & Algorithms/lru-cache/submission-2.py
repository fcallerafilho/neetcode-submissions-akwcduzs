class LRUCache:
    def __init__(self, capacity: int):
        self.dictionary = {} # key: (value, node)
        self.llist = LinkedList(capacity)

    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return -1
        self.llist.update_node(self.dictionary.get(key)[1])
        return self.dictionary[key][0]

    def put(self, key: int, value: int) -> None:
        if not self.dictionary.get(key):
            nodeRef, removedKey = self.llist.add_node(key)

            if removedKey:
                del self.dictionary[removedKey]

            self.dictionary[key] = (value, nodeRef)
        else:   
            self.llist.update_node(self.dictionary[key][1])
            self.dictionary[key] = (value, self.dictionary[key][1])
        
class ListNode:
    def __init__(self, val: int, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self, capacity):
        self.size = 0
        self.head = self.tail = None
        self.capacity = capacity

    def add_node(self, val: int):
        node = ListNode(val)

        if not self.head:
            self.head = self.tail = node
            print(f'list has one node, {self.head.val}')
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            print(f'node with value {node.val} was added')

        self.size += 1

        removed = None
        if self.size > self.capacity:
            removed = self.remove_from_head()

        return (node, removed if removed else None)

    def remove_from_head(self):
        removed = self.head
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

        print(f'key {removed.val} evicted')
        return removed.val

    def update_node(self, node: ListNode):
        if self.size == 1 or node == self.tail:
            return
        
        curr = node

        if curr == self.head:
            nextNode = curr.next

            nextNode.prev = None
            self.head = nextNode

        else:
            previousNode = curr.prev
            nextNode = curr.next

            previousNode.next = nextNode
            nextNode.prev = previousNode

        curr.prev = self.tail
        curr.next = None

        self.tail.next = curr
        self.tail = self.tail.next

        print(f'node with key {self.tail.val} is the new tail')







        