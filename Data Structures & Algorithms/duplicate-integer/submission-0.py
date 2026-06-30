class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # approach 1: quick but less efficient
        # return len(set(nums)) == len(nums)
        # it's O(n) since we need to build a set from a list of n elements

        # approach 2: iterate until duplicate is found
        container = set()
        for i in nums:
            if i in container:
                return True
            container.add(i)
        return False