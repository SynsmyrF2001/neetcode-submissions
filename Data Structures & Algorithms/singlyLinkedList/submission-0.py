class Node:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        current = self.head
        for _ in range(index):
            if not current:
                return -1
            current = current.next
        return current.val if current else -1
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return 
        current = self.head
        while current.next:
            current = current.next 
        current.next = new_node
        

    def remove(self, index: int) -> bool:
        if index < 0 or not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            return True
        
        current = self.head
        for _ in range (index - 1):
            if not current.next:
                return False
            current = current.next

        if not current.next:
            return False
        
        current.next = current.next.next
        return True
        

    def getValues(self) -> List[int]:
        values = []
        current = self.head
        while current:
            values.append(current.val)
            current = current.next
        return values
        
