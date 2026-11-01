class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next  # save next
        curr.next = prev  # reverse pointer
        prev = curr  # move prev forward
        curr = nxt  # move curr forward
    return prev  # new head
