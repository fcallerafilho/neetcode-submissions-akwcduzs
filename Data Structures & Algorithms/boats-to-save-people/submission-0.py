class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        i = 0
        j = len(people) - 1

        while i <= j:
            if i == j:
                boats += 1
                break
            if people[j] >= limit:
                boats += 1
                j -= 1
            else:
                if people[j] + people[i] > limit:
                    boats += 1
                    j -= 1
                else:
                    boats += 1
                    i += 1
                    j -= 1

        return boats


        