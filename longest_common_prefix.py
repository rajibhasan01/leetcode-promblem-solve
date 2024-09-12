class Solution:
    def longestCommonPrefix(self, strs):
        min_char_len = list(map(len, strs))
        min_char = min(min_char_len)
        index_of_min_word = min_char_len.index(min_char)
        min_word = strs[index_of_min_word]
        i = 0
        count = min_char
        check = 0

        while i < min_char:
            for word in strs:
                if min_word[0 : min_char - i] == word[0 : min_char - i]:
                    check = check + 1
                    continue
                else:
                    check = 0
                    break
            if check == len(strs):
                return strs[0][:count]
            i = i + 1
            count = count - 1
        return strs[0][:count]


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
