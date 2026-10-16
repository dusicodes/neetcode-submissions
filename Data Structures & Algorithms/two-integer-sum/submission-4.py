class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h = {} 

        for i, n in enumerate(nums):
            
            check = target - n

            if check in h:
                return [h[check], i]
            
            if n not in h:
                h[n] = i