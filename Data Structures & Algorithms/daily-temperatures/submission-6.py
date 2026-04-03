class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temps = [30,38,30,36,35,40,28]
        res = [0]*len(temperatures)
        stack = [(30, 0)]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                x = stack.pop()
                res[x[1]] = i - x[1]
            stack.append((temp, i))
        return res
            
