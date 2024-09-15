from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        replace = 1

        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[replace] = nums[i]
                replace += 1
        return replace


def run_tests():
    """
    This method is written for verifying correctness of solution.removeDuplicates() methods.
    """
    test_cases = [
        ([1, 1, 2], 2, [1, 2]),  # Test Case 1
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),  # Test Case 2
    ]

    solution = Solution()
    for nums, expected_k, expected_arr in test_cases:
        result = solution.removeDuplicates(nums)
        print(
            f"Nums: {nums}, Expected_K: {expected_k}, "
            f"Expected_Array: {expected_arr}, Result: {result}"
        )

        assert result == expected_k, f"Expected {expected_k} but got {result}"
        for i in range(expected_k):
            assert (
                nums[i] == expected_arr[i]
            ), f"Expected_Array: {expected_arr} But got Array: {nums}"

    print("Congrats! All test case passed.")


if __name__ == "__main__":
    run_tests()
