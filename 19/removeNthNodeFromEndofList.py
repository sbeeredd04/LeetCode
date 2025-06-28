# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #dummy head
        dummy = ListNode(0)
        dummy.next = head

        counter = 0
        while head : 
            counter += 1
            head = head.next
        
        if counter < n :
            return dummy.next

        index, n = 0, counter-n
        head = dummy.next #reset the head
        prev = dummy
        
        #remove the last n -> n = counter - n index
        while head: 
            if index == n : 
                prev.next = head.next
                return dummy.next
            
            prev = head
            head = head.next
            index += 1
        
        return dummy.next
    
# Example usage
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    sol = Solution()
    new_head = sol.removeNthFromEnd(head, n)
    
    # Print the modified list
    while new_head:
        print(new_head.val, end=" -> ")
        new_head = new_head.next
    print("None")