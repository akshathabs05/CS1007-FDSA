class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = CircularNode(data)
        new_node.next = self.head  
        if not self.head:
            self.head = new_node
            new_node.next = self.head  
        else:
            current = self.head
            while current.next != self.head:  
                current = current.next
            current.next = new_node
            new_node.next = self.head  

    def insert_at_beginning(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  
        else:
            current = self.head
            while current.next != self.head:  
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node  

    def delete_node(self, key):
        if not self.head: 
            return

        current = self.head
        prev = None

       
        if current.data == key:
            if current.next == self.head:  
                self.head = None
            else:
            
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next  
                self.head = self.head.next  
            return

      
        while current.next != self.head and current.data != key:
            prev = current
            current = current.next

        
        if current.data == key:
            prev.next = current.next

    def traverse(self):
        if not self.head: 
            return "List is empty"

        nodes = []
        current = self.head
        while True:
            nodes.append(current.data)
            current = current.next
            if current == self.head:
                break
        return nodes

    def search(self, key):
        if not self.head: 
            return False

        current = self.head
        while True:
            if current.data == key:
                return True
            current = current.next
            if current == self.head: 
                break
        return False
