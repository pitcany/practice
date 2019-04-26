#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:51:23 2019

@author: yannik
"""

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
            
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.count = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.getNode(index) is None:
            return -1
        return self.getNode(index).val
    
    def getNode(self, index: int) -> Node:
        """
        Get the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0:
            return
        current = self.head
        for n in range(index):
            if current is None:
                break
            current = current.next
        return current
    
    def getHead(self) -> Node:
        return self.head
    
    def getTail(self) -> Node:
        curr = self.head
        while(curr is not None and curr.next is not None):
            curr = curr.next
        return curr
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self.count += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            prev = self.getTail()
            prev.next = node
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        if index < 0 or index > self.count:
            return
        elif index==0:
            self.addAtHead(val)
        elif index==self.count:
            self.addAtTail(val)
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node
            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.count-1 or index < 0:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            prev = None
            cur = self.head
            for n in range(index):
                prev = cur
                cur = cur.next
            prev.next = cur.next
        self.count -= 1
            
    def print_list(self):
        if self.count == 0:
            return
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur=cur.next

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.get(-1)
obj.deleteAtIndex(1)
obj.get(-3)
obj.get(0)
obj.addAtIndex(1,2)
obj.get(0)
obj.get(1)
obj.addAtIndex(0,1)
obj.get(0)
obj.get(1)

#obj.addAtHead(0)
#obj.addAtIndex(1,9)
#obj.addAtIndex(1,5)
#obj.addAtTail(7)
#obj.addAtHead(1)
#obj.addAtIndex(5,8)
#obj.addAtIndex(5,2)
#obj.addAtIndex(3,0)
#obj.addAtTail(1)
#obj.addAtTail(0)
#obj.deleteAtIndex(6)
