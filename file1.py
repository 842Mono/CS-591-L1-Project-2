import ast, sys

FunctionsToParameters = {}

class PopulateFunctionsToParameters(ast.NodeVisitor):
    
    def visit_FunctionDef(self, node):
        #print(dir(node.args.args))
        #print(node.name)
        FunctionsToParameters[node.name] = {}
        for i, arg in enumerate(node.args.args):
            #print(arg.arg)
            FunctionsToParameters[node.name][i] = (arg.arg)



class Problem1Visitor(ast.NodeVisitor):
    
    def visit_BinaryOp(self, node):
        print(node)
        
    def visit_Assign(self, node):
        if(node.targets[0].id.startswith('_n_')):
            
            # directly assigning None
            if(hasattr(node.value, 'value') and node.value.value == None):
                print("Error! Assigning 'None' to a protected variable at " + str(node.value.lineno) + ".")
                
            # assigning an unprotected variable to a protected variable
            if(hasattr(node.value, 'id') and not node.value.id.startswith('_n_')):
                print("Error! Assigning an unprotected variable to a protected variable at " + str(node.value.lineno) + ".")
                
            # assigning the return value of a function to a variable
            if(hasattr(node.value, 'func') and not node.value.func.id.startswith('_n_')):
                print("Error! Assigning non-protected function to a protected variable at " + str(node.value.func.lineno) + ".")
                
    #def visit_FunctionDef(self, node):
        #for e in dir(node):
            #print(e)
            
    def visit_Call(self, node):
        for i, arg in enumerate(node.args):
            print(node.lineno)
            #for e in dir(arg):
                #print(e)
            #print(node.func.id)
            #print(node.func.id in FunctionsToParameters)
            #if(node.func.id in FunctionsToParameters):
                #print(FunctionsToParameters[node.func.id][i].startswith('_n_'))
            #print(hasattr(arg, 'value'))
            if(node.func.id in FunctionsToParameters and FunctionsToParameters[node.func.id][i].startswith('_n_')):
                
                #print(FunctionsToParameters[node.func.id][i])
                #print(arg.value)
                if(hasattr(arg, 'value') and arg.value == None) :
                    print("Error! Passing 'None' to a protected argument at " + str(arg.lineno) + ".")
                #if(hasattr(arg, 'n')):
                    #for e in dir(arg.n):
                        #print(e)
                elif(hasattr(arg, 'id') and not arg.id.startswith('_n_')):
                    print("Error! Passing unprotected variable to a protected argument at " + str(arg.lineno) + ".")
        


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as code_file:
        code = code_file.read()
        tree = ast.parse(code)
        
        populator = PopulateFunctionsToParameters()
        visitor = Problem1Visitor()
        
        #populate FunctionsToParameters
        populator.visit(tree)
        
        print(FunctionsToParameters)
        
        #run the visitor
        visitor.visit(tree)

        
        
