class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def has_cycle(head: Node | None) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next          # +1 step
        fast = fast.next.next     # +2 steps
        if slow is fast:          # they met =cycle
            return True
    return False                  # fast hit None =no cycle
