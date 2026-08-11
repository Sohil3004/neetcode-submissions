class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,x in enumerate(nums):
            comple = target - x
            if comple in seen:
                return [seen[comple],i]
            seen[x] = i
