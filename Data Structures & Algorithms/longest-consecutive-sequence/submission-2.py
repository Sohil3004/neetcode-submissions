class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        if not nums:
            return 0
        if len(nums)==1:
            return 1

        sorted_num = sorted(nums)
        n = len(nums)

        consecutive = 1
        longest = 1
   
        for i in range(n-1):
            if sorted_num[i+1] == sorted_num[i]:
                continue
            elif sorted_num[i+1] == 1 + sorted_num[i]:
                consecutive +=1
            else:
                longest = max(longest,consecutive)
                consecutive = 1
        return max(longest,consecutive)
