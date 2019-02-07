class SplayTree():
    def __init__(self,
                 x,
                 left: 'SplayTree' = None,
                 right: 'SplayTree' = None,
                 parent: 'SplayTree' = None):
        self._value = x
        self._left = left
        self._right = right
        self._parent = parent

    def __str__(self):
        return ' '.join([
            str(self._left) if self._has_left() else '',
            str(self._value),
            str(self._right) if self._has_right() else ''
        ])

    def insert(self, x) -> None:
        val = SplayTree(x)
        new_node = self._insert(val)
        return self._splay(new_node)

    def _insert(self, x: 'SplayTree') -> 'SplayTree':
        if self._value >= x._value:
            return self._set_left(
                x) if self._left == None else self._left._insert(x)

        if self._value < x._value:
            return self._set_right(
                x) if self._right == None else self._right._insert(x)

    def _set_left(self, x: 'SplayTree') -> 'SplayTree':
        self._left = x
        x._parent = self
        return self

    def _set_right(self, x: 'SplayTree') -> 'SplayTree':
        self._right = x
        if x is not None:
            x._parent = self
        return self

    def _has_left(self) -> bool:
        return self._left != None

    def _has_right(self) -> bool:
        return self._right != None

    def _splay(self, target) -> 'SplayTree':
        pass


if __name__ == '__main__':
    root = SplayTree(10)
    root.insert(6)
    root.insert(4)
    root.insert(8)
    root.insert(7)
    root.insert(9)
    root.insert(11)
    print(root)
