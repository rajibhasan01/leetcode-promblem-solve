class Solution:
    """
    Solution for finding the index of the first occurrence in a string.

    Methods:
        strStr(haystack, needle): Find and then the first index if there is a match of needle in haystack.
    """

    def strStr(self, haystack: str, needle: str) -> int:
        """
        Find the index of the first occurrence of needle in the haystack.

        Params:
            :dtype haystack: Input String
            :dtype needle: Input String
            :rtype: Return Matched Index
        """
        if len(needle) >= len(haystack) and needle != haystack:
            return -1

        left = 0
        right = len(needle)

        while left >= 0 and right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            left += 1
            right += 1
        return -1


def run_tests():
    """
    This method is to checking the correctness of the Solution.solution methods.
    """
    solution = Solution()

    test_cases = [
        ("sadbutsad", "sad", 0),  # Test Case 1
        ("leetcode", "leeto", -1),  # Test Case 2
        ("rajibhasan", "jib", 2),  # Test Case 3
        ("abdulovi", "ovi", 5),  # Test Case 4
    ]

    for haystack, needle, expected in test_cases:
        result = solution.strStr(haystack, needle)
        assert (
            result == expected
        ), f"Haystack: {haystack}, Needle: {needle}, Expected: {expected}. But get {result}"
    print(f"Congrats! Passed all {len(test_cases)} test cases.")


if __name__ == "__main__":
    run_tests()
