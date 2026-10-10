class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_1 = {}
        s_2 = {}
        k = len(s1)
        i, j = 0 ,0

        for n in s1:
            if n not in s_1:
                s_1[n] = 1
            else:
                s_1[n] += 1

        print(s_1)
        for j in range(len(s2)):
            if s2[j] not in s_2:
                s_2[s2[j]] = 1
            else:
                s_2[s2[j]] += 1

            if (j - i + 1) == k:
                if s_1 == s_2:
                    return True
                else:
                    s_2[s2[i]] -= 1
                    if s_2[s2[i]] == 0:
                        del s_2[s2[i]]
                i += 1

        return False
        
