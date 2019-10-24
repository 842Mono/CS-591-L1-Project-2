import ast, sys

class Problem1Visitor(ast.NodeVisitor):
    def visit_BinaryOp(self, node):
        print(node)
        
    def visit_Assign(self, node):
        #print(node)
        #print(dir(node))
        #print("^dir")
        #print(node.targets)
        #print("^targets")
        #print(node.targets[0])
        print(node.targets[0].id)
        #print(dir(node.targets[0]))
        #print("^sth")
        print(node.value)
        print(node.value.lineno)
        print(dir(node.value))
        #print(node.value.n)
        print("^value")
        

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as code_file:
        code = code_file.read()
        tree = ast.parse(code)
        #solution(tree) # your solution function
        #print(tree)
        
visitor = Problem1Visitor()
visitor.visit(tree)

        
        
