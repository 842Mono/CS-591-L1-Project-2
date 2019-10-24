import ast, sys

class Problem1Visitor(ast.NodeVisitor):
    def visit_BinaryOp(self, node):
        print(node)
        
    def visit_Assign(self, node):
        #print(node.targets[0].id)
        if(node.targets[0].id.startswith('_n_')):
            #print(dir(node.value))
            if(hasattr(node.value, 'value') and node.value.value == None):
                print("Error! Assigning 'None' to a protected variable at " + str(node.value.lineno) + " .")
        
        if(hasattr(node.value, 'value')):
            print(node.value.value)
            print("v")
        if(hasattr(node.value, 'n')):
            print(node.value.n)
            print("n")
        

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as code_file:
        code = code_file.read()
        tree = ast.parse(code)
        #solution(tree) # your solution function
        #print(tree)
        
visitor = Problem1Visitor()
visitor.visit(tree)

        
        
