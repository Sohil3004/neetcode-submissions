
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1,len2 = len(s1),len(s2)
        if len1>len2:
            return False
        count_s1 = Counter(s1)
        for i in range(len2-len1+1):
            curr_win = s2[i:i+len1]
            if Counter(curr_win)==count_s1:
                return True
        return False

