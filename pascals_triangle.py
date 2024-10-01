class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []

        def helper(num):
            dummy = []
            for i in range(num + 1):
                if i == 0:
                    dummy.append(1)
                elif i == num:
                    dummy.append(1)
                else:
                    dummy.append(result[num - 1][i - 1] + result[num - 1][i])
            print(f"{num}: {dummy=}")
            return dummy

        for i in range(numRows):
            print(f"{result=}")
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1, 1])
            else:
                result.append(helper(i))
        return result


solution = Solution()
print(solution.generate(5))
