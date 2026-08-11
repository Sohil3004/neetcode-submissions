class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            sorted_s = sorted(s)
            key = "".join(sorted_s)
            if key in seen:
                seen[key].append(s)
            else:
                seen[key] = [s]
        return list(seen.values())
            
               
            
        

