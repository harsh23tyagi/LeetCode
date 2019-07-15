import sys


# Not all questions are done. Only the important ones are done
# Question 1: find unique characters


def calculateUniques(str):
    # we dont have to use any extra data structure- dict can be used in python directly
    d = {}
    for each in str:
        if(d.get(each)):
            return False
        d[each] = True
    return True


# Question 2: Given two strings, check if one is a permutation of the other

def question2(str1, str2):
    if(len(str1) != len(str2)):
        return False

    # The below takes O(nlogn) for each sorting and O(n) for comparison:time
    # The below takes O(n) for each storage or can be done without excess storage
    # stringmain = str(sorted(str1))
    # stringcheck = str(sorted(str2))
    # if(stringmain == stringcheck):
    #     return True
    # else:
    #     return False

    # The below takes O(n) for creating a hashmap or dictionary
    # Another O(n) to check availability of the character
    # O(n) in storage of map
    dict1 = {}
    for each in str1:
        if(each in dict1):
            dict1[each] += 1
        else:
            dict1[each] = 1

    for each in str2:
        if (each not in dict1):
            return False
        if(dict1[each] == 0):
            return False
        dict1[each] -= 1

    return True


def question4(input):  # Check if the permutation of a string is a palindrome or not
    # approach1: count all the characters;
    # if all the characers are in the multiple of 2 then true
    # if all the characers but one is odd are in the multiple of 2 then true
    dict1 = {}
    input = input.lower()
    for each in input:
        if(each == ' '):
            continue
        if each in dict1:
            dict1[each] += 1
        else:
            dict1[each] = 1
    oddCount = 0

    for k, v in dict1.items():
        if(v % 2 != 0):
            oddCount += 1
            if(oddCount > 1):
                # print(oddCount)
                return False
    return True

# def question5(input1, input2):
#     flag = False
#     if(len(input1)== len(input2)):
#         # check replacement
#         for each in range(len(input1)):
#             if(flag):
#                 return False
#             if(input1[each] != input2[each]):
#                 flag = True
#         return True
#     elif((len(input1)-1) == len(input2)):
#         # check insert in input1
#         for each in range(len(input1)):
#             if(flag):
#                 return False
#             if(input1[each] != input2[each]):
#                 flag = True
#         return True
#     elif((len(input2)-1) == len(input1)):
#         # check insert in input2
#     else:
#         return False


def question7(matrix):  # rotate matrix by 90 degrees
    # Doing it in place- without using any other temporary data structures
    # 2 3 4       4 3 1 2
    # 1 2 3       5 4 2 3
    # 3 4 5       2 5 3 4
    # 4 5 2
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
                # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix


def question9(str1, str2):  # check if one string is rotation of the other
    dict1 = {}
    i = 0
    if len(str1) != len(str2):
        return False
    if str1 == str2:
        return True
    for each in str2:
        if(each in dict1):
            dict1[each].append(i)
        else:
            dict1[each] = [i]
        i += 1
    mainStr = ""

    # for each in str1:
    #     if(each not in dict1):
    #         return False
    #     index = dict1[each].pop()
    #     mainStr += str2[index]
    #     if(len(dict1[each]) == 0):
    #         dict1.pop(each)

    for each in dict1[str1[0]]:
        mainStr = str2[:each]+str2[each::]
        mainStr2 = str2[each::]+str2[:each]
        if(mainStr == str1 or mainStr2 == str1):
            return True
    return False


def main():
        # print(str(calculateUniques("Helo"))) # Question 1
        # print(question2('3563476', '7334566'))
        # print(question4('Random Words'))

    # Question 7-----
    # inputMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    # print(inputMatrix)
    # question7(inputMatrix)
    # print(inputMatrix)
    # Question 7-----

    # 'waterbottle', 'erbottlewat' = true
    # 'foo', 'bar' = false
    # 'foo','foofoo'= false
    # 'foooof','foofoo'= false
    # print(question9('abbcbde', 'bdeabbc'))
    pass


if __name__ == "__main__":
    main()
    pass
