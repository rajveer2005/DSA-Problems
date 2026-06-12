class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        num = abs(x)
        rev = 0

        while num > 0:
            LD = num % 10
            rev = rev * 10 + LD
            num = num // 10

        rev *= sign

        if -2**31 <= rev <= 2**31 - 1:
            return rev
        return 0