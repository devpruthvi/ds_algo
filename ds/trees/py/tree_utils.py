from TreeNode import TreeNode
import random
from enum import Enum

class ChildDirection(Enum):
    LEFT = 0
    RIGHT = 1


class TreeUtils:
    def get_random_binary_tree(n=10):
        if n == 0:
            return
        i = 1
        root = TreeNode(i)
        i += 1
        free_nodes = [(root, ChildDirection.LEFT), (root, ChildDirection.RIGHT)]
        while i <= n:
            insert_at, direction = random.choice(free_nodes)
            random_node = TreeNode(i)
            free_nodes.extend([(random_node, ChildDirection.LEFT), (random_node, ChildDirection.RIGHT)])
            i += 1
            if direction == ChildDirection.LEFT:
                insert_at.left = random_node
            elif direction == ChildDirection.RIGHT:
                insert_at.right = random_node
            free_nodes.remove((insert_at, direction))
        return root

    def get_height(root):
        if root == None:
            return 0
        else:
            return max(TreeUtils.get_height(root.left), TreeUtils.get_height(root.right)) + 1
    
    def get_levels(root):
        if root == None:
            return []
        levels = [[root]]
        cur_level = levels[-1]
        while True:
            next_level = []
            allNone = True
            for node in cur_level:
                if node == None:
                    next_level += [None, None]
                    continue
                if node.left != None:
                    allNone = False
                next_level.append(node.left)
                if node.right != None:
                    allNone = False
                next_level.append(node.right)
            if allNone:
                break
            levels.append(next_level)
            cur_level = next_level
        return levels
        
    def print_tree(root):
        if root == None:
            return
        h = TreeUtils.get_height(root)

    