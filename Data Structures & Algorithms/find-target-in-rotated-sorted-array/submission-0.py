class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i,v in enumerate(nums):
            if nums[i]==target:
                return i
            
        return -1