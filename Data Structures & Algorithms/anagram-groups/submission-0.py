class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_map = defaultdict(list)
        
        for element in strs:
            sorted_elem = "".join(sorted(element))
            final_map[sorted_elem].append(element)

        return list(final_map.values())