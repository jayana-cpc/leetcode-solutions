class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        [1, 4]
        [3, 3]

        [(4, 2) (1, 2) (0, 1) (7, 1)]
        [(0, 1) (1, 2) (4, 2) (7, 1)]
        [10, 4.5, 3, 3]

        """
        paired = []
        for i in range(len(position)):
            paired.append((position[i], speed[i]))
        paired.sort(reverse=True)
        stack = []
        for p, s in paired:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        
