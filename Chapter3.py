# Stacks and Queueus

# Implementing 3 stacks in one stack

import sys
import copy


class StackImp:
    def __init__(self):
        self.subStack1 = 0
        self.lenStack1 = 0
        self.subStack2 = 0
        self.lenStack2 = 0
        self.subStack3 = 0
        self.lenStack3 = 0
        self.stack = []

    def _push(self, val, stackNum):
        if(stackNum == 1):
            self.stack.insert(self.subStack1, val)
            self.lenStack1 += 1
            self.subStack1 += 1
            self.subStack2 += 1
            self.subStack3 += 1
        elif(stackNum == 2):
            self.stack.insert(self.subStack2, val)
            self.lenStack2 += 1
            self.subStack2 += 1
            self.subStack3 += 1
        elif(stackNum == 3):
            self.stack.append(val)
            self.lenStack3 += 1
            self.subStack3 += 1
        else:
            print("Stack Numbers between 1 and 3")

    def _peek(self, stackNum):
        if(stackNum == 1):
            return self.stack[self.subStack1-1]
        elif(stackNum == 2):
            return self.stack[self.subStack2-1]
        elif(stackNum == 3):
            return self.stack[self.subStack3-1]
        else:
            print("Stack Numbers between 1 and 3")

    def _pop(self, stackNum):
        if(stackNum == 1):
            if(self.lenStack1 == 0):
                return "Stack Empty"
            else:
                value = self.stack.pop(self.subStack1-1)
                self.subStack1 -= 1
                self.lenStack1 -= 1
                if(self.subStack2 != 0):
                    self.subStack2 -= 1
                if(self.subStack3 != 0):
                    self.subStack3 -= 1
                return value
        elif(stackNum == 2):
            if(self.lenStack2 == 0):
                return "Stack Empty"
            else:
                value = self.stack.pop(self.subStack2-1)
                self.subStack2 -= 1
                self.lenStack2 -= 1
                if(self.subStack3 != 0):
                    self.subStack3 -= 1
                return value

        elif(stackNum == 3):
            if(self.lenStack3 == 0):
                return "Stack Empty"
            else:
                value = self.stack.pop(self.subStack3-1)
                self.lenStack3 -= 1
                self.subStack3 -= 1
                return value

    def _wholeStack(self):
        return self.stack

    # ------------------The below section is for question 1------------------
    def pushing(self):
        self._push(3, 1)
        self._push(4, 2)
        self._push(5, 3)
        self._push(5, 1)
        self._push(8, 3)
        self._push(7, 2)

    def peeking(self):
        print(self._peek(1))
        print(self._peek(2))
        print(self._peek(3))

    def popping(self):
        # print(stack._pop(1))
        # print(stack._pop(2))
        # print(stack._pop(3))
        # print("-----------------")
        # print(stack._pop(3))
        # print(stack._pop(3))
        # print(stack._pop(1))
        # print("-----------------")
        # print(stack._pop(1))
        # print(stack._pop(2))
        # print(stack._pop(3))
        print(self._pop(3))
        print(self._pop(3))
        print(self._pop(3))
        print(self._pop(3))
        pass
# ------------------ Question1 Section Ends ------------------


# ------------------------Question 2--------------------------
class StackQuestion2:
    def __init__(self):
        self.stack = []
        self.minimum = sys.maxsize

    def _push(self, val):
        self.stack.append(val)
        self.checkMinimum(val)

    def checkMinimum(self, val):
        if(self.minimum > val):
            self.minimum = val

    def getMinimum(self):
        if(self.minimum == sys.maxsize):
            return "Stack Empty.."
        return self.minimum

    def peek(self):
        if(self.stack == []):
            return "Stack Empty"
        return self.stack[len(self.stack)-1]

    def pushingAndMinimum(self):
        print(self.getMinimum())
        self._push(3)
        print(self.getMinimum())
        self._push(8)
        print(self.getMinimum())
        self._push(9)
        print(self.getMinimum())
        self._push(1)
        print(self.getMinimum())
        self._push(16)
        print(self.getMinimum())

# ------------------------Question 2 Ends--------------------------

# Implementing queue using two stacks

# ------------------------Question 4--------------------------


class QueueQuestion4:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def _push(self, val):
        self.stack1.append(val)

    def _pop(self):
        if(self.stack2 == [] and self.stack1 == []):
            return "Stack Empty"
        if(self.stack2 == []):

            for i in range(0, len(self.stack1)):
                val = self.stack1.pop()
                self.stack2.append(val)

            return self.stack2.pop()
        else:
            return self.stack2.pop()

    def _printStacks(self):
        print("Stack1: ")
        print(self.stack1)
        print("Stack2: ")
        print(self.stack2)
        print("-----")

# ------------------------Question 4 Ends--------------------------


# ------------------------Question 5: Sort Stack using only one additional stack-------------------------
class StackSortQ5:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def _push(self, val):
        if(self.stack1 == [] and self.stack2 == []):
            self.stack2.append(val)
        else:
            if(self.stack2[len(self.stack2)-1] <= val):
                self.stack2.append(val)
            else:
                self.stack1.append(val)

    def _sort(self):
        if(self.stack1 == [] and self.stack2 != []):
            return self.stack2

        else:
            while(self.stack1 != []):
                val = self.stack1.pop()
                while(self.stack2[len(self.stack2)-1] > val):
                    v2 = self.stack2.pop()
                    self.stack1.append(v2)
                    if(len(self.stack2) == 0):
                        break
                self.stack2.append(val)

    def _printingStacks(self):
        print("Stack1: ")
        print(self.stack1)
        print("Stack2: ")
        print(self.stack2)
        print("-----")

