/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        // if (head == null || head.next.next == null || head.next == null) return;

        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }

        ListNode curr = slow.next;
        slow.next = null;
        ListNode prev = null;

        while (curr != null){
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        ListNode front = head;
        ListNode back = prev;

        while (back != null){
            ListNode frontTemp = front.next;
            ListNode backTemp = back.next;
            front.next = back;
            back.next = frontTemp;
            front = frontTemp;
            back = backTemp;
        }
    }
}
