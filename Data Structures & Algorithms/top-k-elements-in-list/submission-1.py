class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        count_map = defaultdict(int)
        output = []

        for i in nums:
            count_map[i] += 1
        sorted_dict = [i for (i, v) in sorted(count_map.items(), key=lambda item: item[1])]
        return sorted_dict[-k:]