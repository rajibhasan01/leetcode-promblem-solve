class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        length = len(x)
        right = length - 1

        for i in range(length // 2):
            if x[i] != x[right]:
                return False
            right -= 1
        return True


solution = Solution()
print(solution.isPalindrome(1221))


def run_test():
    """
    Runs predefined test cases to verify the correctness of the Solution.isPalindrome method
    """
    solution = Solution()

    # Define test cases
    test_cases = [
        (1221, True),
        (121, True),
        (1, True),
        (13253, False),
        (1234231, False),
        (22122, True),
    ]

    # Run and print the results for each test case
    for nums, expected in test_cases:
        result = solution.isPalindrome(nums)
        print(f"Nums: {nums}, Result: {result}, Expected: {expected}")
        assert (
            result == expected
        ), f"Test failed for Nums: {nums}, Expected: {expected}, \
        but got {result}"

    print("Congrats! All tests passed")

    # Run the tests


run_test()
