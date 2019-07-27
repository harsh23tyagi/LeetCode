import sys


class Solution:
    def __init__(self):
        self.tm = [0]*128
# def minWindow(self, s: str, t: str) -> str:

    def minWindow(self, s, t):
        #         Creating each character count in t
        tm = self.tm
        for each in t:
            tm[ord(each) - ord('A')] += 1

        count = 0
        length = 0
        start = 0
        minLength = sys.maxsize
        minimumSb = ""
        for i in range(0, len(s)):
            char = s[i]
            tm[ord(char) - ord('A')] -= 1
            if(tm[ord(char)-ord('A')] >= 0):
                count += 1
            while(count == len(t)):
                tm[ord(s[start]) - ord('A')] += 1
                if(tm[ord(s[start]) - ord('A')] > 0):
                    count -= 1
                length = i - start + 1
                if(length < minLength):
                    minimumSb = s[start:i+1]
                    minLength = length
                start += 1

        return minimumSb


def main():
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(sol.minWindow(s, t))


if __name__ == "__main__":
    main()
    pass
