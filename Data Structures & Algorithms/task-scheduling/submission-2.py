class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        heap = [(-freqs[key], key) for key in freqs]
        heapq.heapify(heap)

        q = deque()  # stores (freq, task, available_at)
        time = 0

        while heap or q:
            time += 1

            if heap:
                freq, task = heapq.heappop(heap)
                if freq + 1 != 0:             # still has uses remaining
                    q.append((freq + 1, task, time + n))  # ← cool down first

            if q and q[0][2] == time:         # ← check front, not back
                freq, task, _ = q.popleft()
                heapq.heappush(heap, (freq, task))

        return time