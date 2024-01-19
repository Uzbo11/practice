# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        nodes = [head.val]
        nextNode = head.next

        while (nextNode != None):
            nodes.append(nextNode.val)
            nextNode = nextNode.next

        return nodes == nodes[::-1]