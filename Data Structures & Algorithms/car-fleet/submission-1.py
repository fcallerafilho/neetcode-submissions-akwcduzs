class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], speed[i], time))

        cars.sort(reverse=True)

        stack = []
        for i in range(len(cars)):
            stack.append(cars[i][2])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

            
            
        





