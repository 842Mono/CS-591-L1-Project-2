from file2 import null_cast # Change this to import your function

y = 'something'
_n_x = y # should not work
_n_x = null_cast(y) # should work 


def test(_n_p1):
    return _n_p1

test(null_cast(y))
test(test(y))

null_cast(None)