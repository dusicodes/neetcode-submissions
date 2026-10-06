class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for i in range(0, len(numbers)):
           find = target - numbers[i] 
           if find in numbers:
                result.append(i + 1)
                result.append(numbers.index(find) + 1)
                return result
        
        return result
           

        
