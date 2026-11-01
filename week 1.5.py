#mini stack
class MinStackO1:
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, x):
        if not self.stack:
            self.stack.append(0)      # diff is 0 for the first element
            self.min_val = x
        else:
            self.stack.append(x - self.min_val)   # store diff
            if x < self.min_val:
                self.min_val = x      # update min

    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        diff = self.stack.pop()
        # If diff < 0, the popped value was the minimum = restore old min
        if diff < 0:
            self.min_val = self.min_val - diff
        if not self.stack:
            self.min_val = None

    def top(self):
        if not self.stack:
            raise IndexError("top from empty stack")
        diff = self.stack[-1]
        # If diff < 0, top is the current min; else it's min + diff
        return self.min_val if diff < 0 else self.min_val + diff

    def get_min(self):
        if self.min_val is None:
            raise IndexError("get_min from empty stack")
        return self.min_val