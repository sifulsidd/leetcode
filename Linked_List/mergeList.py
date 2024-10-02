# just use a dummy to keep track of everything 
# combine based off of that

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        d = dummy 
        while list1 and list2:
            if list1.val <= list2.val:
                d.next = list1
                list1 = list1.next
                d = d.next
            else:
                d.next = list2
                list2 = list2.next
                d = d.next
        
        if list1:
            d.next = list1
        
        if list2:
            d.next = list2
        
        return dummy.next