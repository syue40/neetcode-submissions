class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            if i == len(nums):
                ahead = []
            else:
                ahead = nums[i + 1:]
            behind = nums[:i]

            ahead_tot = 1
            for num in ahead:
                ahead_tot *= num

            behind_tot = 1
            for num in behind:
                behind_tot *= num

            output.append(behind_tot*ahead_tot)

        return output
