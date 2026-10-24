/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *dummy = new ListNode(0, head);
        ListNode *left = dummy;
        ListNode *right = head;

        // pushing right to the number of n
        while (n>0 && right!=NULL) {
            right = right->next;
            n --;
        }

        // Moving the pointers, right or left till right reaches the last node
        while (right != NULL) {
            right = right->next;
            left = left->next;
        }

        // point the next node for left to the 2nd next
        // this means deleting the next node from left
        // return the updated list
        left->next = left->next->next;
        return dummy->next;
    }
};
