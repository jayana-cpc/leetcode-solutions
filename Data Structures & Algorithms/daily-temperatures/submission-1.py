class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if sorted(temperatures, reverse=True) == temperatures:
            return [0] * len(temperatures)

        stack = []
        stack.append(temperatures[0])
        res = [0] * len(temperatures)
        i = 0
        save = 0
        while save < len(temperatures):
            if temperatures[i] > stack[-1]:
                res[save] = i - save
                i = save + 1
                stack.pop()
                stack.append(temperatures[save + 1])
                save += 1
            elif temperatures[i] <= stack[-1]:
                if i + 1 < len(temperatures):
                    i+=1
                else:
                    res[save] = 0
                    i = save + 1
                    stack.pop()
                    if save + 1 < len(temperatures):
                        stack.append(temperatures[save + 1])
                    else:
                        return res
                    save += 1
            else:
                save = i
                stack.append(temperatures[i])

    