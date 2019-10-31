import sys
import ast
import astor
import inspect

FunctionsToParameters = {}

class PopulateFunctionsToParameters(ast.NodeVisitor):
    
    def visit_FunctionDef(self, node):
        
        FunctionsToParameters[node.name] = {}
        for i, arg in enumerate(node.args.args):
            FunctionsToParameters[node.name][i] = (arg.arg)


def WeaveOneFunction(function):

    def NewFunction(*args, **kwargs):

        limit = len(args) if len(args) < len(function.__code__.co_varnames) else len(function.__code__.co_varnames)
        i = 0
        while(i < limit):
            if args[i] is None:
                raise Exception(function.__code__.co_varnames[i] + ' is given None in ' + function.__name__ + ".")
            i += 1
        function(*args, **kwargs)
    
    return NewFunction


def null_weave(code):

    tree = ast.parse(code)

    populator = PopulateFunctionsToParameters()
    populator.visit(tree)

    statements = []
    for statement in tree.body:
        if isinstance(statement, ast.FunctionDef):
            statement = instrument_FunctionDef(statement)
        statements.append(statement)
    tree.body = statements
    code = astor.to_source(tree)
    print('# output code --------------------------')
    print(code)
    print('# --------------------------------------')
    return code


def instrument_FunctionDef(function_def):
    
    statements = []
    for e in function_def.args.args:
        if(e.arg.startswith('_n_')):
            statements.append(ast.parse("if(" + e.arg + " is None):\n   raise Exception('" + e.arg + " is given None in " + function_def.name + "')"))

    function_def.body = statements + function_def.body

    if(function_def.name.startswith('_n_')):
        i = 0
        while(i < len(function_def.body)):
            if(isinstance(function_def.body[i], ast.Return)):
                print(function_def.body[i].value)
                if(hasattr(function_def.body[i].value, 'id')):
                    function_def.body.insert(i, ast.parse("if(" + function_def.body[i].value.id + " is None):\n   raise Exception('" + function_def.body[i].value.id + " is given None in " + function_def.name + "')"))
                    i += 1
                elif(hasattr(function_def.body[i].value, 'value')):
                    function_def.body.insert(i, ast.parse("if(" + function_def.body[i].value.value + " is None):\n   raise Exception('" + function_def.body[i].value.value + " is given None in " + function_def.name + "')"))
                    i += 1
            i += 1


    return function_def


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as code_file:
        code = code_file.read()
        null_weave(code)