class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    
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
        self.tail = new_node  

    def delete(self, data):
        current = self.head
        prev = None

        while current:
            if current.data == data:
                if prev:  
                    prev.next = current.next
                else:  
                    self.head = current.next
                
                if current.next is None:  
                    self.tail = prev
                
                return True  
            
            prev = current
            current = current.next

        return False 
    

    def __iter__(self):
        current=self.head
        while current:
            yield current.data
            current=current.next


    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  




linked_list = SinglyLinkedList()

   
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.traverse() 

linked_list.delete(2)
linked_list.traverse()  

linked_list.delete(1)  
linked_list.traverse()  

    
linked_list.delete(10)  
linked_list.traverse()  
