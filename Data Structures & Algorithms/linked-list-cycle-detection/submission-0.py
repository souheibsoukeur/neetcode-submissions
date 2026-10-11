# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() 
        temp = head
        if head == None : return False 
        while (temp) : 
            if temp in seen :return True 
            seen.add(temp) 
            temp=temp.next
        return False
        