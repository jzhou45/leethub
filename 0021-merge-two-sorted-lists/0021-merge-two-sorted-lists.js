/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    const ans = new ListNode();
    let dummy = ans;
    
    while (list1 && list2){
        if (list1.val < list2.val){
            dummy.next = new ListNode(list1.val);
            list1 = list1.next
        } else{
            dummy.next = new ListNode(list2.val);
            list2 = list2.next
        };
        
        dummy = dummy.next;
    };
    
    if (list1){
        dummy.next = list1;
    } else{
        dummy.next = list2;
    };
    
    return ans.next;
    
};