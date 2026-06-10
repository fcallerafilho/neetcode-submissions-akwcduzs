'''
[(2, X), (2, Y)]

- process task w largest number remaining: [(1, X), (2, Y)]
- pop it from back and reinsert: [(2, Y), (1, X)]
- do until there are no remaining tasks / if there is only one type of task, idle n times
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        tasks_f = []
        time = 0

        for i in range(len(tasks)):
            freqs[tasks[i]] = freqs.get(tasks[i], 0) + 1

        for task, freq in freqs.items():
            tasks_f.append(freq)
        
        heapq.heapify_max(tasks_f)
        queue = collections.deque()

        while tasks_f or queue:
            time += 1

            if tasks_f:
                rem = heapq.heappop_max(tasks_f)
                rem -= 1
                if rem > 0:
                    queue.append((rem, time + n))

            if queue and queue[0][1] == time:
                rem, t = queue.popleft()
                heapq.heappush_max(tasks_f, rem)
            
        return time