# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
        def mergeTwoLists(list1,list2):
            dummy = ListNode()
            res = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    res.next = list1
                    list1 = list1.next
                else:
                    res.next = list2
                    list2 = list2.next
                res = res.next
            if list1:
                res.next = list1
            elif list2:
                res.next = list2

            return dummy.next
        if lists==[] or lists==[[]]:
            return None
        if len(lists)==1:
            return lists[0]
        current_list=lists[0]
        for i in range(1,len(lists)):
            current_list=mergeTwoLists(current_list,lists[i])
        return current_list