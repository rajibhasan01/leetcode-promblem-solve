class Solution:
    """
    :type s: str
    :rtype: bool
    """

    def isValid(self, s: str) -> bool:
        open_braces = ["(", "{", "["]
        close_braces = [")", "}", "]"]

        if len(s) % 2 != 0:
            return False

        if len(s):
            if s[0] in close_braces:
                return False
            if s[-1] in open_braces:
                return False

        stacks = []
        prev = ""

        for i, char in enumerate(s):
            if s[i] in open_braces:
                stacks.append(char)
                prev = stacks[-1]

            if s[i] in close_braces:
                if prev in open_braces and close_braces.index(
                    char
                ) == open_braces.index(prev):
                    stacks.pop()
                    if stacks:
                        prev = stacks[-1]
                    else:
                        prev = ""
                else:
                    stacks.append(char)

        if not stacks:
            return True
        return False


def run_test():
    """
    Run this test case to varifing the correctness of solution.isValid mehtods.
    """
    test_cases = [
        ("()", True),  # Test Case 1
        ("()[]{}", True),  # Test Case 2
        ("(]", False),  # Test Case 3
        ("[]", True),  # Test Case 4
        ("(){}}{", False),  # Test Case 5
        ("({{{{}}}))", False),  # Test Case 6
        ("(([]){})", True),  # Test Case 7
        ("()))", False),
    ]

    solution = Solution()
    for parentheses, expected in test_cases:
        result = solution.isValid(parentheses)
        print(f"Parentheses: {parentheses}, Result: {result}, Expected:{expected}")
        assert (
            result == expected
        ), f"Parentheses: {parentheses}, Result: {result}. But Expected:{expected}"
    print("Congrats! All the test case passed.")


if __name__ == "__main__":
    run_test()
