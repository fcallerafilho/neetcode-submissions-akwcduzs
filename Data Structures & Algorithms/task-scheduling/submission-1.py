class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}

        for task in tasks:
            freqs[task] = 1 + freqs.get(task, 0)

        arr = [[val, key] for key, val in freqs.items()]
        
        heapq.heapify_max(arr)

        q = collections.deque()
        time = 0
        cycle = 0

        while q or arr:
            if arr and time < n+1:
                popped = heapq.heappop_max(arr)
                popped[0] -= 1
                time += 1
                cycle += 1
                if popped[0] > 0:
                    q.append(popped)
            elif not arr and time < n+1:
                cycle += 1
                time += 1
            elif time == n+1:
                while q:
                    fromQ = q.popleft()
                    heapq.heappush_max(arr,fromQ)
                time = 0

        return cycle

