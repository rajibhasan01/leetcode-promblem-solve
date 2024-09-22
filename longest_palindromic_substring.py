class Solution:
    def longestPalindrome(self, s: str) -> str:
        lcs = LCS(s)
        max_len = 0
        ans = ""
        for word in lcs.get_sub_string:
            result = check_palindrome(word)
            if result:
                if len(word) > max_len:
                    ans = word
                    max_len = len(ans)
        return ans


class LCS:
    def __init__(self, data: str) -> None:
        self.__sub_string = set()

        for i in range(len(data)):
            for j in range(len(data)):
                self.__sub_string.add(data[j : j + i + 1])

    @property
    def get_sub_string(self):
        return self.__sub_string


def check_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


solution = Solution()
print(solution.longestPalindrome("a"))
