class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1

        while l<r:
            addition=numbers[l] + numbers[r] 
            if addition > target:
                r-=1
            if addition < target:
                l+=1
            if addition == target:
                return[l+1,r+1]