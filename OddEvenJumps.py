class TreeNode:
    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.left = None
        self.right = None


class Solution:
    def addNodesToBST(self, root, val, index, odd_ind, even_ind):
        if not root:
            return
        if(val > root.val):
            if root.right is None:
                node = TreeNode(val, index)
                root.right = node
                return odd_ind, root.index
            else:
                return self.addNodesToBST(root.right, val, index, odd_ind, root.index)
        elif(val < root.val):
            if root.left is None:
                node = TreeNode(val, index)
                root.left = node
                return root.index, even_ind
            else:
                return self.addNodesToBST(root.left, val, index, root.index, even_ind)
        elif (val == root.val):
            return_index = root.index
            root.index = index
            return return_index, return_index

    def oddEvenJumps(self, A):
        countOdd = 1
        opt = [[False, False] for _ in range(len(A))]
        # print(opt)
        curr_index = len(A)-1
        root = TreeNode(A[curr_index], curr_index)
        opt[curr_index] = [True, True]
        curr_index -= 1
        while(curr_index >= 0):
            odd_ind, even_ind = self.addNodesToBST(
                root, A[curr_index], curr_index, -1, -1)
            if odd_ind != -1 and opt[odd_ind][1]:
                opt[curr_index][0] = True
                countOdd += 1
            if even_ind != -1 and opt[even_ind][0]:
                opt[curr_index][1] = True
            curr_index -= 1
        return countOdd


if __name__ == "__main__":
    sol = Solution()
    A1 = [10, 13, 12, 14, 15]
    A2 = [2, 3, 1, 1, 4]
    A3 = [5, 1, 3, 4, 2]
    print(sol.oddEvenJumps(A1))
    pass
