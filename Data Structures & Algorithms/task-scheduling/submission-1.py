class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # tasks = ["X","X","X","Y","Y"]
        # Are the tasks arranged in a certain way? (ex: alphabetical or in order of highest occurence): No
        # There will be a singular correct answer?
        # Max # of tasks = 1000
        """
        Algorithm Design
        Q: How to complete most frquent task first (prioritize most common task)?
        A: a) Use Counter(tasks) to determine freq. {"X": 3, "Y": 2}
           b) Add tasks onto a max heap: [3, 2]
        
        Q: How do I cooldown task or how do I know when the CPU has cooled down?
        A: a) Use a queue to hold tasks while they are cooling down
        A: b) Keep track of the time they'll be ready: [(count, cycle)]

        1. Count Frequencies
        2. Create max heap with frequencies
        3. While there are tasks in the heap or on the queue:
            a. increase cycle
            b. if heap: pop from the heap, process it (reduce its count) then add it on the queue
                        if the count > 0.
            c: if the front of the queue is ready (cycle = cylce): push that task onto the heap
        """
        freq = Counter(tasks)
        heap = [-val for val in freq.values()]
        heapq.heapify(heap)
        q = []
        cycle = 0

        while heap or q:
            cycle += 1

            if heap:
                task = -heapq.heappop(heap)
                task -= 1
                if task > 0:
                    q.append((task, cycle+n))
            
            if q:
                task = q[0]
                if cycle == q[0][1]:
                    heapq.heappush(heap, -q.pop(0)[0])
        return cycle








