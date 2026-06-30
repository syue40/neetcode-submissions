class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = list(set(sorted(nums)))

        if not nums:
            return 0

        if len(nums)==1:
            return 1

        sorted_nums = sorted(list(set(nums)))
        max_cons = 1
        count = 1
        print(sorted_nums)
        for i in range(1, len(sorted_nums)):
            before = sorted_nums[i-1]
            curr = sorted_nums[i]

            reset = False

            if abs(curr - before) == 1:
                count += 1
            else:
                reset = True
            print(count)
            max_cons = max(max_cons, count)
            if reset:
                count = 1
            
    
        return max_cons