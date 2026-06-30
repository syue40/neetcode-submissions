class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            placeholder = target - nums[i]
            for j in range(len(nums)):
                if j != i and nums[j] == placeholder:
                    return sorted([i, j])
