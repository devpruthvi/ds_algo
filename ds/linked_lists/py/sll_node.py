class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return self.__str__()

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def create_node_if_not_valid(new_node):
        if not isinstance(new_node, Node):
            new_node = Node(new_node)
        return new_node

    def insert_at_head(self, new_node):
        new_node = SinglyLinkedList.create_node_if_not_valid(new_node)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_last(self, new_node):
        new_node = SinglyLinkedList.create_node_if_not_valid(new_node)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
    
    def insert_at_position(self, pos,new_node):
        new_node = SinglyLinkedList.create_node_if_not_valid(new_node)
        if self.head == None:
            self.head = new_node
        if pos == 0:
            self.insert_a_head(new_node)
            return
        previous = self.head
        current = self.head.next
        idx = 1
        while current != None and idx < pos:
            previous = current
            current = current.next
            idx += 1
        if idx == pos:
            previous.next = new_node
            new_node.next = current


    def delete_at_head(self):
        if self.head == None:
            return
        head = head.next
    
    def delete_at_last(self):
        if self.head == None:
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = None
    
    def delete_by_value(self, other_val):
        if self.head == None:
            return
        if self.head.val == other_val:
            self.head = self.head.next
        else:
            previous = self.head
            current = self.head.next
            while current != None:
                if current.val == other_val:
                    previous.next = current.next
                    break
                previous = current
                current = current.next
    
    def delete_at_position(self, pos):
        if self.head == None:
            return
        if pos == 0:
            self.delete_at_head()
            return
        previous = self.head
        current = self.head.next
        idx = 1
        while current != None and idx < pos:
            previous = current
            current = current.next
            idx += 1
        if idx == pos and current != None:
            previous.next = current.next
    
    def delete_all_by_value(self, other_val):
        if self.head == None:
            return
        if self.head.val == other_val:
            self.head = self.head.next
        previous = self.head
        current = self.head.next
        while current != None:
            if current.val == other_val:
                previous.next = current.next
            previous = current
            current = current.next
        
            
    def print_linked_list(self):
        temp = self.head
        while temp != None:
            print(temp.val, end=' -> ')
            temp = temp.next
        print('None')
    
    def __len__(self):
        temp = self.head
        length = 0
        while temp != None:
            temp = temp.next
            length += 1
        return length