/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        //create two Nodes //curent & previous
        //set previous to null //loop through list //in each iteration:
        //change pointers
        //use temporary node to store next node (so we don't lo point current to previous move forward
        //Finally previous will be our head
        //Return previous
        let current = head;
        let prev = null;

        while(current){
            let next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }
}
