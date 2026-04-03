class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        # res = [1, 4, 1 , 2, 1, 0, 0]
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temp, i))
        return res

