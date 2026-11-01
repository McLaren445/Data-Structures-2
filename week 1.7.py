#Validate a Binary Search Tree
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Node | None) -> bool:
    def check(node, low, high):
        if node is None:
            return True
        # current node must lie strictly between low and high
        if node.val <= low or node.val >= high:
            return False
        # left subtree: upper bound becomes node.val
        # right subtree: lower bound becomes node.val
        return (check(node.left, low, node.val) and
                check(node.right, node.val, high))

    return check(root, float("-inf"), float("inf"))