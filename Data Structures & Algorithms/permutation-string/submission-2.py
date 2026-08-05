class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1,len2 = len(s1), len(s2)
        if len1>len2:return False
        count_s1 = Counter(s1)
        win_count = Counter(s2[:len1])

        if count_s1 == win_count:
            return True
        for r in range(len1,len2):
            win_count[s2[r]] += 1
            l_char = s2[r-len1]
            win_count[l_char] -= 1
            # if win_count == 0:
            #     del win_count
            if win_count == count_s1:
                return True
        return False
