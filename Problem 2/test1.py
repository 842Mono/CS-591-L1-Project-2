from Part1 import memoize

def fib(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1

  return memoize(fib, n-1) + memoize(fib, n-2)

print(memoize(fib, 10))