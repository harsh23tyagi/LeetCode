class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]: -----Leetcode definition
    def productExceptSelf(self, nums):
        opt = []
        opt.append(1)
        for i in range(1, len(nums)):
            opt.append(opt[i-1]*nums[i-1])
        n = len(nums)-1
        optimal = 1
        for j in reversed(range(0, len(nums)-1)):
            opt[j] = opt[j]*optimal*nums[j+1]
            optimal = optimal*nums[j+1]
        return opt


def main():
    sol = Solution()
    nums = [1, 2, 3, 4]
    answer = sol.productExceptSelf(nums)
    print(answer)


if __name__ == "__main__":
    main()
    pass
