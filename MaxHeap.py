class MaxHeap:
    # the constructor creates Heap
    def __init__(self, items):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self._heapify(len(self.heap) - 1)

    # The push fucntion appends the element to the end of the heap and then floats it up to the right position
    def push(self, data):
        self.heap.append(data)
        self._heapify(len(self.heap)-1)

    # The peek function gives the maximum of the heap- just displays it- doesn't pop it
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    # The pop functions first takes the maximum of the heap which is at root
    # It then swaps it to the last element
    # Then it pops it out
    # Then it bubbles down the element at the root
    def pop(self):
        if(len(self.heap) > 2):
            self._swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self._bubbleDown(1)
        elif(len(self.heap) == 2):
            max = self.heap.pop()
        else:
            max = False
        return max

    # It basically just swaps the two values using their indices respectively
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        pass

    # It heapifies the value at the index mentioned
    # Heapifies mean to bubble up the element to its currect position
    def _heapify(self, index):
        # Find the parent index
        parent = index // 2  # in a heap the parent is always at index/2 integer value
        if(index <= 1):
            return
        if(self.heap[index] > self.heap[parent]):
            self._swap(index, parent)
            self._heapify(parent)
        pass

    # It bubblesDown the value from the top in the pop function as we excahnge the lower value at the end and put it at the root
    def _bubbleDown(self, index):
        left = index * 2
        right = index*2 + 1
        largestIndex = index
        if(len(self.heap) > left and self.heap[left] > self.heap[largestIndex]):
            largestIndex = left
        if(len(self.heap) > right and self.heap[right] > self.heap[largestIndex]):
            largestIndex = right
        # The largestIndex is the index of the child with the largest value. First it compares the parent with left child
        # If left child value is greater then it stores the index of the child
        # It then compares it to the right child, the max(parent, left)
        # If the largest index is not the same then it means that it has to be brought down
        # Eventually the index would be same as the length of the heap condition would fail
        if(largestIndex != index):
            self._swap(index, largestIndex)
            self._bubbleDown(largestIndex)
        pass


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(nums[:k])
    m = MaxHeap([95, 3, 21])

    m.push(10)
    print(str(m.heap[0:len(m.heap)]))
    print(m.pop())
    m.push(105)

    print(str(m.heap[0:len(m.heap)]))
    print(m.pop())


if __name__ == "__main__":
    main()
    pass
