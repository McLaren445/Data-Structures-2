class QueueFromStacks:
    def __init__(head):
        head.in_stack = []
        head.out_stack = []
    def enqueue(head, x) -> None:
        head.in_stack.append(x)
    def _shift(head):
        if not head.out_stack:
            while head.in_stack:
                head.out_stack.append(head.in_stack.pop())
    def dequeue(head):
        head._shift()
        if not head.out_stack:
            raise IndexError("dequeue from empty queue")
        return head.out_stack.pop()
    def peek(head):
        head._shift()
        if not head.out_stack:
            raise IndexError("peek from empty queue")
        return head.out_stack[-1]

    def is_empty(head) -> bool:
        return not head.in_stack and not head.out_stack

    def __len__(head):
        return len(head.in_stack) + len(head.out_stack)
