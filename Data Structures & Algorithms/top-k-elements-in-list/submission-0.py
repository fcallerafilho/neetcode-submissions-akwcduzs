from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}

        for i in range(len(nums)):
            if nums[i] not in myMap:
                myMap[nums[i]] = 1
            else:
                myMap[nums[i]] += 1
        
        counter = Counter(myMap)
        result = dict(counter.most_common(k))

        return(list(result.keys()))