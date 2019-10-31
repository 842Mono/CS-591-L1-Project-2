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

    # all_functions = inspect.getmembers(inspect.getmodulename("__module__"), inspect.isfunction)
    # print(all_functions)
    # for e in all_functions:
    #     print(e)

    # for e in dir(__name__):
    #     print(e)

#     filename = sys.argv[1]
#     with open(filename, 'r') as code_file:
#         code = code_file.read()
#         print(code)
#         code = weave(code, memoize_aspect)
#         code()



    tree = ast.parse(source)

    # statements = []
    for statement in tree.body:
        if isinstance(statement, ast.FunctionDef) and not (statement.name == "memoize_aspect" or statement.name == "weave_memoize"):
            print("ddd")
            print(statement.name)
            print(inspect.getsource(Globals[statement.name]))
            weave(Globals[statement.name], memoize_aspect)
            print(inspect.getsource(Globals[statement.name]))
            print("dbg")
            # print(statement)
            # for e in dir(statement):
            #     print(e)
            # weave(statement, memoize_aspect)
            # print(statement)
        # statements.append(statement)
    # tree.body = statements
    # print(tree.body)
    # code = astor.to_source(tree)
    
    # print('# output code --------------------------')
    # print(code)
    # print('# --------------------------------------')

    # exec(code)
    print(memo)