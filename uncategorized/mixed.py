class Node:
    def __init__(self, left=None, right=None,val=None):
        self.left = left
        self.right = right
        self.val = val
    
    def isLeaf(self):
        return self.left == None and self.right == None 

    def inOrder(n):
        if n == None:
            return
        Node.inOrder(n.left)
        print(n.val)
        Node.inOrder(n.right)
    
    def levelOrder(n):
        stack = [n]
        while stack != []:
            node = stack.pop(0)
            if node == None:
                return
            print(node.val)
            stack.append(node.left)
            stack.append(node.right)
    def __str__(self):
        return str(self.val)
    
    def __repr__(self):
        return str(self.val)


def mirrorTree(node):
    if node.isLeaf():
        return
    else:
        mirrorTree(node.left)
        mirrorTree(node.right)
        node.left, node.right = node.right, node.left
        
        

d = Node(val=4)
e = Node(val=5)
f = Node(val=6)
g = Node(val=7)
b = Node(d, e, 2)
c = Node(f, g, 3)
a = Node(b, c, 1)

def get_all_paths(node):
    if node == None:
        return []
    if node.left == None and node.right == None:
        return [[node]]
    left_paths = get_all_paths(node.left)
    right_paths = get_all_paths(node.right)

    for i in left_paths:
        i.append(node.val)
    for i in right_paths:
        i.append(node.val)
    left_paths.extend(right_paths)
    return left_paths


def buildTree(inorder, preorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return Node(val=inorder)
    root_i = inorder.index(preorder[0])
    left_inorder = inorder[0:root_i]
    right_inorder = inorder[root_i + 1:]
    left_preorder = preorder[1: 1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder) :]
    return Node(buildTree(left_inorder, left_preorder), buildTree(right_inorder, right_preorder), preorder[0] )

Node.levelOrder(buildTree("DBAC", "ABDC"))
    

print(get_all_paths(a))
        