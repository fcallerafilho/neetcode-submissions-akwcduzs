class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}

        for task in tasks:
            freqs[task] = 1 + freqs.get(task, 0)

        arr = [val for val in freqs.values()]
        
        heapq.heapify_max(arr)

        q = collections.deque()
        time = 0
        cycle = 0

        while q or arr:
            time += 1
            if arr:
                popped = heapq.heappop_max(arr)
                popped -= 1
                if popped > 0:
                    q.append([popped, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush_max(arr, q.popleft()[0])

        return time

