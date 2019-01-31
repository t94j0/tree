#include <gtest/gtest.h>
#include <tree.h>

TEST(TreeTest, Constructor) {
  auto root = BinaryTree<int>(10);
  // ASSERT_EQ();
}

TEST(TreeTest, SetLeft) {
  auto root = BinaryTree<int>(10);
  root.set_left(std::make_shared<BinaryTree<int>>(9));
}

TEST(TreeTest, SetRight) {
  auto root = BinaryTree<int>(10);
  root.set_right(std::make_shared<BinaryTree<int>>(11));
}

TEST(TreeTest, SetBoth) {
  auto root = BinaryTree<int>(10);
  root.set_right(std::make_shared<BinaryTree<int>>(9));
  root.set_left(std::make_shared<BinaryTree<int>>(11));
}
