class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0

        while l < r:
            res = min(heights[l], heights[r]) * (r - l)
            area = max(res, area)
            if heights[l] > heights[r]:
                r = r - 1
            else:
                l = l + 1
        return area