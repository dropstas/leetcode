# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

# from typing import Optional

# class Node:
#     def __init__(self, x=0):
#         self.data = x
#         self.next = None
#     def __str__(self):
#         return f"[{self.data}]->{self.next}"


# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def __str__(self):
#         return self.head
     
#     # Method to display the list
#     def printList(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" ")
#             temp = temp.next
 
#     # Method to add element to list
#     def addToList(self, newData):
#         newNode = Node(newData)
#         if self.head is None:
#             self.head = newNode
#             return
 
#         last = self.head
#         while last.next:
#             last = last.next
 
#         last.next = newNode
 
 
# alist = LinkedList()
# list = [1,10]
# for i in list:
#     alist.addToList(i)

# blist = LinkedList()
# list = [1,7,8]
# for i in list:
#     blist.addToList(i)

# clist = LinkedList()


# ahead = alist.head
# bhead = blist.head

# while ahead and bhead:
#     if ahead.data < bhead.data:
#         clist.addToList(ahead.data)
#         ahead = ahead.next
#     else:
#         clist.addToList(bhead.data)
#         bhead = bhead.next

# while ahead or bhead:
#     if ahead:
#         clist.addToList(ahead.data)
#         ahead = ahead.next   
#     if bhead:
#         clist.addToList(bhead.data)
#         bhead = bhead.next   
   

# print(clist.head)


        

# # while ahead and bhead:
# #     print(ahead, bhead)
# #     if ahead.data < bhead.data:
# #         tail.next = ahead
# #         ahead = ahead.next
# #         tail = ahead
# #     else:
# #         tail.next = bhead
# #         bhead = bhead.next
    
# # if ahead or bhead:
# #     tail.next = ahead if ahead else bhead

