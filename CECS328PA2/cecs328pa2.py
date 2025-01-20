class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse(x):
    if x is not None:
        x.val = 1
        traverse(x.left)
        traverse(x.right)
   
def print_tree(x):
    if x is None:
        print ("None", end='')
    else:
        print(f'TreeNode({x.val}, ', end= '')
        print_tree(x. left)
        print(', ', end='')
        print_tree(x. right)
        print(')', end='')

def my_function(x):
    traverse(x)
    print_tree(x)
    print("") #this creates a new line after the printed result

