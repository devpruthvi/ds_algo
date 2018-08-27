from tree_utils import TreeUtils

class TreeTraversals:

    @staticmethod
    def inorder(node):
        if node == None:
            return
        TreeTraversals.inorder(node.left)
        print(node)
        TreeTraversals.inorder(node.right)
    
    @staticmethod
    def level_order(node):
        if node == None:
            return
        q = [node]
        while len(q) != 0:
            top = q.pop(0)
            print(top)
            if top.left != None:
                q.append(top.left)
            if top.right != None:
                q.append(top.right)

        
    

if __name__ == "__main__":
    tree = TreeUtils.get_random_binary_tree(20)
    print(TreeUtils.get_height(tree))
    print(TreeUtils.get_levels(tree))
        