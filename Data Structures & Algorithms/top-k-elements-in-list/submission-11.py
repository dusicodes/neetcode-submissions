class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        result = []
        for n in nums:
            counter[n] = counter.get(n,0)+ 1
        
        top = max(counter.values())
        while k > 0:

            for key in counter:
                if counter[key] == top:
                    result.append(key)
                    k -= 1
            top -= 1
        return result



                
            
       

        
        