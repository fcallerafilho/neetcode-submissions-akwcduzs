class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def happy(number):
            if number == 1:
                return True
            if number in seen:
                return False

            seen.add(number)
            res = 0
            to_str = str(number)
            for i in range(len(to_str)):
                res += int(to_str[i])**2

            return happy(res)

        return happy(n)
