class Solution:
    """
    Solution for remove element from a given integer array.

    Methods:
        removeElement(nums, val): Take an integer array and a target value
        then return an array where target value is removed.
    """

    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Remove the target value from the given integer array.

        Params:
            :dtype nums: Input integer array
            :dtype val: Input integer value
            :rtype: Return removed array length
        """
        k = 0
        for i, _ in enumerate(nums):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


def run_tests():
    """
    Check the correctness of the Solution.solution methods using some predefine test case.
    """
    solution = Solution()

    test_cases = [
        ([3, 2, 2, 3], 3, [2, 2]),  # Test Case 1
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),  # Test Case 2
        ([1, 4, 4, 5, 2], 4, [1, 5, 2]),  # Test Case 3
        ([1, 2, 3, 4], 1, [2, 3, 4]),  # Test Case 4
    ]

    for nums, target, expected in test_cases:
        result = solution.removeElement(nums, target)
        for i in range(result):
            if nums[i] != expected[i]:
                assert (
                    result == expected
                ), f"Nums: {nums}, Target: {target}, Expected: {expected}. But got {result}"
    print(f"Congrats! Passed all {len(test_cases)} cases.")


if __name__ == "__main__":
    run_tests()
