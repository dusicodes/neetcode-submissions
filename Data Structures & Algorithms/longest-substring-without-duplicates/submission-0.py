class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j  = 0 , 0 
        ls = set()
        max_val = 0
        if len(s) == 1:
            return 1
        while i < len(s) and j < len(s):
            if s[j] not in ls: 
                ls.add(s[j])
                j += 1  
                max_val = max(max_val, (j - i))
                print(ls)
            else:

                if s[i] in ls:
                    ls.remove(s[i])
                    i += 1

        return max_val 