# ------------------------Question 5 Ends--------------------------

# ------------------------Question 6: Cats and Dogs using Linkedlist implementing stacks-------------------------


class Node:
    def __init__(self, val, type):
        self.val = val
        self.type = type
        self.next = None
        self.nextType = None


class SelectStackQ6:
    def __init__(self):
        self.animal = None
        self.dog = None
        self.cat = None
        self.initial_dog = None
        self.initial_cat = None
        self.initial = None
        pass

    def _enqueue(self, animalName, animalType):
        if(self.animal is None):
            self.animal = Node(val=animalName, type=animalType)
            self.initial = self.animal
            if(animalType.lower() == 'cat'):
                self.cat = self.animal
                self.initial_cat = self.cat
            elif(animalType.lower() == 'dog'):
                self.dog = self.animal
                self.initial_dog = self.dog
        else:
            self.animal.next = Node(val=animalName, type=animalType)
            self.animal = self.animal.next
            if(animalType.lower() == 'cat'):
                if(self.cat is None):
                    self.cat = self.animal
                    self.initial_cat = self.cat
                else:
                    self.cat.nextType = self.animal
                    self.cat = self.cat.nextType
            elif(animalType.lower() == 'dog'):
                if(self.dog is None):
                    self.dog = self.animal
                    self.initial_dog = self.dog
                else:
                    self.dog.nextType = self.animal
                    self.dog = self.dog.nextType

    def _dequeueAny(self):
        # removing initial pointers
        animalType = self.initial.type
        if(animalType.lower() == 'dog'):
            self.initial_dog = self.initial.nextType
        elif(animalType.lower() == 'cat'):
            self.initial_cat = self.initial.nextType
        self.initial = self.initial.next

    def dequeueCat(self):
        name = self.initial_cat.val
        self.initial_cat = self.initial_cat.nextType
        return name

    def dequeueDog(self):
        name = self.initial_dog.val
        self.initial_dog = self.initial_dog.nextType
        return name

    def _printStacks(self, stack):
        if(stack == 'a'):
            print(self.printLinkedList(self.initial, True))
            pass
        elif(stack == 'd'):
            print(self.printLinkedList(self.initial_dog, False))
            pass
        elif(stack == 'c'):
            print(self.printLinkedList(self.initial_cat, False))
            pass
        else:
            print("Wrong Input while printing..")

    def printLinkedList(self, li, ty):
        finalList = []
        while(li is not None):
            finalList.append(li.val)
            if(ty):
                li = li.next
            else:
                li = li.nextType
        return finalList


def main():

    # =========================Question1=========================
    # stack = StackImp()
    # stack.pushing()
    # print(stack._wholeStack())
    # print("=========PEEKING==========")
    # stack.peeking()
    # print("==========================")
    # print("=========Popping=========")
    # stack.popping()
    # print("==========================")

    # =========================Question1 Ends=========================
    # =========================Question2=========================

    # stack2 = StackQuestion2()
    # stack2.pushingAndMinimum()

    # =========================Question2 Ends=========================
    # Question 3 skipped
    # =========================Question4=========================

    # queue = QueueQuestion4()
    # queue._push(4)
    # queue._push(5)
    # queue._push(6)
    # queue._push(8)
    # queue._printStacks()
    # print(queue._pop())
    # queue._push(11)
    # queue._push(12)
    # queue._printStacks()
    # print(queue._pop())
    # print(queue._pop())
    # print(queue._pop())
    # print(queue._pop())
    # print(queue._pop())
    # print(queue._pop())
    # queue._printStacks()

    # =========================Question 4 Ends=========================

    # =========================Question 5 Begins=========================
    # st=StackSortQ5()
    # st._push(7)
    # st._push(1)
    # st._push(3)
    # st._push(8)
    # st._push(12)
    # st._push(10)
    # st._push(5)
    # st._printingStacks()
    # st._sort()
    # st._printingStacks()

    # =========================Question 5 Ends=========================

    # =========================Question 6 Begins=========================
    st = SelectStackQ6()
    st._enqueue('Harry', 'Dog')
    st._enqueue('FirstCat', 'Cat')
    st._enqueue('FirstCatRemoved', 'Cat')
    st._enqueue('FirstRemovedDog', 'dog')
    st._enqueue('Beta4', 'dog')
    st._enqueue('Beta5', 'dog')
    st._enqueue('Beta6', 'Cat')
    st._printStacks('a')
    st._printStacks('d')
    st._printStacks('c')
    print("-------")
    st._dequeueAny()
    st._printStacks('a')
    st._printStacks('d')
    st._printStacks('c')
    print("-------")
    st._dequeueAny()
    st._printStacks('a')
    st._printStacks('d')
    st._printStacks('c')

    st._enqueue('Tom1', 'Cat')
    st._enqueue('Tom2', 'Cat')
    st._enqueue('Joy', 'dog')
    st._enqueue('Alex', 'dog')

    print("-------")
    st._printStacks('a')
    st._printStacks('d')
    st._printStacks('c')

    print("-------")
    print(st.dequeueDog())
    print(st.dequeueCat())
    st._printStacks('a')
    st._printStacks('d')
    st._printStacks('c')
    pass


if __name__ == "__main__":
    main()
    pass
