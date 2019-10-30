# from file3 import null_weave


def func1(_n_x, _n_y, z):
    if _n_x is None:
        raise Exception('_n_x is given None in func1')
    if _n_y is None:
        raise Exception('_n_y is given None in func1')
    print(z)
    return None


def _n_func2(x):
    return x


# null_weave()
func1(10, 20, 30)
print(_n_func2(10))
print(_n_func2(None))
