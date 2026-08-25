class Solution:
    def isValid(self, s: str) -> bool:
        paran = []
        lookup ={")":"(","}":"{","]":"["}
        for char in s:
            if char in lookup:
                if paran and paran[-1] == lookup[char]:
                    paran.pop()
                else:
                    return False
            else:
                paran.append(char)

        return True if not paran else False