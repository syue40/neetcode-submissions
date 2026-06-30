class Solution:
    def binary_search_idx(self, inp, target):
        if len(inp) == 1 and inp[0][1] != target:
            return -1

        middle = len(inp) // 2
        idx, middle_num = inp[middle]
        if middle_num == target:
            return idx
        
        elif middle_num > target:
            result = self.binary_search_idx(inp[0: middle], target)

        else:
            result = self.binary_search_idx(inp[middle: len(inp)], target)
        return result


    def search(self, nums: List[int], target: int) -> int:
        enumerated_input = tuple(enumerate(nums))
        found = self.binary_search_idx(enumerated_input, target)
        return found