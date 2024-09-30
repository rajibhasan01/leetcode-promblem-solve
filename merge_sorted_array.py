class Solution:
    """
    Finding the sorted array from merging two non-decreasing array.

    Methods:
        merge(nums1, m, nums2, n): Two integer arrays nums1 and nums2 and
        m and n represent the number of elements in nums1 and nums2. This
        method return the sorted array from merge this two array.
    """

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        This method sort and merge two non-descreasing array
        Params:
            :dtype nums1: A list of integer.
            :dtype m: integer
            :dtype nums2: A list of integer.
            :dtype n: integer
            :rtype: None
        """
        nums1[m : m + n] = nums2
        nums1.sort()
        return None


def run_test():
    """
    This method is to varify the correctness of solution.merge class.
    """
    test_case = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),  # Test Case 1
        ([1], 1, [], 0, [1]),  # Test Case 2
        ([0], 0, [1], 1, [1]),  # Test Case 3
    ]

    solution = Solution()
    for nums1, m, nums2, n, expected in test_case:
        solution.merge(nums1, m, nums2, n)
        assert (
            nums1 == expected
        ), f"{nums1=}, {m=}, {nums2=}, {n=}, {expected=} but got {nums1=}"
    print(f"Congrats! All {len(test_case)} test case passed.")


if __name__ == "__main__":
    run_test()
