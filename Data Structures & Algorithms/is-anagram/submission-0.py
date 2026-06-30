class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force, sort both
        s_sort = sorted(s)
        t_sort = sorted(t)
        return s_sort == t_sort
        