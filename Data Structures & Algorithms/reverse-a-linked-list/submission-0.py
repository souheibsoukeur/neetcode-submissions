class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_temp = curr.next  # 1. Save the next node
            curr.next = prev       # 2. Reverse the pointer
            prev = curr            # 3. Move 'prev' one step forward
            curr = next_temp       # 4. Move 'curr' one step forward

        return prev  # 'prev' is now the new head of the reversed list