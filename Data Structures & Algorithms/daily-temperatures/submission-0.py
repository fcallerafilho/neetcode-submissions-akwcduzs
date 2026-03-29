class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i in range(len(temperatures)):
            temp = temperatures[i]
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temp:
                    result.append(j-i)
                    break
                elif j == len(temperatures) - 1:
                    result.append(0)

        result.append(0)
        return result
            
