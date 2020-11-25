# Basic Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    # Should always be pointing to either None or another Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        # Were we passed the data or an actual node?
        if isinstance(data, Node):
            new_node = data
        else:
            new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node
    

    def append(self, data):
        # Were we passed the data or an actual node?
        if isinstance(data, Node):
            new_node = data
        else:
            new_node = Node(data)        
        
        # If list is initialized, but empty, designate node as both head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            # print(f'Head and tail were None, both are now {node.data}')
            return
        # Point current tail toward new node, set tail to new node
        else:
            self.tail.next = new_node
            # print(f'Next node after {self.tail.data} is now {new_node.data}')
            self.tail = new_node
            # print(f'{new_node.data} is now the tail of the list')
            return


    def traverse(self):
        cursor = self.head
        while cursor is not None:
            print(cursor.data)
            cursor = cursor.next
        print(self.tail.data)

    def delete_head(self):
        self.head = self.head.next

    def delete_tail(self):
        # Sanity check
        if self.head == self.tail:
            print("You're drunk. Go home")
            return self.tail

        # Get a cursor to the second to last node
        cursor = self.head
        while cursor.next != self.tail:
            cursor = cursor.next
        
        # Save what the tail is before cutting it off
        popped_tail_node = self.tail

        # Look at me. I am the tail now.
        self.tail = cursor
        cursor.next = None
        
        # Return the tail we cut off as a gift for our overlords
        return popped_tail_node
    

    def delete(self, data):
        # Were we passed the data or an actual node?
        if isinstance(data, Node):
            target = data
        else:
            target = Node(data)

        cursor = self.head
        while cursor is not None:
            if cursor.next.data == target.data:
                cursor.next = cursor.next.next
                break       # Why do I have "break" here? I'm afraid to remove it.
        cursor = cursor.next


def reverse_list(elel):
    new_ll = LinkedList()
    # new_ll.head = elel.delete_tail()
    while elel.head.next != None:
        new_ll.append(elel.delete_tail())
    new_ll.tail = elel.head
    return new_ll

linkinPark = LinkedList()

for i in range(0,11):
    linkinPark.append(i)


linkinPark.delete_head()
linkinPark.delete_tail()
linkinPark.delete(Node(2))

linkinPark.traverse()
print("BREAK-----------------")

hybridTheory = reverse_list(linkinPark)

hybridTheory.traverse()
print(f"Head is {hybridTheory.head.data}")
print(f"Tail is {hybridTheory.tail.data}")
