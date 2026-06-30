import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1, 3, 9, 13, 14]
        # need to find the minimum number of bph needed to finish bananas in h hours

        piles = sorted(piles)

        left, right = 1, max(piles)

        result = right
        while left <= right:
            middle = (left + right) // 2

            total_hours = 0
            for bananas in piles:
                hours_taken = math.ceil(bananas / middle) 
                total_hours += hours_taken

            if total_hours <= h:
                result = middle
                right = middle - 1
            else:
                left = middle + 1

        return result
        
