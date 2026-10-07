class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        pairs.sort(reverse=True)

        stack = []
        for pos, t in pairs:
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)



