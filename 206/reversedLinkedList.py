# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #intiliaze a new list
        reverse =  None
        curr = head

        # create a new linked list and update it as reverse along the way
        while curr : 
            temp = curr.next            #first store the next node and seperate the current node
            curr.next = reverse         #point the current node to the reverse list 
            reverse = curr              #update the reverse list to the current node
            curr = temp                 #move to the next node in the original list          

        return reverse       