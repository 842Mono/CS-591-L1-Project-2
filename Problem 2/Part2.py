from aspectlib import Aspect, Proceed, Return, weave
import sys, ast, astor
import inspect

memo = {}

@Aspect(bind=True)
def memoize_aspect(f, *args, **kwargs):
    key = f.__name__ + "|" + ",".join(str(args)) + "|" + ",".join(str(kwargs))
    if(not key in memo):
        memo[key] = yield Proceed(*args, **kwargs)
        yield Return(memo[key])
    yield Return(memo[key])

def weave_memoize(source, Globals):

    tree = ast.parse(source)

    for statement in tree.body:
        if isinstance(statement, ast.FunctionDef) and not (statement.name == "memoize_aspect" or statement.name == "weave_memoize"):
            # print(inspect.getsource(Globals[statement.name]))
            weave(Globals[statement.name], memoize_aspect)
            # print(inspect.getsource(Globals[statement.name]))