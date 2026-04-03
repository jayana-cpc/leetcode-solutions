class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        max_heap = [-val for val in task_count.values()]
        heapq.heapify(max_heap)
        q = []
        time = 0

        while max_heap or q:
            time += 1
            if max_heap:
                task = heapq.heappop(max_heap)
                if task + 1 < 0:
                    q.append((task+1, time+n))

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.pop(0)[0])
        return time


