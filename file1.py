import ast, sys

FunctionsToParameters = {}
ReturnLineNumbers = []

class PopulateFunctionsToParameters(ast.NodeVisitor):
    
    def visit_FunctionDef(self, node):
        #print(dir(node.args.args))
        #print(node.name)
        FunctionsToParameters[node.name] = {}
        for i, arg in enumerate(node.args.args):
            #print(arg.arg)
            FunctionsToParameters[node.name][i] = (arg.arg)
    
    #def visit_Return(self, node):
        
        #for e in dir(node):
            #print(e)
        #ReturnLineNumbers.append(node.lineno)


class Problem1Visitor(ast.NodeVisitor):
    
    def visit_BinaryOp(self, node):
        print(node)
        
    def visit_Assign(self, node):
        if(node.targets[0].id.startswith('_n_')):
            
            if(hasattr(node.value, 'value') and node.value.value == None):
                print("Error! Assigning 'None' to a protected variable at " + str(node.value.lineno) + ".")
                
            if(hasattr(node.value, 'id') and not node.value.id.startswith('_n_')):
                print("Error! Assigning an unprotected variable to a protected variable at " + str(node.value.lineno) + ".")
                
            if(hasattr(node.value, 'func') and not node.value.func.id.startswith('_n_')):
                print("Error! Assigning an unprotected function to a protected variable at " + str(node.value.func.lineno) + ".")
            
    def visit_Call(self, node):
        for i, arg in enumerate(node.args):
            print(node.lineno)
            if(node.func.id in FunctionsToParameters and FunctionsToParameters[node.func.id][i].startswith('_n_')):

                if(hasattr(arg, 'value') and arg.value == None) :
                    print("Error! Passing 'None' to a protected argument at " + str(arg.lineno) + ".")
                elif(hasattr(arg, 'id') and not arg.id.startswith('_n_')):
                    print("Error! Passing unprotected variable to a protected argument at " + str(arg.lineno) + ".")

    #def visit_Return(self, node):

        #print(node.lineno)
        #print(node.value)
        #if(hasattr(node.value, 'ctx')):
            #print("ld")
            #print(node.value.ctx)
            #for e in dir(node.value.ctx):
                #print(e)
        #if(hasattr(node.value, 'id')):
            #print(node.value.id)
        #for e in dir(node.value):
            #print(e)

    def visit_FunctionDef(self, node):
        
        # only for the case of functions having no return statements
        NoReturnStatements = True
        
        #print(node.lineno)
        #for e in dir(node):
            #print(e)
        print("nm")
        print(node.name)
        if(node.name.startswith('_n_')):
            #print("rets")
            #print(node.returns)
            #empty
            
            #print(node.body)
            #print("bodyy")
            for line in node.body:
                if(isinstance(line, ast.Return)):
                    NoReturnStatements = False
                    # has attribute "value". sometimes has attribute "targets"
                    
                    #print("=======")
                    #print(line.lineno)
                    #print(line.value)
                    #for e in dir(line.value):
                        #print(e)
                    #if(hasattr(line, 'value')):
                    if(hasattr(line.value, 'id') and not line.value.id.startswith('_n_')):
                        print("Error! Protected function returning an unprotected variable at " + str(line.value.lineno) + ".")
                    if(hasattr(line.value, 'value') and line.value.value == None):
                        print("Error! Protected function returning 'None' at " + str(line.value.lineno) + ".")
                #if(hasattr(line, 'func')):
                    #for e in dir(line.func):
                        #print(e)
                    if(hasattr(line.value, 'func') and not line.value.func.id.startswith('_n_')):
                        print("Error! Protected function returning a call to an unprotected function at " + str(line.value.lineno) + ".")
            
            if(NoReturnStatements):
                print("Error! Protected function with no return statements at " + str(node.lineno) + ".")


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as code_file:
        code = code_file.read()
        tree = ast.parse(code)
        
        populator = PopulateFunctionsToParameters()
        visitor = Problem1Visitor()
        
        #populate variables
        populator.visit(tree)
        
        print(FunctionsToParameters)
        print(ReturnLineNumbers)
        
        #run the visitor
        visitor.visit(tree)

        
        
