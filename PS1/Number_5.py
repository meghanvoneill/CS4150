class Node(object):

    def __init__(self, value, left=None, right=None, parent=None, depth=0, complete_depth=0, childrens_best_depth=0):
        self.value = value
        self.left = left
        self.parent = parent
        self.right = right
        self.depth = depth
        self.complete_depth = complete_depth
        self.childrens_best_depth = childrens_best_depth

    def __str__(self):
        return str(self.__class__) + ': ' + str(self.value)


def main():

    return


def find_largest_complete_subtree(root):

    # If root has no children, return.
    if root.left is None and root.right is None:
        root.complete_depth = 0
        return root

    # Pre-node traversal to bottom left leaf.
    if root.left is not None:
        left_leaf = find_largest_complete_subtree(root.left)

        # To ensure this root's subtree is complete, there must be a right child as well.
        if left_leaf.parent.right is not None:
            # We know our parent tree has both children and is a complete subtree by itself.
            left_leaf.parent.complete_depth = 1

            # We must recurse on the right node as the new subtree root, in case it also has children.
            right_node = find_largest_complete_subtree(left_leaf.parent.right)

            # Check which child has the better complete depth and update parent. If the children do not match
            #   one another, the complete depth of the parent will not change.
            if right_node.complete_depth > left_leaf.complete_depth:
                left_leaf.parent.childrens_best_depth = right_node.complete_depth
            elif right_node.complete_depth < left_leaf.complete_depth:
                left_leaf.parent.childrens_best_depth = left_leaf.complete_depth
            # If both children have the same complete depth, the parent has a complete depth of the children's + 1.
            else:
                left_leaf.parent.complete_depth = left_leaf.complete_depth + 1
                left_leaf.parent.childrens_best_depth = left_leaf.complete_depth
            return left_leaf.parent
        # There is no right child and this subtree is incomplete.
        else:
            left_leaf.parent.complete_depth = 0
            return left_leaf.parent
    # Otherwise, there is no left child and this subtree is incomplete.
    else:
        # We must recurse on the right node as the new subtree root, in case it also has children.
        right_node = find_largest_complete_subtree(root.right)
        # The only value to update would be if this node had a subtree that was best.
        if right_node.complete_depth > right_node.parent.childrens_best_depth:
            right_node.parent.childrens_best_depth = right_node.complete_depth


if __name__ == '__main__':
    main()



