class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        j = len(numbers) - 1

       

        for i in range(0, len(numbers)):
           find = target - numbers[i] 
           if find in numbers:
                result.append(i + 1)
                result.append(numbers.index(find) + 1)
                break
        
        return result
           

        
