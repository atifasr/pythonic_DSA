# tree traversal methods
from collections import deque
from tree_node import Tree

queue = deque([])


def insert(root, val):
    """Tree insertion"""

    if root == None:
        root = Tree(val)
        return root
    else:
        queue.append(root)
        while len(queue) != 0:
            buff = queue.popleft()
            if buff.left:
                queue.append(buff.left)
            else:
                buff.left = Tree(val)
                return root
            if buff.right:
                queue.append(buff.right)
            else:
                buff.right = Tree(val)
                return root


def traverse(root):
    """level_order traversal using queue container"""
    q2 = deque([])
    q2.append(root)
    while len(q2) != 0:
        temp = q2.popleft()
        print('data -> '.title(), temp.data)
        if temp.left:
            q2.append(temp.left)

        if temp.right:
            q2.append(temp.right)

# preorder traversal


def pre_order(root):
    flag = 0
    stack = []
    if root == None:
        print('empty root'.title())
        return None

    curr = root

    while flag != 1:
        while curr:
            stack.append(curr)
            print(curr.data)
            curr = curr.left

        if len(stack) == 0:
            break
        curr = stack.pop()
        curr = curr.right


def in_order(root):
    print('inorder traversal'.title())
    flag = 0
    stack = []
    if root == None:
        print('empty root'.title())
        return None

    curr = root

    while flag != 1:
        while curr:
            stack.append(curr)
            curr = curr.left

        if len(stack) == 0:
            break
        curr = stack.pop()
        print(curr.data)
        curr = curr.right


def size_recur(root):
    if root == None:
        return 0
    else:
        return (size_(root.left)+1+size_(root.right))


def size_(root):
    size = 0
    q2 = deque([])
    q2.append(root)
    while len(q2) != 0:
        temp = q2.popleft()
        size += 1
        if temp.left:
            q2.append(temp.left)

        if temp.right:
            q2.append(temp.right)
    return size


def search_recu(root, val):
    if val == root.data:
        print(f'data {val} found at -> ', root.data)

    if root.left:
        search_recu(root.left, val)

    if root.right:
        search_recu(root.right, val)


def leaves(root):

    leaf_count = 0
    queue = deque([])
    queue.append(root)
    while(queue.__len__() != 0):
        curr = queue.popleft()

        if curr.left == None and curr.right == None:
            leaf_count += 1

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return leaf_count


def height_binary(root):
    """level / height of a binary tree """
    height = -1
    queue = deque([])
    if root == None:
        return 0
    queue.append(root)
    queue.append(None)
    while(queue.__len__() != 0):
        curr = queue.popleft()
        if curr == None:
            if queue.__len__() != 0:
                queue.append(None)
            height += 1
        else:
            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
    return height


def max_level_sum(root, *argv):
    height = 0
    prev_s, sum_ = 0, 0
    queue = deque([])
    queue.append(root)
    queue.append(None)
    max_level = 0
    while(queue.__len__() != 0):
        curr = queue.popleft()

        if curr != None:
            prev_s += curr.data

        if curr == None:
            if queue.__len__() != 0:
                queue.append(None)
            height += 1

            if prev_s > sum_:
                temp = prev_s
                prev_s = sum_
                sum_ = temp
                max_level = height

            prev_s = 0
        else:
            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
    return max_level


def path_nodes(root, lst):
    if root is None:
        return
    lst.append(root)
    # push nodes in a list
    if root.left is None and root.right is None:
        travr_arry(lst)

    else:
        path_nodes(root.left, lst)
        path_nodes(root.right, lst)


def travr_arry(lst):
    for val in lst:
        print(val.data)

# mirroring without recursion


def mirror(root):

    flag = 0
    stack = deque([])
    stack.append(root)
    while flag != 1:

        while root != None:
            root = root.left
            stack.append(root)

        if stack.__len__() == 0:
            break

        root = stack.pop()

        if root != None:
            temp = root.left
            root.left = root.right
            root.right = temp
            root = root.right


def inorder_to_pr_order(in_order_arr, pre_order_arr, inorder_start, inorder_end):
    pre_order_index = 0
    new_node = Tree()

    new_node.data = pre_order_arr[pre_order_index]
    pre_order_arr.popleft()

    if inorder_start > inorder_end:
        return None

    if inorder_start == inorder_start:
        return new_node

    in_order_index = search_inorder_index(
        in_order_arr, inorder_start, inorder_end, new_node.data)
    new_node.left = inorder_to_pr_order(
        in_order_arr, pre_order_arr, inorder_start, in_order_index-1)
    new_node.right = inorder_to_pr_order(
        in_order_arr, pre_order_arr, in_order_index+1, inorder_end)

    return new_node


def search_inorder_index(inorder_arr, start, end, val):

    for index in range(start, end):
        if val is inorder_arr[index]:
            return index

# revisit


def zig_zag(root):
    height = 0
    flag_chng = 0
    queue = deque([])
    left_right = deque([])
    right_left = deque([])
    queue.append(root)
    queue.append(None)
    while(queue.__len__() != 0):
        curr = queue.pop()

        if flag_chng == 0 and curr:
            left_right.append(curr)
        elif flag_chng and curr:
            right_left.append(curr)

        if curr == None:

            if queue.__len__() != 0:
                queue.append(None)
            height += 1
            if flag_chng is 1:
                flag_chng = 0
            else:
                flag_chng = 1
        else:
            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)


def deepest_node(root):
    q2 = deque([])
    q2.append(root)
    while len(q2) != 0:
        temp = q2.popleft()

        if temp.left:
            q2.append(temp.left)

        if temp.right:
            q2.append(temp.right)

    return temp


def ancestors(root, data):
    flag = 0
    stop = 0
    stack = []

    curr = root
    while flag != 1:

        if stop != 1:
            while curr.left != None:
                stack.append(curr)
                curr = curr.left

        if len(stack) == 0:
            break

        if curr.left != None:
            if curr.left.data == data:
                stop = 1
        elif curr.right != None:
            if curr.right.data == data:
                stop = 1

        if stop == 1:
            print(stack.pop().data)
        else:
            curr = stack.pop()
            curr = curr.right

# revisit


def no_of_nodes_bst(root):
    if root == None:
        return 0
    else:
        return no_of_nodes_bst(root.left)+1+no_of_nodes_bst(root.right)


def no_of_leaves_recur(root):
    """returns no of leaves """
    if root == None:
        return 0
    elif not(root.left) and not(root.right):
        return 1
    return no_of_leaves_recur(root.left)+no_of_leaves_recur(root.right)


def lca(root, alpha, beta):
    """ returns lowest common ancestor """
    if root == None:
        return root
    if root.data == alpha or root.data == beta:
        return root
    left = lca(root.left, alpha, beta)
    right = lca(root.right, alpha, beta)

    if left != None and right != None:
        return root
    else:
        if left:
            return left
        else:
            return right
