import copy


class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    def longestConsecutive(self, nums):
        dict1 = {}
        if(len(nums) == 0):
            return 0
        minimum = nums[0]
        for index in range(len(nums)):
            each = nums[index]
            dict1[each] = index
            if(each < minimum):
                minimum = each
        c = 0
        start = minimum
        length = 0
        end = minimum
        maximumlength = 0
        while(dict1):
            # print(str(start)+"--"+str(end))
            # print(dict1)
            initialstart = (start)
            initialend = (end)
            flag1 = True
            flag2 = True
            # print("Initials:"+str(initialstart)+", "+str(initialend))
            # length += 1
            # print("Final:"+str(start)+", "+str(end))
            if(end+1 in dict1):
                length += 1
                dict1.pop(end)
                # print("Popped Out end:"+str(end)+" at "+str(c))
                end += 1
                flag1 = False
                # print("ENTERED")

            c += 1
            if(start-1 in dict1):
                length += 1
                flag2 = False
                try:
                    dict1.pop(start)
                    # print("Popped Out start:"+str(start)+" at "+str(c))
                except:
                    pass
                start = start-1
            if(flag1 and flag2):
                length += 1
            # print("Final:"+str(start)+", "+str(end))
            if(initialstart-1 not in dict1 and initialend+1 not in dict1):

                try:

                    dict1.pop(start)
                    # length += 1
                    dict1.pop(end)
                    # length +=1

                except:
                    pass
                if(len(dict1) != 0):
                    start = list(dict1.keys())[0]
                    end = list(dict1.keys())[0]
                if(maximumlength < length):
                    maximumlength = length
                length = 0
            # print(c)
        # print(maximumlength)
        return maximumlength


def main():
    sol = Solution()
    nums = [-7, -1, 3, -9, -4, 7, -3, 2, 4, 9, 4, -
            9, 8, -7, 5, -1, -7]  # [2, 1, 4, 5, 6, 17]
    print(sol.longestConsecutive(nums))


if __name__ == "__main__":
    main()
    pass
