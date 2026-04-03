class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        comps = {}

        for i in range(0, len(numbers)):
            if target - numbers[i] in comps.keys():
                return[comps[target - numbers[i]] + 1, i + 1]

            else:
                comps[numbers[i]] = i



        


        