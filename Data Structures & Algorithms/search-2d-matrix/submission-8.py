class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            low, high= 0, len(arr) - 1
            while low <= high:
                mid = low + (high - low) // 2
                print(arr[mid])
                if arr[mid] == target:
                    return True

                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1


        return False 

            
        