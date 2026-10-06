class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        h = {}
        i = 0

        # h = {'name': 1}
        # h[name] = 1

        for i in range(len(nums)): # for i in 4 
            if nums[i] not in h:
                h[nums[i]] = i
            else:
                return True
        return False



            



