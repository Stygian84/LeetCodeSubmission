/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let carry = 0
    let res = new ListNode(0)
    let dummy = res

    while (l1 || l2 || carry>0){
        let current = 0
        if (l1 && l2){
            current = l1.val+l2.val
            l1 = l1.next
            l2 = l2.next
        }
        else if (l1){
            current = l1.val
            l1 = l1.next
        }
        else if (l2){
            current = l2.val
            l2 = l2.next
        }
        current += carry
        dummy.next = new ListNode(current%10) 
        carry = Math.floor(current/10)
        dummy = dummy.next
        
    }
    return res.next
};