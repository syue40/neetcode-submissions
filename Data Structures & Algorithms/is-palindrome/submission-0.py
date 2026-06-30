class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) -1

        while left < right:
            curr_left = s[left].lower()
            curr_right = s[right].lower()

            if not curr_left.isalnum():
                left += 1
                continue
            if not curr_right.isalnum():
                right -= 1
                continue

            if curr_left != curr_right:
                return False
            else:
                left += 1
                right -= 1

        return True

            