"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Thought Process
        1. Create an empty map
        2. Create a current Node starting at head
        3. Loop while current is not None
        4. Add each Node (values) to the map
        5. Increment current
        6. reset current to head
        7. Loop while current is not None
        8. Initialize a new Node called copy and assign it the first value in the map
        9. Assign the next pointer for copy to the next pointer of the current in the map
        9. Assign the random pointer for copy to the random pointer of the current in the map
        10. Increment the current
        11. return the head equivalent in the mp

        """
        # Create an empty map with key-value pairs initialize to None
        mp = {None:None}
        curr = head

        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            cpy = mp[curr]
            cpy.next = mp[curr.next]
            cpy.random = mp[curr.random]
            curr = curr.next

        return mp[head]
