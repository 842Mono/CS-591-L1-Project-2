memo = {}

def memoize(f, *args, **kwargs):
    
    # check if f(*args, **kwargs) is already computed and stored
    # if it is, return the output directly,
    # otherwise, call f(*args, **kwargs) and save its result, and return it.
    key = f.__name__ + "|" + str(args) + "|" + str(kwargs)
    if(not key in memo):
        memo[key] = f(*args, **kwargs)
    return memo[key]

print(memoize(sum, [10, 30]))
print(memoize(sum, [10, 30]))
print(memo)