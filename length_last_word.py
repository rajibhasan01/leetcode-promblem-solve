class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = len(s)
        k = 0

        while right:
            if s[right - 1] == " " and k:
                return k
            if s[right - 1] != " ":
                k += 1
            right -= 1
        return k


solution = Solution()
print(solution.lengthOfLastWord(""))
