class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for i in asteroids:
            while stack and i < 0 and stack[-1] > 0:
                if stack[-1] + i == 0:
                    i = 0
                    stack.pop()
                elif stack[-1] + i > 0:
                    i = 0
                elif stack[-1] + i < 0:
                    stack.pop()
            if i:
                stack.append(i)
            
        return stack


