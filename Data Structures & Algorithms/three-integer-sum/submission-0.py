class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, j, k= 0, 0, len(nums) - 1
        nums.sort()
        res = []

        for i in range(len(nums)):
            j = i + 1 
            k = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue


            while j < k: 
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    r = [nums[i], nums[j], nums[k]]
                    res.append(r)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                    
                else:
                    if total < 0:
                        j += 1
                    else:
                        k -= 1


        return res
        