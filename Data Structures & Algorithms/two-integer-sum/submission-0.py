class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i in range(0, len(nums)):
            dif = target - nums[i]

            for j in range(i + 1 , len(nums)):
                if dif == nums[j]:
                    result.append(i)
                    result.append(j)
                    return result;

        return []