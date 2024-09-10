class Solution(object):
    def two_sum(self, nums, target):
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a disctionary to store the complement and its index
        num_to_index = {}

        # Iterate over the list of numbers
        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                return [num_to_index[complement], i]

            num_to_index[num] = i

        print("num_to_index", num_to_index)

        # If no solution is found, return an empty list
        return []


def run_tests():
    """
    Runs predefined test cases to verify the correctness of the Solution.two_sum method.
    """
    solution = Solution()

    # Define test cases
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),  # Test case 1
        ([3, 2, 4], 6, [1, 2]),  # Test case 2
        ([3, 3], 6, [0, 1]),  # Test case 3
        ([1, 2, 3, 4, 5], 8, [2, 4]),  # Test case 4
        ([0, -1, 2, -3, 1], -2, [1, 3]),  # Test case 5
    ]

    # Run and print the results for each test case
    for nums, target, expected in test_cases:
        result = solution.two_sum(nums, target)
        print(f"nums: {nums}, target: {target}, result: {result}, expected: {expected}")
        assert (
            result == expected
        ), f"Test failed for nums: {nums}, target: {target}. Expected {expected}, but got {result}"

    print("Congrats! All tests passed.")


# Run the tests
run_tests()
