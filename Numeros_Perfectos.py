#¿what if?
#arboles de algoritmo
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursively(node.right, key)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

# Ejemplo de uso
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(8)
    tree.insert(6)
    tree.insert(7)
    tree.insert(9)

    print("Recorrido en orden del árbol binario:")
    tree.inorder_traversal(tree.root)
    print("Recorrido en orden del ord")
    tree.inorder_traversal(tree.root)

# ¿qué pasa si insertamos un valor que ya existe en el árbol?
    tree.insert(6)
    print("Recorrido en orden del árbol binario:")
    tree.inorder_traversal(tree.root)
    print("Recorrido en orden del ord")
    tree.inorder_traversal(tree.root)
# Ahora el árbol no es un árbol binario, ya que hay dos nodos con el valor 6.
