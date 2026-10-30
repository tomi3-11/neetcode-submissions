# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0);
        current = dummy;
        # Reset the carry at first start
        carry = 0

        # Loop until
        while l1 or l2 or carry != 0:
            x = 0
            y = 0
            if l1:
                x = l1.val
            if l2:
                y = l2.val

            sum = x + y + carry

            carry = sum // 10
            digit = sum % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:

                l2 = l2.next

        return dummy.next