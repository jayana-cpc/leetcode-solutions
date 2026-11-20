class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = [] # (index, temp)
        res = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                index, _ = stack.pop()
                res[index] = i - index
            stack.append((i, temp))
        return res


