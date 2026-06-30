class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                dist = j - i
                height_ = min(heights[i], heights[j])
                maxi = dist * height_
                if maxi > maximum:
                    maximum = maxi
        return maximum