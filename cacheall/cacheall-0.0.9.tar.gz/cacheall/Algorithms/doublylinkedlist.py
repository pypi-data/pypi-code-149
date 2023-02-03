# Class for a Doubly LinkedList Node
from .dllnode import DLLNode

class DoublyLinkedList:
    
    def __init__(self):
        self.head=None
        self.tail=None
    

    def deleteNode(self, node):
        # head and tail both will be manipulated
        if node==self.head:
            self.head=node.next
            self.head.prev=None
        elif node==self.tail:
            self.tail=node.prev
            self.tail.next=None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        del node

    def addToHead(self, key, val):
        node=DLLNode(key,val)
        if self.head == None:
            self.head=node
            self.tail=node
        else:
            node.next = self.head
            self.head.prev=node
            self.head = node
        return node

    def printlist(self,h):
        temp=h
        while temp!=None:
            print(temp.key," ",temp.val)
            temp=temp.next
