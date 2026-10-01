# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """

        1. starting point (dummy)
        2. assign tail to dummy
        3. While loop
        4. compare the first 2 heads from both lists(if)
        5. tail.next will be list1
        6. increment list1
        7. else 
        8. tail.next will be list2
        9. increment list2
        10. increment tail
        11. if balance in list1
        12. assign tail.next to list1
        13. else balance in list2
        14. assign tail.next to list2
        15 return dummy.next


        time: O(m+n)
        space: O(1)

        Another:
        1. create an empty array
        2. store both lists into the empty array
        3. sort the items in the array
        4. convert back to a linked list

        time: O(nlogn)
        space: O(m+n)
        """

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next





























        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2
        
        return dummy.next
        """