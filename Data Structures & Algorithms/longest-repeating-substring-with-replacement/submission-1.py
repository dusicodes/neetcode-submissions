class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, m = 0,0
        longest = 0

        freq = {}
        for j in range(len(s)):

            if s[j] in freq:
                freq[s[j]] += 1
            else:
                freq[s[j]] = 1

            m = max(m, freq[s[j]]) 
            while (j - i + 1) - m > k:
                freq[s[i]] -= 1
                i += 1
            window_size = j - i  + 1
            longest = max(longest, window_size)
        return longest

