def func(_n_x): # should work
    return 'something'

def _n_func1(v):
    return 10 # should work

def _n_func2(_n_v):
    return _n_v # should work

def _n_func3():
    x = 'something'
    return x # should not work

def _n_func4():
    x = 'something'
    # should not work because it has no return

def _n_func5():
    return func(10) # should not work because func can be null

_n_x = 0
y = 'something'

func(y) # should cause an error
_n_x = _n_func1(y) # should work
_n_y = _n_func2(10) # should work
_n_func2(y) # should cause an error


_n_x = func(_n_x) # error

# a function taking two parameters
def f1(_n_a, b):
    print(_n_a)
    
f1(1, 2)
f1(None, 3)

_n_protected = None
_n_protected2 = y

def _n_f2():
    print("here")
    
v1 = _n_f2()
print("v1:", v1)

def _n_f3():
    return None

return "test"
