import ast, sys

class Problem1Visitor(ast.NodeVisitor):
    def visit_BinaryOp(self, node):
        print(node)
        
    def visit_Assign(self, node):
        if(node.targets[0].id.startswith('_n_')):
            
            # directly assigning None
            if(hasattr(node.value, 'value') and node.value.value == None):
                print("Error! Assigning 'None' to a protected variable at " + str(node.value.lineno) + " .")
                
            # assigning an unprotected variable to a protected variable
            if(hasattr(node.value, 'id') and not node.value.id.startswith('_n_')):
                print("Error! Assigning an unprotected variable to a protected variable at " + str(node.value.lineno) + " .")
        

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as code_file:
        code = code_file.read()
        tree = ast.parse(code)
        
        visitor = Problem1Visitor()
        visitor.visit(tree)

        
        
