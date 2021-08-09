from Binary_trees.tree_node import Tree
from collections import deque


def insert_bst(root, val):
    queue = deque([])
    if root == None:
        root = Tree(val)
        return root
    else:
        queue.append(root)
        while len(queue) != 0:
            curr = queue.popleft()

            if val == curr.data:
                print('value already present '.title())
                return root

            if val < curr.data:
                if curr.left:
                    queue.append(curr.left)
                else:
                    curr.left = Tree(val)
                    return root

            if val > curr.data:
                if curr.right:
                    queue.append(curr.right)
                else:
                    curr.right = Tree(val)
                    return root


def delete_bst(root, val):
    if root is None:
        return None
    elif val < root.data:
        root.left = delete_bst(root.left, val)
    elif val > root.data:
        root.right = delete_bst(root.right, val)
    else:
        if root.left and root.right:
            temp = find_max_bst(root.left)  # find max element in left subtree
            root.data = temp.data
            root.left = delete_bst(root.left, val)
        elif root.left is None and root.right is None:
            return None
        else:
            temp = root
            if root.left is None:
                root = root.right

            if root.right is None:
                root = root.left

            del temp
    return root


def find_min_bst(root):
    """find minimum BST"""
    if root == None:
        return None

    if root.left == None:
        return root
    else:
        return find_max_bst(root.left)


def find_max_bst(root):
    if root == None:
        return None

    if root.right == None:
        return root
    else:
        return find_max_bst(root.right)


def insrt_bst_recur(root, val):
    if root == None:
        root = Tree(val)
        return root
    else:
        if val < root.data:
            root.left = insrt_bst_recur(root.left, val)
        elif val == root.data:
            print('value already present'.title())
            return root
        else:
            root.right = insrt_bst_recur(root.right, val)
    return root


def rotate_left(root):
    temp = root
    root = root.left
    temp.left = root.right
    root.right = temp
    return root


def rotate_right(root):
    temp = root
    root = root.right
    temp.right = root.left
    root.left = temp
    return root


def d_rotate_left(root):
    root.left = rotate_right(root.left)
    return rotate_left(root)


def d_rotate_right(root):
    root.right = rotate_left(root.right)
    return rotate_right(root)


def range_nodes_bst(k1, k2, root):
    if root == None:
        return

    if k1 <= root.data and k2 >= root.data:
        print(root.data)

    if root.data >= k1:
        range_nodes_bst(k1, k2, root.left)
    else:
        range_nodes_bst(k1, k2, root.right)
