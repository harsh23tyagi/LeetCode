class Solution:
    # def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        start = 0
        if(len(s) == 0):
            return 0
        if(k == 0):
            return 0
        begin = s[start]
        distinct = {}
        distinct[s[start]] = 1
        sub = s[start]
        count = 1
        end = 1
        maximum = 1
        length = 1
        while(end < len(s)):
            if(s[end] in distinct):
                distinct[s[end]] += 1
                sub += s[end]
                end += 1
                length += 1
            else:
                count += 1
                if(count > k):
                    start += 1
                    distinct[sub[0]] -= 1
                    if(distinct[sub[0]] == 0):
                        distinct.pop(sub[0])
                        sub = sub[1:] + s[end]
                        distinct[s[end]] = 1
                        end += 1
                        # length += 1

                    else:
                        sub = sub[1:]
                        count -= 1
                        length -= 1
                else:
                    sub += s[end]
                    distinct[s[end]] = 1
                    end += 1
                    length += 1
            if(length > maximum):
                maximum = len(sub)

        return maximum


def main():
    sol = Solution()
    print(sol.lengthOfLongestSubstringKDistinct("eceba", 2))
    # Example: sol.lengthOfLongestSubstringKDistinct("oeropvlmcdvipdfvasskvokdfspivsk", 3)=== answer is 4


if __name__ == "__main__":
    main()
    pass
