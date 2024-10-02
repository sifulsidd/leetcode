# use two pointers
# one previous pointer that will always be the current value, and one current pointer that allows us to go through the list
# we use a temporary variable becasue we will reassign the curr pointer, so assign that to the next value 
# curr.next is going to be the previous value, and the previous value is curr 
# then we go next 

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # start with null value 
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
            
        