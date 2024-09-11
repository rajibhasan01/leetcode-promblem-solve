class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_rules_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        double_digit_dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        i = 0
        total = 0
        string_length = len(s)

        while i < string_length:
            if i + 1 < string_length:
                if s[i] + s[i + 1] in double_digit_dict:
                    total = total + double_digit_dict[s[i] + s[i + 1]]
                    i += 2
                    continue
            total = total + roman_rules_dict[s[i]]
            i += 1

        return total


def run_test():
    """
    Runs predefined test case for varify the correctness of solution.romanToInt methods.
    """
    solution = Solution()
    test_cases = [
        ("III", 3),  # Test Case 1
        ("LVIII", 58),  # Test Case 2
        ("MCMXCIV", 1994),  # Test Case 3
        ("XVII", 17),  # Test Case 4
        ("CMXX", 920),  # Test Case 5
    ]

    for roman_num, expected in test_cases:
        result = solution.romanToInt(roman_num)
        print(f"Roman Nums: {roman_num}, Exepected: {expected}, Result: {result}")
        assert (
            result == expected
        ), f"FAILED. Roman Nums: {roman_num}, Expected: {expected}, but got Result: {result}"
        print("Congrats! All test case passed")


if __name__ == "__main__":
    run_test()
