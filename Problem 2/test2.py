from Part2 import weave_memoize, memo
import inspect, sys
# inspect.getsource(sys.modules[__name__])

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1

    return fib(n-1) + fib(n-2)

# print(globals()["fib"])
weave_memoize(inspect.getsource(sys.modules[__name__]), globals())
# print(dir("__main__"))

print(fib(5))
print(memo)