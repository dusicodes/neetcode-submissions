class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = False
        nums.sort()
        x = 0
        while dup == False and x < len(nums) - 1:
            if nums[x] == nums[x+1]:
                dup = True
                return True
            else:
                x += 1
        return False
