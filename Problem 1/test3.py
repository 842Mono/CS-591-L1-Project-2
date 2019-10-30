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


_n_x = func(_n_x) # Error: Assigning the result of an unprotected function to a protected variable

_n_func2(None) # Error: Passing 'None' to a protected argument

_n_protected = None # Error: Assigning 'None' to a protected variable
_n_protected2 = y # Error: Assigning an unprotected variable to a protected variable

def _n_f3():
    return None # Error: Protected function returning 'None'
