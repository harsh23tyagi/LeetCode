class Solution:
    def threeSum(self, nums):
        nums.sort()
        finalList = []
        sumfind = 0
        for i in range(len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue  # because they are going to create same pairs
                # because i have already created all the pairs that include nums[i]
            j, k = i+1, len(nums)-1

            while(j < k):
                if(nums[i]+nums[j]+nums[k]) > sumfind:
                    k -= 1
                elif(nums[i]+nums[j]+nums[k] < sumfind):
                    j += 1
                else:
                    li = [nums[i], nums[j], nums[k]]
                    if len(finalList) == 0:
                        finalList.append(li)
                    elif finalList[-1] != li:
                        finalList.append(li)
                    k -= 1
                    j += 1

        return (finalList)


if __name__ == "__main__":
    sol = Solution()
    arr = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    answer = sol.threeSum(arr)
    print(answer)
    pass
