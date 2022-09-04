# Creation in Singly Linked List
# Insertion in Singly Linked List
# Traversal in Singly Linked List
# Searching in Singly Linked List
# Deletion in Singly Linked List

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while(node):
            yield node
            node = node.next

    # insertion in Linked List
    
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            if location == 0 :
                newNode.next = self.head
                self.head = newNode
            
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

                if tempNode == self.tail:
                    self.tail = newNode

    # Traverse Singly Linked List

    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Searching an Element in Singly Linked List

    def searchSLL(self,nodeValue):
        if self.head is None:
            return "The Singly Linked List does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in the list"

    def deleteNode(self,location):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

singlyLinkdeList = SLinkedList()

singlyLinkdeList.insertSLL(1, 1)
singlyLinkdeList.insertSLL(2, 1)
singlyLinkdeList.insertSLL(3, 1)
singlyLinkdeList.insertSLL(4, 1)
singlyLinkdeList.insertSLL(0, 0)
singlyLinkdeList.insertSLL(5, 4)


singlyLinkdeList.deleteNode(0)


print([node.value for node in singlyLinkdeList])

singlyLinkdeList.traverseSLL()

print(singlyLinkdeList.searchSLL(3))

print(singlyLinkdeList.searchSLL(33))
