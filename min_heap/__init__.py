class MinHeap:
    def __init__(self, list_count):
        self.list_count = list_count
        self.heap = [None] * (list_count+1)
        self.current_last = 0

    def __repr__(self):
        return f'heap: {self.heap}'

    def insert(self, value_with_head_index):
        value = value_with_head_index["value"]
        i = self.current_last + 1  # the index of the node which is going to be inserted
        self.current_last += 1

        if i > self.list_count:
            print('The heap is full')
            return

        while i != 1 and value < self.heap[int(i / 2)]["value"]:  # i == 1 means this node should be root
            self.heap[i] = self.heap[int(i / 2)]
            i = int(i / 2)
        self.heap[i] = value_with_head_index

    def pop(self):
        if self.is_empty():
            return 'The heap is empty, cannot pop'

        root = self.heap[1]  # Target to return
        last_element = self.heap[self.current_last]
        self.current_last -= 1

        cur = 1
        child = 2
        while child <= self.current_last:
            if child < self.current_last and self.heap[child + 1]["value"] < self.heap[child]["value"]:
                child += 1  # move to right child if right child is smaller

            if last_element["value"] <= self.heap[child]["value"]:
                break

            self.heap[cur] = self.heap[child]
            cur = child
            child *= 2  # find next left child

        self.heap[cur] = last_element
        return root

    def is_empty(self):
        return self.current_last == 0
