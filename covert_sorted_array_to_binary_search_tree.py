#!/usr/bin/env python3
"""
Convert sorted array to binary search tree.
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Convert a sorted array into binary search tree.
    Convert it to a height-balanced binary search tree.

    Methods:
        sortedArrayToBST(nums): Take a sorted integer array.
    """

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Params:
            :dtype nums: A sorted list of integer.
            :rtype: Optional[TreeNode]
        """
        if len(nums) == 0:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])  # Use the value from nums, not mid
        root.left = self.sortedArrayToBST(nums[:mid])  # Correctly use self
        root.right = self.sortedArrayToBST(nums[mid + 1 :])  # Correctly use self
        return root


def level_order_traversal(node: Optional[TreeNode]) -> List[Optional[int]]:
    """
    This method is to represent the tree in an array.
    """
    if not node:
        return []

    queue = deque([node])
    result = []

    while queue:
        current = queue.popleft()

        if current is not None:
            result.append(current.val)
            queue.append(current.left)  # This can be None, which is acceptable
            queue.append(current.right)  # This can also be None, which is acceptable
        else:
            result.append(None)

    # Optionally trim trailing 'None' values for cleaner output
    while result and result[-1] is None:
        result.pop()

    return result


def run_tests():
    """
    Varify the correctness of solution.sortedArrayToBST methods using some test case.
    """

    solution = Solution()

    test_cases = [
        ([-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5]),  # Test Case 1
        ([1, 3], [3, 1]),  # Test Case 2
        ([1], [1]),  # Test Case 3
        ([], []),  # Test Case 4 (empty array)
        ([0, 1, 2, 3], [2, 1, 3, 0]),  # Test Case 5
    ]

    for i, (nums, expected) in enumerate(test_cases):
        bst_root = solution.sortedArrayToBST(nums)
        output = level_order_traversal(bst_root)
        assert (
            output == expected
        ), f"Test case {i + 1} failed. {nums=}, {expected=} but got {output=}"

    print(f"Congrats! All {len(test_cases)} test case passed.")


if __name__ == "__main__":
    run_tests()
