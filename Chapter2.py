# Implementing LinkedList in python


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None    # Initially linkedlist pointer points to nothing

# ==================================================================+Question 1+=============================================================================


def removeDuplicates(firstNode):
    # we have to remove duplicates without using a temporary buffer or a dictionary
    while(firstNode.next is not None):
        current = firstNode.next
        prev = firstNode
        while(current.next is not None):
            if(current.val == firstNode.val):
                prev.next = current.next
                current = firstNode.next
            else:
                current = current.next
                prev = prev.next
        if(current.val == firstNode.val):
            prev.next = current.next

        firstNode = firstNode.next
        # print(firstNode.val)

# ==================================================================+Question 2+=============================================================================


def kthFrmRight(firstNode, k):
    kth = firstNode
    current = firstNode
    i = 1
    while(current.next is not None):
        if(i > k):
            kth = kth.next
        current = current.next
        i += 1
    if(i <= k):
        return 0, False
    else:
        kth = kth.next
        return kth.val, True


count = 0


def kthFrmRight_Recursive(firstNode, k, count):

    firstNode = firstNode.next
    if(firstNode.next is None):
        return
    count += 1
    kthFrmRight_Recursive(firstNode, k, count)
    count -= 1

    if (count == k):
        # print(count)
        print(firstNode.val)
        # return firstNode.val

    # ==================================================================+Question 3+=============================================================================
    # rather than finding previous node let's iterate it over the entire linked list from the middle node


def deletingMiddleNode(midlenode):
    while(midlenode.next.next is not None):
        midlenode.val = midlenode.next.val
        midlenode.next = midlenode.next.next
    pass

# ==================================================================+Question 4+=============================================================================


def partition(firstNode, partition):

    nodeBegin = None
    nodeTail = None
    count = 0
    begin = None  # We just maintain one head pointer
    while(firstNode.next is not None):
        if(firstNode.val < partition):
            if(nodeBegin is None):
                nodeBegin = Node(firstNode.val)
                begin = nodeBegin
            else:
                temp = Node(firstNode.val)
                nodeBegin.next = temp
                nodeBegin = temp
        elif(firstNode.val > partition):
            if(nodeTail is None):
                nodeTail = Node(firstNode.val)
            else:
                temp = Node(firstNode.val)
                temp.next = nodeTail
                nodeTail = temp
        else:
            count += 1  # we will insert the partition number in the end in single for loop

        firstNode = firstNode.next

    for each in range(count):
        temp = Node(partition)
        nodeBegin.next = temp
        nodeBegin = nodeBegin.next

    nodeBegin.next = nodeTail
    printList(begin, inline=True)
    # printList(nodeTail, inline=True)
    pass


# ==================================================================+Question 5+=============================================================================
newList = []  # if we want to return in a list
begin = Node(None)  # if we want to return in linked list

count = 1  # for setting up the initial head pointer

head = None  # stores the head pointer


def sumlists(l1, l2, carry):
    global newList, count, begin, head
    # print(str(l1.val)+":"+str(l2.val))
    sum_elem = (l1.val + l2.val + carry) % 10
    carry = (l1.val + l2.val)/10
    newList.append(sum_elem)
    if count == 1:
        begin.val = sum_elem
        head = begin
        count += 1
    else:
        begin.next = Node(sum_elem)
        begin = begin.next

    # begin.next = Node(None)
    # begin.val = sum_elem
    # begin = begin.next

    if(l1.next is None and l2.next is None):
        if carry != 0:
            # =======================DIsplaying in List==============================
            # newList.append(carry) # use this line if you want to display last carry over
            # or
            # newList[len(newList)-1] = newList[len(newList)-1]+10*carry

            # =======================DIsplaying in linkedList==============================
            # begin.next = Node(carry)

            # begin = begin.next
            # ==============or if display carry over in the same node comment the above two lines and uncomment the below=======
            # begin.val = begin.val + (10*carry)

            pass
        return newList
    l1 = l1.next
    l2 = l2.next
    sumlists(l1, l2, carry)


# ==================================================================+Question 6+=============================================================================
# This is an interesting question- I want to use recursion in this approach, if the length of the list is known
# If the length of the list is unknown then it would be wise to use reversal and comparison or maybe slow runner and fast runner method
flag = False
mid = None
answer = True


def palindromeString(node, length):
    global mid, answer
    if(length == 0 or length == 1):
        if (length == 1):
            mid = node.next
        else:
            mid = node  # didnt check this part
        return
    # Recursion
    palindromeString(node.next, length-2)

    if(mid.val != node.val):
        # print("Unequal for- Mid Value: "+str(mid.val) +
        #       ", Node Value: "+str(node.val))
        answer = False
        mid = mid.next
    else:
        mid = mid.next
# The stack will be running for every element anyway, so we declare a global variable and set the answer in that


