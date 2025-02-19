class BSTNode:
    def __init__(self, key,value,left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
class BST:
    def __init__(self):
        self.root = None

    def put(key,val):
        pass
        #for next time!

    def get(self,key):
        return self._get(key,self.root)

    def _get(self,key,node):
        if node is None:return None #search miss
        if key < node.key:
            return self._get(key,node.left)
        if key > node.key:
            return self._get(key,node.right)

    def get_min(self):
        return self._get_min(self.root)

    def _get_min(self,node):
        if node.left is None: return self.value
        return self._get_min(node.left)

    def get_max(self):
        return self._get_max(self.root)
    
    def _get_max(self,node):
        if node.right is None: return self.value
        return self._get_max(node.right)

    #floor of "key" largest key <= "key"
    def floor(self,key):
        return self._floor(key,self.root)

    def _floor(self,key,node):
        if node is None: return None
        if key == node.key: return key
        if key < node.key: return self._floor(key,node.left)
        if key > node.key:
            fl = self._floor(key, node.right)
            if fl: return fl
            return node.key

    def ceil(self,key):
        return self._ceil(key,self.root)

    def _ceil(self,key,node):
        if node is None: return None
        if key == node.key: return key
        if key > node.key: return self._ceil(key,node.right)
        if key < node.key:
            cl = self._ceil(key, node.left)
            if cl: return cl
            return node.key
    