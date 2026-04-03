class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if sorted(temperatures, reverse=True) == temperatures:
            return [0] * len(temperatures)

        stack = [(0, temperatures[0])]
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            j = len(stack) - 1
            while j > -1:
                if temperatures[i] > stack[j][1]:
                    res[stack[j][0]] = i - stack[j][0]
                    stack.pop(j)
                j -= 1
            stack.append((i, temperatures[i]))
        return res


    