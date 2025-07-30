from data_structures.graph_classes.linked_list.list_node import ListNode

class SinglyLinkedList:
    def __init__(self):
        self._head = None # Head of the singly linked list
        self._tail = None # Tail of the singly linked list

    def append(self, data):
        # If the head is none the list is empty
        if self._head is None:
            self._head = ListNode(data) # Construct a list node at the head
            self._tail = self._head # Set the tail to the head because there is only 1 element
        # The list is not empty
        else:
            self._tail.set_next(ListNode(data)) # Construct a list node after the tail
            self._tail = self._tail.get_next() # Update the location of the tail

    def get_head(self):
        return self._head