# ==================================================================+Question 7+=============================================================================
# Intersection of two linkedlists based on the reference and not on value
# We can use hash table or dictionary in python
def intersectionDetection(l1, l2):
    dict1 = {}
    # Searching in dictionary is O(1)
    # O(m+n) where m and n are lengths of linkedlists
    # O(n) space complexity to store dictionary
    while(l1.next is not None):
        dict1[l1] = l1.val
        l1 = l1.next
    dict1[l1] = l1

    while(l2.next is not None):
        l2 = l2.next
        if(l2 in dict1):
            return True, l2.val, l2

    if(l2 in dict1):
        return True, l2.val, l2
    return False, None

# Space complexity in the above easy function was O(n).
# Space complexity in this new function is O(1)
# Time complexity in both is O(m+n)


def intersectionDetectionWithreducedSpaceComplexity(l1, l2):
    length1 = 0
    length2 = 0
    begin1 = l1
    begin2 = l2
    while(l1.next is not None):
        l1 = l1.next
        length1 += 1
    length1 += 1
    while(l2.next is not None):
        l2 = l2.next
        length2 += 1
    length2 += 1

    if(l1 != l2):
        return False, None
    diff = abs(length1-length2)
    print("Difference: "+str(diff))
    if (length1 > length2):
        answer = doWork(begin1, begin2, diff)
    else:
        answer = doWork(begin2, begin1, diff)
    return answer


def doWork(l1, l2, diff):
    while(l2 is not None):
        beg = l1
        for i in range(diff+1):
            if(l1 is not None):
                if(l1 == l2):
                    print("Intersecting node: "+str(l2.val))
                    return l2.val, True
                l1 = l1.next

            pass
        l1 = beg.next
        l2 = l2.next
    # print(l2.val)
    return None, False


def main():

    # ==========================+Question 1 & 2 Inputs+====================================
    # node1 = Node(12)
    # node2 = Node(14)
    # node3 = Node(16)
    # node4 = Node(14)
    # node5 = Node(18)
    # node6 = Node(19) #These inputs are good  to check question 2
    #
    #
    #
    #
    # ==========================+Question 4 Inputs+====================================
    # node1 = Node(3)
    # node2 = Node(5)
    # node3 = Node(8)
    # node4 = Node(5)
    # node5 = Node(10)
    # node6 = Node(2)
    # node7 = Node(1)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5
    # node5.next = node6
    # node6.next = node7 # These inputs are good to question 4
    #
    #
    #
    #
    # ==========================+Question 5 Inputs+====================================
    # node1 = Node(4)  # Node(7)
    # node2 = Node(0)  # Node(1)
    # node3 = Node(9)  # Node(6)

    # node_1 = Node(3)  # Node(5)
    # node_2 = Node(0)  # Node(9)
    # node_3 = Node(9)  # Node(2)

    # node1.next = node2
    # node2.next = node3

    # node_1.next = node_2
    # node_2.next = node_3

    # inputs above are good for question 5
    #
    #
    #
    #
    # ==========================+Question 6 Inputs+====================================

    # node1 = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # node4 = Node(4)
    # node5 = Node(5)
    # node6 = Node(4)
    # node7 = Node(3)
    # node8 = Node(8)
    # node9 = Node(1)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5
    # node5.next = node6
    # node6.next = node7
    # node7.next = node8
    # node8.next = node9
    # inputs above are good for question 6
    #
    #
    #
    #
    # ==========================+Question 7 Inputs+====================================

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    # node9 = Node(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node7.next = node8
    node8.next = node1
    # node9.next = node5

    # node1 = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # node4 = Node(4)
    # node5 = Node(5)
    # node6 = Node(4)
    # node7 = Node(18)
    # node8 = node2
    # node9 = Node(18)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node5.next = node6
    # node6.next = node7
    # node7.next = node8
    # node8.next = node9

    #
    #
    #
    #
    #
    #
    #
    # Uncomment the following for the questions one by one
    # =========Question 1===============
    # removeDuplicates(node1)
    # printList(node1, inline=True)

    # ========+Question 2+============
    # print(kthFrmRight(node1, 8))  # using sliding window
    # printList(node1, inline=True)
    # (kthFrmRight_Recursive(node1, 2, 0))  # using recursion

    # =========+Question 3+==============
    # printList(node1, inline=True)
    # deletingMiddleNode(node4)
    # printList(node1, inline=True)

    # =========+Question 4+==============
    # partition(node1, 5)

    # =========+Question 5+==============
    # sumlists(node1, node_1, 0)
    # global newList, begin, head
    # print(newList)
    # printList(head, inline=True)

    # =========+Question 6+==============
    # (palindromeString(node1, 9))
    # global answer
    # print(answer)

    # =========+Question 7+==============
    # print(intersectionDetection(node1, node5)) # The space complexity in this one is O(n)
    # print(intersectionDetectionWithreducedSpaceComplexity(node1, node7)) # The space complexity in this one is O(1)
    # Printing Linked List
    # Set inline as true if want to see elements in one list


def printList(node1, inline):
    nextNode = node1
    finalList = []
    while(nextNode.next is not None):
        if(inline):
            finalList.append(nextNode.val)
        else:
            print(nextNode.val)
        nextNode = nextNode.next
    if(inline):
        finalList.append(nextNode.val)
        print(finalList)
    else:
        print(nextNode.val)


if __name__ == "__main__":
    main()
    pass
