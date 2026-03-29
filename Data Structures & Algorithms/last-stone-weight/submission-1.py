class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            heaviest = heapq.heappop_max(stones)
            snd_heaviest = heapq.heappop_max(stones)
            print(heaviest, snd_heaviest)

            if heaviest == snd_heaviest:
                continue
            else:
                heapq.heappush_max(stones, heaviest - snd_heaviest)
            

        return stones[0] if stones else 0
