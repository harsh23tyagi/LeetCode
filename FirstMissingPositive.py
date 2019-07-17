class Solution:
    # def firstMissingPositive(self, nums: List[int]) -> int: --Leetcode defintion
    def firstMissingPositive(self, nums):
        if(len(nums) == 0):
            return 1
        maximum = nums[0]
        dict1 = {}
        for each in nums:
            if(maximum < each):
                maximum = each
            dict1[each] = True
        if(maximum < 1):
            minimum = float("-inf")
        else:
            minimum = float("inf")
        for i in range(1, maximum):
            if i not in dict1:
                minimum = i
                break
        if(minimum == float("inf")):
            minimum = maximum+1
        if(minimum == float("-inf")):
            minimum = 1
        return minimum


def main():
    sol = Solution()
    nums = [7, 8, 9, 11, 12]
    print(sol.firstMissingPositive(nums))


if __name__ == "__main__":
    main()
    pass
