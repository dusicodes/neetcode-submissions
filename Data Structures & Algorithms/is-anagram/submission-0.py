class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hg = {}
        hg2 = {}
        for letter in s:
            if letter in hg:
                hg[letter] += 1
            else:
                hg[letter] = 1
            
        for letter in t:
            if letter in hg2:
                hg2[letter] += 1
            else:
                hg2[letter] = 1
            
        if hg == hg2:
            return True
        return False
        
        print(hg)