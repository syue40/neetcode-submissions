class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3 numbers must add up to 0

        # [-1, 0, 1, 2, -1, -4]

        # final output should be an array of arrays
        final_output = []

        unique_sorted = set()


        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                curr = nums[i] + nums[j]
                for k in range(j+1, len(nums)):
                    if curr + nums[k] == 0:
                        curr_arr = [nums[i], nums[j], nums[k]]
                        sorted_ = str(sorted(curr_arr))
                        if sorted_ not in unique_sorted:
                            unique_sorted.add(sorted_)
                            final_output.append(curr_arr)

        
        return final_output