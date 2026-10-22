class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)):
            j = i + 1
            while abs(i-j) <= k and j < len(nums):
                if nums[i] == nums[j]:
                    print(nums[i], nums[j])
                    print(abs(i-j))
                    return True
                
                j+= 1
            
        return False

    