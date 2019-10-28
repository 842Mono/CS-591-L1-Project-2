import inspect
import sys
import ast
import astor


FunctionsToParameters = {}

class PopulateFunctionsToParameters(ast.NodeVisitor):
    
    def visit_FunctionDef(self, node):
        
        FunctionsToParameters[node.name] = {}
        for i, arg in enumerate(node.args.args):
            FunctionsToParameters[node.name][i] = (arg.arg)

# class VisitCalls(ast.NodeVisitor):

#     def visit_Call(self, node):
#         pass


def WeaveOneFunction(function):

    def NewFunction(*args, **kwargs):

        limit =  len(args) if len(args) < len(function.__code__.co_varnames) else len(function.__code__.co_varnames)
        i = 0
        while(i < limit):
            if args[i] is None:
                raise Exception(function.__code__.co_varnames[i] + ' is given None in ' + function.__name__ + ".")
            i += 1
        function(*args, **kwargs)
    
    return NewFunction

# class Visitor(ast.NodeVisitor):

#     def visit_FunctionDef(self, node):
#         pass
        # for e in dir(node):
        #     print(e)
        # for line in node.body:


def null_weave():

    tree = ast.parse(inspect.getsource(sys.modules['__main__']))

    populator = PopulateFunctionsToParameters()
    populator.visit(tree)

    # callvisitor = VisitCalls()
    # callvisitor.visit(tree)

    
    # find function definitions and instrument the body of each function
    statements = []
    for statement in tree.body:
        if isinstance(statement, ast.FunctionDef):
            statement = instrument_body(statement)
        statements.append(statement)
    tree.body = statements
    code = astor.to_source(tree)
    print('output code --------------------------')
    print(code)
    print('---------------------------------------')
    return code

    # tree = ast.parse(inspect.getsource(sys.modules['__main__']))
    # visitor = Visitor()
    # print(visitor.visit(tree))
    # print("tt")

    # print(inspect.getsource(sys.modules['__main__']))

def instrument_body(function_def):
    
    statements = []
    for e in function_def.args.args:
        if(e.arg.startswith('_n_')):
            statements.append(ast.parse("if(" + e.arg + " is None):\n   raise Exception('" + e.arg + " is given None in " + function_def.name + "')"))
            
    # for e in statements:
    #     print(e)

    # for e in function_def.body:
    #     print(e.value)

    function_def.body = statements + function_def.body
    return function_def

    # for statement in function_def.body:
    #     if isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
    #         pass
    #         # statements += instrument_statement(statement, statement.value)
    #     else:
    #         # does not require an instrumentation because it is not a function call
    #         statements.append(statement)

    # function_def.body = statements
    # return function_def




# @null_weave
# def test1(a, b, c, d):
#     print(a + b + 1)

# test1(1, 2, 3, 4)
# # test1(None, 2, 5, 6)
