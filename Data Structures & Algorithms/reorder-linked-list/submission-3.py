# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Edge case
        if not head or not head.next or not head.next.next: return

        # find the mid
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # reverse the second list
        curr = slow.next # curr is start of the second half
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        front = head
        back = prev

        # interleave
        while back:
            front_temp = front.next
            back_temp = back.next
            front.next = back
            back.next = front_temp
            front = front_temp
            back = back_temp
