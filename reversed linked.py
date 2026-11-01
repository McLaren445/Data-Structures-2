def reverse_list_recursive(head):
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head  # make next node point back to us
    head.next = None  # cut our old forward link
    return new_head