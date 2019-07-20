class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    def findDuplicate(self, nums):
        #         the numbers are between 1 and n
        if(len(nums) == 0):
            return -1
        temp = 0
        count = 0
        recent = temp
        duplicate = 0
        while(temp != len(nums)):
            if(nums[temp] != temp+1):
                k = nums[temp]
                if(nums[k-1] == k):
                    duplicate = k
                    count += 1
                    temp += 1
                else:
                    sim = nums[k-1]
                    nums[k-1] = k
                    nums[temp] = sim
            else:
                temp += 1
        # print(duplicate)
        return duplicate


def main():
    sol = Solution()
    nums = [3, 1, 3, 4, 2]
    print(sol.findDuplicate(nums))


if __name__ == "__main__":
    main()
    pass
