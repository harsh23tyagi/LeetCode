class Solution:
    # def maxArea(self, height: List[int]) -> int: ==== Leetcode definition
    def maxArea(self, height):
        left = 1
        right = len(height)
        max_vol = abs(left-right) * min(height[left-1], height[right-1])
        while(left < right):
            if(height[left-1] < height[right-1]):
                left += 1
            else:
                right -= 1
            newarea = abs(left-right) * min(height[left-1], height[right-1])
            if(newarea > max_vol):
                max_vol = newarea
        return max_vol


def main():
    sol = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    answer = sol.maxArea(height)
    print(answer)


if __name__ == "__main__":
    main()
    pass
