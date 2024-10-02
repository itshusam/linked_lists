class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def delete(self, data):
        current = self.head

        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                return True
            
            current = current.next

        return False

    def traverse_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

    def traverse_backward(self):
        current_node = self.tail
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.prev
        print("None")


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)


doubly_linked_list.traverse_forward()
doubly_linked_list.traverse_backward()
doubly_linked_list.delete(2)
doubly_linked_list.traverse_forward()
doubly_linked_list.delete(1)
doubly_linked_list.traverse_forward()
doubly_linked_list.delete(10)
doubly_linked_list.traverse_forward()
