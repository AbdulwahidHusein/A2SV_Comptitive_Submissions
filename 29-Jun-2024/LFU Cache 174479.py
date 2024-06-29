# Problem: LFU Cache - https://leetcode.com/problems/lfu-cache/

class Node: 
    def __init__(self, key, val, count = 0, prv=None, next=None): 
        self.key = key
        self.val = val
        self.count = count
        self.prv = prv
        self.next = next

class LFUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.d1 = {}
        self.d2 = {}
        self.cnt = 0
        
    def get(self, key: int) -> int:
        if key in self.d1: 
            node = self.d1[key]
            value = node.val
            count = node.count
            head, tail = self.d2[count]
            if head == node == tail: 
                self.d2.pop(count)
                if count == self.cnt: 
                    self.cnt += 1
            elif head == node: 
                self.d2[count][0] = node.next
                self.d2[count][0].prv = None
                node.next = None
            elif tail == node: 
                self.d2[count][1] = node.prv
                self.d2[count][1].next = None
                node.prv = None
            if node.prv is None: 
                if node.next is not None: 
                    node.next.prv = None
                    node.next = None
            else: 
                if node.next is None: 
                    node.prv.next = None
                    node.prv = None
                else: 
                    node.prv.next, node.next.prv = node.next, node.prv
                    node.next = None
                    node.prv = None
            if count + 1 not in self.d2: 
                self.d2[count + 1] = [node, node]
            else: 
                _, newtail = self.d2[count + 1]
                newtail.next = node
                node.prv = newtail
                self.d2[count + 1][1] = node
            node.count += 1
            return value        
        else: 
            return -1

    def put(self, key: int, value: int) -> None:      
        if key in self.d1: 
            # if the key exists in the dictionary, no removal.
            node = self.d1[key]
            node.val = value
            count = node.count
            head, tail = self.d2[count]
            if head == node == tail: 
                self.d2.pop(count)
                if count == self.cnt: 
                    self.cnt += 1
            elif head == node: 
                self.d2[count][0] = node.next
                self.d2[count][0].prv = None
                node.next = None
            elif tail == node: 
                self.d2[count][1] = node.prv
                self.d2[count][1].next = None
                node.prv = None
            if node.prv is None: 
                if node.next is not None: 
                    node.next.prv = None
                    node.next = None
            else: 
                if node.next is None: 
                    node.prv.next = None
                    node.prv = None
                else: 
                    node.prv.next, node.next.prv = node.next, node.prv
                    node.next = None
                    node.prv = None
            if count + 1 not in self.d2: 
                self.d2[count + 1] = [node, node]
            else: 
                _, newtail = self.d2[count + 1]
                newtail.next = node
                node.prv = newtail
                self.d2[count + 1][1] = node
            node.count += 1
        else: 
            # if new key
            if len(self.d1) < self.c: 
                # if new key will not overpass the capacity
                node = Node(key, value, 0)
                self.d1[key] = node
                if 1 in self.d2: 
                    head, tail = self.d2[1]
                    tail.next = node
                    node.prv = tail
                    node.count += 1
                    self.d2[1][1] = node
                else: 
                    self.d2[1] = [node, node]
                    node.count += 1
                self.cnt = 1
            else: 
                # if new key overpasses the capacity, we need to remove a key.
                if not self.cnt in self.d2: 
                    return None
                head, tail = self.d2[self.cnt]
                node_tomove = head
                if head == tail: 
                    self.d2.pop(self.cnt)
                else: 
                    head.next.prv = None
                    self.d2[self.cnt][0] = head.next
                    head.next = None
                self.d1.pop(node_tomove.key)
                node = Node(key, value, 0)
                self.d1[key] = node
                if 1 in self.d2: 
                    head, tail = self.d2[1]
                    tail.next = node
                    node.prv = tail
                    node.count += 1
                    self.d2[1][1] = node
                else: 
                    self.d2[1] = [node, node]
                    node.count += 1
                self.cnt = 1
                
                    
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)