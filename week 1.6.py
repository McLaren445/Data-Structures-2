#Implement a Dynamic Array
class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None] * self.capacity   # fixed-size buffer

    def append(self, x):
        if self.size == self.capacity:       # full → double
            self._resize(self.capacity * 2)
        self.data[self.size] = x
        self.size += 1

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]       # copy old items
        self.data = new_data
        self.capacity = new_capacity

    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("index out of range")
        return self.data[i]

    def set(self, i, x):
        if i < 0 or i >= self.size:
            raise IndexError("index out of range")
        self.data[i] = x