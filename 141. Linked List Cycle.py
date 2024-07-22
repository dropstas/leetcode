class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False



all = Solution()
all.hasCycle(node1)


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         slow = head
#         fast = head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False
    
# head = [3,2,0,-4]
# pos = 1

# check = Solution()
# check.hasCycle(head)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node1


# print(node1, node2, node3, node4, node5)


# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node1.next = node2
# node2.next = node3



# def print_list(node):
#     while node:
#         print(node)
#         node = node.next



# def print_list_last(node):
#     while node:
#         node = node.next
#         if node == None:
#             print(nodelast)
#         nodelast = node 

# def fromtail(node):
#     if node == None:
#         return
#     head = node
#     tail = node.next
#     fromtail(tail)
#     print(head.data)

# print(node1)




