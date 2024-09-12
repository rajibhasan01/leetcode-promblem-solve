class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        right, left, max_len = 0, 0, 0

        for right, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(char)
            max_len = max(max_len, right - left + 1)
        return max_len


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
