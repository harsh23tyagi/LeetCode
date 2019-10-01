import sys


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        dec = -1
        for i in range(len(nums)-1, 0, -1):
            if(nums[i] > nums[i-1]):
                dec = i-1
                break
        if dec == -1:
            nums.sort()
            return

        check = sys.maxsize
        checkInd = -1

        for j in range(dec+1, len(nums)):
            if(nums[j] <= check and nums[j] > nums[dec]):
                check = nums[j]
                checkInd = j

        nums[dec], nums[checkInd] = nums[checkInd], nums[dec]

        start = dec+1
        end = len(nums)-1
        while(start < end):

            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 4, 1, 4, 3, 3]
    sol.nextPermutation(nums)
    print(nums)
    pass

# Logic:
# Find the first decreasing pair from right
# then replace the smaller number with its counterpart towards its right which is just greater than itself
# as soon as you replace you just need to reverse the list from next index of decreased pair
