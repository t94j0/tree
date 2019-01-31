#include <iostream>
#include <memory>

template <class T> class BinaryTree {
public:
  BinaryTree(T val) : value(val){};
  void set_left(std::shared_ptr<BinaryTree<T>>);
  void set_right(std::shared_ptr<BinaryTree<T>>);

  void print_inorder();
  void print_preorder();
  void print_postorder();

private:
  T value;
  std::shared_ptr<BinaryTree> left;
  std::shared_ptr<BinaryTree> right;
};

template <class T>
void BinaryTree<T>::set_left(std::shared_ptr<BinaryTree<T>> l) {
  left = l;
}

template <class T>
void BinaryTree<T>::set_right(std::shared_ptr<BinaryTree<T>> r) {
  right = r;
}

template <class T> void BinaryTree<T>::print_inorder() {
  if (left)
    left->print_inorder();
  std::cout << value << std::endl;
  if (right)
    right->print_inorder();
}

template <class T> void BinaryTree<T>::print_preorder() {
  std::cout << value << std::endl;
  if (left)
    left->print_preorder();
  if (right)
    right->print_preorder();
}

template <class T> void BinaryTree<T>::print_postorder() {
  if (left)
    left->print_preorder();
  if (right)
    right->print_preorder();
  std::cout << value << std::endl;
}
