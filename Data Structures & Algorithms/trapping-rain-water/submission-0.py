class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        water = 0
        lMax = height[l]
        rMax = height[r]
        if not height:
            return 0
        while l<r:
            if lMax <=rMax:
                l+=1
                lMax =  max(height[l], lMax)  
                water += lMax - height[l]
            else:
                r -= 1
                rMax = max(height[r],rMax)
                water += rMax - height[r]
        return water
