# Not a very efficient code to calculate the expressions using postfix orientation
# Converts infix to postfix while calculating intermediate results


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def getLast(self):
        return self.items[-1]


class Solution:
    def getPriority(self, elem):
        if(elem == "-" or elem == "+"):
            return 1
        if(elem == "*" or elem == "/"):
            return 2
        if(elem == '(' or elem == ')'):
            return 0
        else:
            return -1

    def perform(self, operand1, operand2, symbol):
        if(symbol == '-'):
            return operand1-operand2
        if(symbol == '+'):
            return operand1+operand2
        if(symbol == '*'):
            return operand1*operand2
        if(symbol == '/'):
            return operand1/operand2

    def calculate(self, s):
        sol = Solution()
        i = 0
        stack = Stack()
        postFix = Stack()
        final = s.replace(' ', '')
        bring = ""
        list1 = []
        while(i < len(final)):
            if(final[i].isdigit()):
                bring += final[i]

            else:
                alpha = final[i]

                list1.append((bring))
                list1.append(alpha)
                bring = ""
            i += 1

        stack.push('(')
        if(bring):
            list1.append((bring))
        if(len(list1) == 1):
            return list1[0]
        if(len(list1) == 0):
            return 0
        list1.append(")")
        answer = 0

        for i in range(0, len(list1)):
            each = list1[i]
            if(each.isdigit()):
                postFix.push(each)
                # print(postFix.getLast())
            else:
                if(each == ')'):
                    # print("Stack Last: "+stack.getLast())
                    while(stack.getLast() != '('):
                        symbol = stack.pop()
                        operand2 = int(postFix.pop())
                        operand1 = int(postFix.pop())
                        # print(symbol, operand1, operand2)
                        answer = sol.perform(operand1, operand2, symbol)
                        postFix.push(answer)
                        # print(answer)
                        # print("=====")
                elif(sol.getPriority(each) > sol.getPriority(stack.getLast())):
                    stack.push(each)
                    # print(each+"===Pushed")
                else:
                    # print(each+"Hhhh")

                    while(sol.getPriority(stack.getLast()) >= sol.getPriority(each)):

                        symbol = stack.pop()
                        operand2 = int(postFix.pop())
                        operand1 = int(postFix.pop())
                        answer = sol.perform(operand1, operand2, symbol)
                        postFix.push(answer)
                        # print(answer, operand1, operand2, symbol)
                        # print("Intermediate: "+str(answer))
                    stack.push(each)
        # print(answer)

        return int(answer)


def main():
    sol = Solution()
    s = " 45*45 + 54/ 54 "
    print(sol.calculate(s))


if __name__ == "__main__":
    main()
    pass
