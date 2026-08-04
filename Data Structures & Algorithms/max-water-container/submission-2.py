class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxi = 0
        l, r = 0, n-1
        while l< r:
            curr_max = min(heights[l],heights[r]) * (r-l)
            if heights[l] <= heights[r]:
                l +=1
            elif heights[l]>= heights[r]:
                r -=1
            maxi = max(maxi,curr_max)
        return maxi