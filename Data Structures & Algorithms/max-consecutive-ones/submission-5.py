class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                j = i

                while j < len(nums) and nums[j] == 1:
                    j += 1

                m = max(m, j - i)

        return m