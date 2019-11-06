from aspectlib import Aspect, Proceed, Return, weave
import sys, ast, astor
import inspect

memo = {}

@Aspect(bind=True)
def memoize_aspect(f, *args, **kwargs):
    key = f.__name__ + "|" + str(args) + "|" + str(kwargs)
    # print('LOOK AT ME', inspect.getsource(f))
    if(not key in memo):
        memo[key] = yield Proceed(*args, **kwargs)
        yield Return(memo[key])
    else:
        yield Return(memo[key])

def weave_memoize():
    source = inspect.getsource(sys.modules['__main__'])
    # print(source)
    tree = ast.parse(source)

    for statement in tree.body:
        # print(statement)
        # for e in dir(statement):
        #     print(e)
        if isinstance(statement, ast.FunctionDef):
            weave('__main__.' + statement.name, memoize_aspect)
            # print(statement)
            # for e in dir(statement):
            #     print(e)
    

    # print("new src")
    # print(astor.to_source(tree))