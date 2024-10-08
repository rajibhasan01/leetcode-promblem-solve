#!/usr/env/bin python3
"""
This class is represent the solution of Pascal's Triangle II problems.
"""


class Solution:
    """
    Given an integer rowIndex, return the row of the Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers of
    it's previous row colunms. Example given below...

    Example:
    Input: rowIndex = 3
    Pascal's Output = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    Return: [1, 3, 3, 1]

    Methods:
        getRow(rowIndex): Take integer as rowIndex.
    """

    def getRow(self, rowIndex: int) -> list[int]:
        """
        Params:
            :dtype rowIndex: An integer
            :rtype: A List of integer
        """

        def helper(num):
            dummy = []
            for i in range(num + 1):
                if i == 0:
                    dummy.append(1)
                elif i == num:
                    dummy.append(1)
                else:
                    dummy.append(result[num - 1][i - 1] + result[num - 1][i])
            return dummy

        result = []
        for i in range(rowIndex + 1):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1, 1])
            else:
                result.append(helper(i))
        return result[rowIndex]


def run_test():
    """
    Varifying the correctness of the solution.getRow methods.
    """
    test_cases = [
        (3, [1, 3, 3, 1]),  # Test Case 1
        (4, [1, 4, 6, 4, 1]),  # Test Case 2
        (2, [1, 2, 1]),  # Test Case 3
        (0, [1]),  # Test Case 4
    ]

    solution = Solution()
    for i, (rowIndex, expected) in enumerate(test_cases):
        result = solution.getRow(rowIndex)
        assert (
            result == expected
        ), f"Failed Case: {i}. {rowIndex=}, {expected=}. But got {result=}"
    print(f"Congrats! All {len(test_cases)} test case passed.")


if __name__ == "__main__":
    run_test()
