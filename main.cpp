#include <memory>

#include "tree.h"

int main() {
  auto root = BinaryTree<int>(10);
  root.set_left(std::make_shared<BinaryTree<int>>(9));

  root.print_preorder();
}
