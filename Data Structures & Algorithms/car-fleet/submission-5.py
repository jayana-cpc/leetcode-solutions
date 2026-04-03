class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        target=10
        position=[4,1,0,7]
        speed=[2,2,1,1]
        [(7, 3), (4, 0), (1, 1), (0, 2)]
        time = [3, 3, 4.5, 10]

        """
        for index, pos in enumerate(position):
            position[index] = (pos, index)
        position.sort(reverse=True)
        fleets = len(position)
        time = [None] * fleets
        for index, tup in enumerate(position):
            pos, realIndex = tup
            time[index] = (target - pos) / speed[realIndex]
        print(position)
        print(time)

        for index, sec in enumerate(time[1:], 1):
            print(sec, time[index-1], index)
            if sec <= time[index-1]:
                time[index] = time[index-1]
                fleets -= 1

        
        return fleets
        