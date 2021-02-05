# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = ListNode()
        psum = sum
        p1 = l1
        p2 = l2
        carrier = 0
        while True:
            localsum = carrier
            if p1 is not None:
                localsum += p1.val
                p1 = p1.next
            if p2 is not None:
                localsum += p2.val
                p2 = p2.next
            psum.val =  localsum % 10
            if localsum >=10:
                carrier = 1
            else:
                carrier = 0

            if (p1 is None) and (p2 is None) and (carrier == 0):
                break
            else:
                psum.next = ListNode()
                psum = psum.next
        return sum
