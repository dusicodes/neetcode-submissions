class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}

       # h = {j: 2, a: 2, m: 1, r: 1}
       # s = jam
       # t = jar


        if len(s) != len(t):
            return False
        

        q1 = ''.join(sorted(s))
        q2 = ''.join(sorted(t))


        if q1 == q2:
            return True
        else:
            return False



            



