class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        input = s
        char_set = set()
        left = 0
        res = 0

        for right in range(len(input)):
            while input[right] in char_set:
                char_set.discard(input[left])
                left += 1
            
            char_set.add(input[right])
            res = max(res, right - left + 1)

        return res