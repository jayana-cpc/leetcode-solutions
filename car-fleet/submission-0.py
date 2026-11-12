class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for index, pos in enumerate(position):
            position[index] = (pos, index)
        position.sort(reverse=True)
        fleets = len(position)
        time = [None] * fleets
        for index, tup in enumerate(position):
            pos, realIndex = tup
            time[index] = (target - pos) / speed[realIndex]
       

        for index, sec in enumerate(time[1:], 1):
            if sec <= time[index-1]:
                time[index] = time[index-1]
                fleets -= 1

        
        return fleets