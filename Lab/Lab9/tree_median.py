from data_structures.binary_tree import Tree


class TreeMedian(Tree):
    def find_median(self):
        result = self.pre_order_traversal(self.root, [])
        result = sorted(result)
        if self.size % 2 == 0:
            median = (result[self.size // 2] + result[self.size // 2 - 1]) / 2
            return median
        else:
            median = result[self.size // 2]
            return median

    def union(self, tree):
        new_tree = self
        nodes = tree.pre_order_traversal(tree.root, [])
        for value in nodes:
            if self.binary_search_tree(self.root, value) is None:
                new_tree.add_node(self.last, value)
        return new_tree


if __name__ == '__main__':

    t = TreeMedian()
    root = t.add_root(8)
    node_3 = t.add_node(root, 3)
    node_10 = t.add_node(root, 10)

    node_1 = t.add_node(node_3, 1)
    node_6 = t.add_node(node_3, 6)

    node_14 = t.add_node(node_10, 14)

    node_4 = t.add_node(node_6, 4)
    node_7 = t.add_node(node_6, 7)

    # print('Median is:', t.find_median())
    print("Before union:")
    for node in t:
        print(node, end=' ')
    print()

    t2 = Tree()
    root2 = t2.add_root(10)
    node_22 = t2.add_node(root2, 22)
    node_10 = t2.add_node(root2, 10)

    node_19 = t2.add_node(node_22, 19)
    node_13 = t2.add_node(node_22, 13)

    t3 = t.union(t2)
    print("After union:")
    for node in t:
        print(node, end=' ')
    print()
