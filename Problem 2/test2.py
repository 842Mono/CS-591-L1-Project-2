from Part2 import weave_memoize #, memo
import inspect, sys

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1

    return fib(n-1) + fib(n-2)

weave_memoize()

# print(fib(5))
# print(memo)



# def my_range(x):
#     x = yield 'kinan'
#     print('hello', x)
#     yield 'mina'

# gen = my_range(10)
# print(gen)
# print(next(gen)) #kinan
# print(gen.send('bla'))