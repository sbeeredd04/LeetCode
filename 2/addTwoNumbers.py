from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10
            
            # Create new node with the digit
            curr.next = ListNode(digit)
            curr = curr.next
            
            # Move to next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
    

# Example usage
if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    
    # Print the result
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")
    
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9 , ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    result = sol.addTwoNumbers(l1, l2)
    
    # Print the result
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")