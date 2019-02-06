# Binary Search Tree
class BinaryTree():
    def __init__(self,
                 x,
                 left: 'BinaryTree' = None,
                 right: 'BinaryTree' = None,
                 parent: 'BinaryTree' = None):
        self._value = x
        self._left = left
        self._right = right
        self._parent = parent

    def __len__(self):
        left = len(self._left) if self._left is not None else 0
        right = len(self._right) if self._left is not None else 0
        return sum([1, left, right])

    def __max__(self):
        return max(self._right) if self._right is not None else self._value

    def __str__(self):
        return ' '.join([
            str(self._left) if self._left != None else '',
            str(self._value),
            str(self._right) if self._right != None else ''
        ])

    def depth(self):
        if self._left == None and self._right == None:
            return 1
        if self._left == None and self._right != None:
            return self._right.depth() + 1
        if self._left != None and self._right == None:
            return self._left.depth() + 1
        return max(self._left.depth(), self._right.depth()) + 1

    def insert(self, x) -> None:
        val = BinaryTree(x)
        self._insert(val)

    def _insert(self, x: 'BinaryTree'):
        if self._value >= x._value:
            return self._set_left(
                x) if self._left == None else self._left._insert(x)

        if self._value < x._value:
            return self._set_right(
                x) if self._right == None else self._right._insert(x)

    def _set_left(self, x: 'BinaryTree') -> 'BinaryTree':
        self._left = x
        x._parent = self
        return self

    def _set_right(self, x: 'BinaryTree') -> 'BinaryTree':
        self._right = x
        if x is not None:
            x._parent = self
        return self

    def _rotate_left(self):
        y = self._left
        x = y._right
        T2 = x._left
        y._set_right(T2)
        x._set_left(y)
        self._set_left(x)

    def is_balanced(self) -> bool:
        left = self._left.depth() if self._left is not None else 0
        right = self._right.depth() if self._right is not None else 0
        return abs(left - right) <= 1


if __name__ == '__main__':
    root = BinaryTree(10)
    root.insert(6)
    root.insert(4)
    root.insert(8)
    root.insert(7)
    root.insert(9)
    root.insert(11)

    print(root._left)
    root._rotate_left()
    print(root._left._left)
