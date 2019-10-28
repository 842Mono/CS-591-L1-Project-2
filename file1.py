import ast, sys

FunctionsToParameters = {}

class PopulateFunctionsToParameters(ast.NodeVisitor):
    
    def visit_FunctionDef(self, node):
        
        FunctionsToParameters[node.name] = {}
        for i, arg in enumerate(node.args.args):
            FunctionsToParameters[node.name][i] = (arg.arg)

class Problem1Visitor(ast.NodeVisitor):
    
    #def visit_BinaryOp(self, node):
        #print(node)
        
    def visit_Assign(self, node):
        if(node.targets[0].id.startswith('_n_')):
            
            if(hasattr(node.value, 'value') and node.value.value == None):
                print("Error: Assigning 'None' to a protected variable at " + str(node.value.lineno) + ".")
                
            if(hasattr(node.value, 'id') and not node.value.id.startswith('_n_')):
                print("Error: Assigning an unprotected variable to a protected variable at " + str(node.value.lineno) + ".")
                
            if(hasattr(node.value, 'func') and not (node.value.func.id.startswith('_n_') or node.value.func.id == 'null_cast')):
                print("Error: Assigning the result of an unprotected function to a protected variable at " + str(node.value.func.lineno) + ".")
            
    def visit_Call(self, node):
        for i, arg in enumerate(node.args):
            if(node.func.id in FunctionsToParameters and FunctionsToParameters[node.func.id][i].startswith('_n_')):

                if(hasattr(arg, 'value') and arg.value == None) :
                    print("Error: Passing 'None' to a protected argument at " + str(arg.lineno) + ".")
                elif(hasattr(arg, 'id') and not arg.id.startswith('_n_')):
                    print("Error: Passing unprotected variable to a protected argument at " + str(arg.lineno) + ".")
                elif(hasattr(arg, 'func') and not(arg.func.id.startswith('_n_') or arg.func.id == 'null_cast')):
                    print("Error: Passing unprotected function call to a protected argument at " + str(arg.lineno) + ".")
                #for e in dir(arg):
                    #print(e)

    def visit_FunctionDef(self, node):
        
        # only for the case of functions having no return statements
        NoReturnStatements = True
        
        if(node.name.startswith('_n_')):
            for line in node.body:
                if(isinstance(line, ast.Return)):
                    NoReturnStatements = False

                    if(hasattr(line.value, 'id') and not line.value.id.startswith('_n_')):
                        print("Error: Protected function returning an unprotected variable at " + str(line.value.lineno) + ".")
                    if(hasattr(line.value, 'value') and line.value.value == None):
                        print("Error: Protected function returning 'None' at " + str(line.value.lineno) + ".")
                    if(hasattr(line.value, 'func') and not line.value.func.id.startswith('_n_')):
                        print("Error: Protected function returning the result of an unprotected function at " + str(line.value.lineno) + ".")
            if(NoReturnStatements):
                print("Error: Protected function with no return statements at " + str(node.lineno) + ".")


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as code_file:
        code = code_file.read()
        tree = ast.parse(code)
        
        populator = PopulateFunctionsToParameters()
        visitor = Problem1Visitor()
        
        #populate variables
        populator.visit(tree)
        #print(FunctionsToParameters)
        
        #run the visitor
        visitor.visit(tree)

        
        
