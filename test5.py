from file3 import null_weave # change to import your function

def func1(_n_x, _n_y, z):
  # when part3 main function is run
  # this function should be modified to have the following checks
  # if _n_x is None:
  #    raise Exception('_n_x is given None in func1')
  # if _n_y is None:
  #    raise Exception('_n_y is given None in func1')
  #
  # notice that z has no check because it is not protected!

  print(z)
  return None # this should be OK!

def _n_func2(x):
  return x

# if this file is run you should see this behavior:
null_weave() # should use aspect lib to weave your aspect to all function calls
func1(10, 20, 30) # should show 30 to the screen
print(_n_func2(10)) # should print 10
print(_n_func2(None)) # should show an error because of the None check in the aspect! 
