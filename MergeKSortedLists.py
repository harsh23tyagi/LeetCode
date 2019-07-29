# Definition for singly-linked list.
import sys


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MinHeap:
    def __init__(self, items):
        self.heap = [0]
        for each in items:
            self.heap.append(each)
            self._heapify(len(self.heap)-1)

    def push(self, data):
        self.heap.append(data)
        self._heapify(len(self.heap) - 1)

    def popMin(self):
        if(len(self.heap) > 2):
            self._swap(1, len(self.heap)-1)
            minimum = self.heap.pop()
            self._bubbledown(1)
        elif(len(self.heap) == 2):
            minimum = self.heap.pop()
        else:
            minimum = False
        return minimum

    def peek(self):
        if(len(self.heap) == 1):
            return False
        else:
            return self.heap[1]

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _heapify(self, index):
        parent = index // 2
        if(index <= 1):
            return
        if(self.heap[parent] > self.heap[index]):
            self._swap(parent, index)
            self._heapify(parent)

    def _bubbledown(self, index):
        left = index*2
        right = index*2 + 1
        minimalIndex = index
        if(left < len(self.heap) and self.heap[left] < self.heap[minimalIndex]):
            minimalIndex = left
        if(right < len(self.heap) and self.heap[right] < self.heap[minimalIndex]):
            minimalIndex = right
        if(minimalIndex != index):
            self._swap(minimalIndex, index)
            self._bubbledown(minimalIndex)


class Solution:
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode
    def mergeKLists(self, lists):
        listFirst = []
        dictionary = {}
        listDict = {}
        sub = 0
        for i in range(len(lists)):
            listDict[i] = lists[i]
            each = lists[i]
            if(each == None):
                sub += 1
                continue
            listFirst.append(each.val)
            if(each.val in dictionary):
                dictionary[each.val].append(i)
            else:
                dictionary[each.val] = [i]
            lists[i] = lists[i].next
        finalNode = ListNode(sys.maxsize)
        header = finalNode
        m = MinHeap(listFirst)
        finalList = []
        count = len(lists)
        count = count - sub
        while(count > 0):
            minimum = m.popMin()
            finalList.append(minimum)
            newNode = ListNode(minimum)
            finalNode.next = newNode
            finalNode = newNode
            listNum = dictionary[minimum].pop()
            if(len(dictionary[minimum]) == 0):
                dictionary.pop(minimum)
            node = lists[listNum]
            if(node == None):
                count -= 1
            else:
                m.push(node.val)
                if(node.val in dictionary):
                    dictionary[node.val].append(listNum)
                else:
                    dictionary[node.val] = [listNum]
                lists[listNum] = lists[listNum].next

        header = header.next

        return header


def createlinkedList(lists):
    finalList = []
    for each in lists:
        if(len(each) == 0):
            finalList.append(None)
            continue

        header = ListNode(each[0])
        finalList.append(header)
        for i in range(1, len(each)):
            temp = ListNode(each[i])
            header.next = temp
            header = header.next
    return finalList


def main():
    lists = [[1, 2, 5], [1, 3, 4], [2, 6]]

    finalList = (createlinkedList(lists))
    sol = Solution()
    answer = (sol.mergeKLists(finalList))
    printAnswer(answer)


def printAnswer(answer):
    finalList = []
    while(answer is not None):
        finalList.append(answer.val)
        answer = answer.next
    print(finalList)


if __name__ == "__main__":
    main()
    pass
