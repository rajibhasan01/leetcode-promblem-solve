class Solution:
    """
    Solution to find the position of a given integer in a sorted array of distinct integers.

    Methods:
        searchInsert(nums, target): Returns the position where the target integer would be placed.
    """

    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        Find the target integer position in the sorted nums array.

        Params:
            :dtype list: List of sorted integers
            :dtype target: Integer to find or insert
            :rtype: Index of target if found, or the index where it should be insert
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left


def run_test():
    """
    Check the correctness of the solution.searchInsert methods using some predefined test case.
    """
    solution = Solution()

    test_cases = [
        ([1, 3, 5, 6], 5, 2),  # Test Case 1
        ([1, 3, 5, 6], 2, 1),  # Test Case 2
        ([1, 3, 5, 6], 7, 4),  # Test Case 3
    ]

    for nums, target, expected in test_cases:
        result = solution.searchInsert(nums, target)
        assert (
            result == expected
        ), f"Nums: {nums}, Target: {target}, Expected: {expected}. But got {result}."
    print(f"Congrats! Passed all {len(test_cases)} test cases.")


if __name__ == "__main__":
    run_test()
