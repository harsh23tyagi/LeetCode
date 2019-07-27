import sys


class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    def maxSlidingWindow(self, nums, k):

        finalOutput = []
        maximum = -sys.maxsize
        maximumIndex = -1
        if(len(nums) == 0):
            return []

        for l in range(0, k):
            if(nums[l] > maximum):
                maximum = nums[l]
                maximumIndex = l
        finalOutput.append(maximum)
        for i in range(k, len(nums)):
            if(nums[i] > maximum):
                # print(nums[i], i)
                maximum = nums[i]
                maximumIndex = i
            if(maximumIndex <= i-k):
                maximum = -sys.maxsize
                for j in range((i-k+1), i+1):
                    if(maximum < nums[j]):
                        maximum = nums[j]
                        maximumIndex = j
            finalOutput.append(maximum)

        return finalOutput


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    sol = Solution()
    print(sol.maxSlidingWindow(nums, k))


if __name__ == "__main__":
    main()
    pass
