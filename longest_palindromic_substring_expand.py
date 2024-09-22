class Solution:
    """
    Solution to find the longest palindrome substring in a given string.

    Methods:
        longestPalindrome(s): Returns the longest palindromic substring.
        expand_from_center(left, right): Expands around the center to find
        palindromes.
    """

    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in the input string.

        Params:
            :dtype s: Input string
            :rtype: Longest palindromic substring
        """
        self.s = s
        if len(s) <= 1:
            return s

        max_str = self.s[0]
        for i in range(len(self.s)):
            odd = self.expand_from_center(i, i)
            even = self.expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str

    def expand_from_center(self, left: int, right: int) -> str:
        """
        Expands the substring from the center outwards to find palindrome.

        Params:
            :dtype left: Left index of the center
            :dtype right: Right index of the center
            :rtype: Palindromic substring
        """
        while left >= 0 and right < len(self.s) and self.s[left] == self.s[right]:
            left -= 1
            right += 1
        return self.s[left + 1 : right]


def run_tests():
    """
    Check the correctness of the Solution.solution by run the test cases.
    """
    solution = Solution()
    test_cases = [
        ("babad", "bab"),  # Test Case 1
        ("cbbd", "bb"),  # Test Case 2
        ("aba", "aba"),  # Test Case 3
        ("abcd", "a"),  # Test Case 4
    ]
    for string, expected in test_cases:
        result = solution.longestPalindrome(string)
        assert (
            result == expected
        ), f"Input String: {string}, Expected: {expected}. But got {result}"
    print(f"Congrats! Passed all {len(test_cases)} test cases.")


if __name__ == "__main__":
    run_tests()
