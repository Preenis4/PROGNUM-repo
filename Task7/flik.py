class Fibonacci:
    # for calcing fibbo sequence
    def number(self, N : int) -> int:
        a, b = 0, 1
        for i in range(N-1):
            a, b = b, a+b
        return a
    def foobar(self, N: int, M: int):
        a, b = 0, 1
        count = 0
        res = []
        while count < N:
            a, b = b, a+b
            if a % M == 0:
                res.append(a)
            count += 1
        return res

fib = Fibonacci()
print(fib.number(100))
print(fib.foobar(100, 7))
