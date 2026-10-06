class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       if not nums:
           return 0
       h = set(nums) 
       res = sorted(list(h))
       ls, count = 1, 1

       print(res) 
       
       for i, v in enumerate(res):
        if v + 1 in h:
            count += 1 
            print(count)
            if count > ls:
                ls = count
        else:
            count = 1

            

       return ls



        


