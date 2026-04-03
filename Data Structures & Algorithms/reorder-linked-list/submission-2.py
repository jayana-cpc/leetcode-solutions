# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        print("hi")
        # 1 2 3 4 5
                # s
                #       f      
        # Find middle point
        f = head
        s = head 

        while f and f.next:
            s = s.next
            f = f.next.next
        mid = s

        print("Found middle")

        # Reverse second half
        curr = mid
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        print("Reversed")
        # Merge Lists
        # 1 -> 2
        # 4 -> 3 ->  Null
        tail = prev # 4 3
        curr = head # 1 4 2 3
        # print(curr.next.val, tail.next.val)

        while tail and curr.next: 
            hxt = curr.next # 3 
            curr.next = tail
            tail = tail.next
            curr = curr.next
            if hxt != curr:
                curr.next = hxt
                curr = curr.next
    # 1 -> 4 -> 2 -> 3 -> 3

            


        




        
