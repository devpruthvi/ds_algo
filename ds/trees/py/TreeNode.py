class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
    
    def __str__(self):
        return str(self.val)
    
    def __repr__(self):
        return str(self.val)