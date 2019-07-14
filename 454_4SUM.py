class Solution:
    # def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    def fourSumCount(self, A, B, C, D):
        dictA = {}
        dictB = {}
        dictC = {}
        dictD = {}
        dictAB = {}
        sum = 0
        for i in range(len(A)):
            if A[i] in dictA:
                dictA[A[i]] += 1
            else:
                dictA[A[i]] = 1
            if B[i] in dictB:
                dictB[B[i]] += 1
            else:
                dictB[B[i]] = 1
            if C[i] in dictC:
                dictC[C[i]] += 1
            else:
                dictC[C[i]] = 1
            if D[i] in dictD:
                dictD[D[i]] += 1
            else:
                dictD[D[i]] = 1

        for itemA in dictA:
            for itemB in dictB:
                anb = itemA + itemB
                if anb in dictAB:
                    dictAB[anb] += dictA[itemA]*dictB[itemB]
                else:
                    dictAB[anb] = dictA[itemA]*dictB[itemB]

        for itemC in dictC:
            for itemD in dictD:
                anb = -itemC-itemD
                if anb in dictAB:
                    sum += dictAB[anb]*dictC[itemC]*dictD[itemD]
        return sum

# Eg.
# [1,2]
# [-2,-1]
# [-1,2]
# [0,2]

# Output:
# 2


if __name__ == "__main__":
    sol = Solution()
    count = sol.fourSumCount(A=[1, 2], B=[-2, -1], C=[-1, 2], D=[0, 2])
    print(count)
    pass
