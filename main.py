from data_structures.graph_classes.linked_list.singly_linked_list import SinglyLinkedList

testList = SinglyLinkedList()

for i in range(11):
    print(i)
    testList.append(i)

cur_item = testList._head
while cur_item is not None:
    print(cur_item.data_getter())
    cur_item = cur_item.next_getter()

print("end")