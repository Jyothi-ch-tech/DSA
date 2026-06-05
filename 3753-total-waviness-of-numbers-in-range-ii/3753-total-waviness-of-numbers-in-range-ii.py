from functools import cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def f(x):
            s = str(x)

            @cache
            def dp(i, tight, started, a, b):
                if i == len(s):
                    return (1, 0)

                limit = int(s[i]) if tight else 9
                cnt = wav = 0

                for d in range(limit + 1):
                    nt = tight and d == limit

                    if not started and d == 0:
                        c, w = dp(i + 1, nt, False, -1, -1)
                    elif not started:
                        c, w = dp(i + 1, nt, True, -1, d)
                    else:
                        add = 0
                        if a != -1:
                            if (b > a and b > d) or (b < a and b < d):
                                add = 1
                        c, w = dp(i + 1, nt, True, b, d)
                        w += add * c

                    cnt += c
                    wav += w

                return cnt, wav

            return dp(0, True, False, -1, -1)[1]

        return f(num2) - f(num1 - 1)