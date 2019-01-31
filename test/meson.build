gtest_dep = dependency('gtest', main: 'true', fallback: ['gtest', 'gtest_main_dep'])

test_builder = executable('test_tree', 'tree_test.cpp', dependencies: [gtest_dep, tree_dep])


test('constructor test', test_builder)
