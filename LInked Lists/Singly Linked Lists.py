# Ceration of Single Linked Lists

class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
class single:
    def __init__(self):
        self.head = None
        self.tail = None

singleLinkedList = single()
node1 = Node(1)
node2 = Node(2)

singleLinkedList.head = node1
singleLinkedList.head.next = node2