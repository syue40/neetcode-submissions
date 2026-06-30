class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # ()[]{}

        if not s or len(s) == 1:
            return False

        map_parentheses = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        valid_chars = list(map_parentheses.keys()) + list(map_parentheses.values())
        for ch in s:
            if ch not in valid_chars:
                return False

            if ch in map_parentheses.values():
                stack.append(ch)
            else:
                matching_bracket = map_parentheses.get(ch)
                if not stack:
                    return False
                corresponding_val = stack.pop()
                if corresponding_val != matching_bracket:
                    return False

        if not stack:
            return True
        else:
            return False
                