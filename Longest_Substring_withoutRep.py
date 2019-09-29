class Solution:
    def solution_O_N_space(self, s):
        arr = {}
        if (len(s) <= 1):
            return len(s)
        for i in range(97, 123):
            arr[i] = False

        start = 0
        end = 0
        length = len(s)
        sub_length = 1
        arr[ord(s[start])] = True
        end += 1
        max_length = 0

        while(end < length):
            if ord(s[end]) not in arr:
                arr[ord(s[end])] = False
            if not arr[(ord(s[end]))]:
                arr[(ord(s[end]))] = True
                end += 1
                sub_length += 1
                max_length = max(max_length, sub_length)
            else:
                if(start == end):
                    sub_length = 1
                    end += 1
                else:
                    arr[(ord(s[start]))] = False
                    start += 1
                    max_length = max(max_length, sub_length)
                    sub_length -= 1
        return max_length

    def O_1_space(self, s):
        seen = ""
        max_length = 0
        for i in s:
            if i in seen:
                seen = seen[seen.index(i)+1:]
                max_length = max(max_length, len(seen))
                seen += i
            else:
                seen += i
                max_length = max(max_length, len(seen))
        return max_length

    def lengthOfLongestSubstring(self, s):
        max_length = self.solution_O_N_space(s)
        # faster in python with O(1) space but might be O(n^2) in runtime still faster
        m2 = self.O_1_space(s)
        print(m2)
        return (m2)


if __name__ == "__main__":
    sol = Solution()
    s = "aabc!bb"
    sol.lengthOfLongestSubstring(s)
    pass
