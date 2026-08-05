class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l = 0
        res = 0

        if len(set(s)) == 1:
            return len(s)

        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r],0) +1 
            freq = max(mp.values())
            while(r-l+1) - freq > k:
                mp[s[l]] -=1
                l +=1
            res = max(res, r-l+1)
            
        return res
