from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head.next

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None  # Split the list into two halves
        
        while second: 
            tmp = second.next 
            second.next = prev 
            prev = second
            second = tmp
            
        #merge the two halfs alternately
        first, second = head, prev
        
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

if __name__ == "__main__":
    # Example usage
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol = Solution()
    sol.reorderList(head)
    # The output will show the middle node value