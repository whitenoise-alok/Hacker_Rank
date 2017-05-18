import sys
sys.setrecursionlimit(15000)


class Tree:
    def __init__(self, val):
        self.n = val
        self.r = None
        self.l = None




def add_node(tree, parent_node, node, place):
    if tree.n == parent_node:
        if place == 'left':
            tree.l = Tree(node)
        if place == 'right':
            tree.r = Tree(node)
    else:
        if tree.l:
            add_node(tree.l, parent_node, node, place)
        if tree.r:
            add_node(tree.r, parent_node, node, place)



def swap_node(tree, d, d_count):
    if tree.n ==1:
        d_count=1
    if d == d_count:
        temp = tree.r
        tree.r = tree.l
        tree.l = temp
    else:
        d_count += 1
        if tree.l:
            swap_node(tree.l, d, d_count)
        if tree.r:
            swap_node(tree.r, d, d_count)


def print_in_order(tree):
    if tree:
        print_in_order(tree.l)
        print(tree.n),
        print_in_order(tree.r)

def get_max_depth(tree):

    if not tree:
        return 0
    else:
        depth_1 = get_max_depth(tree.l)
        depth_2 = get_max_depth(tree.r)

        depth = max(depth_1, depth_2)
        depth = depth +1
        return depth


if __name__ == '__main__':
    nodes = int(raw_input().strip())
    tree = Tree(1)
    for node in xrange(nodes):
        temp_nodes = raw_input().strip()
        left_node = int(temp_nodes.split()[0])
        right_node = int(temp_nodes.split()[1])
        if left_node !=-1:
            add_node(tree, node+1, left_node, 'left')
        if right_node != -1:
            add_node(tree, node+1, right_node, 'right')
        # print_in_order(tree)

    max_depth = get_max_depth(tree)
    # print 'max depth:', max_depth
    no_operations = int(raw_input().strip())

    swap_k_list = []
    for operation in xrange(no_operations):
        swap_k = int(raw_input().strip())
        swap_k_list.append(swap_k)

    for swap_k in swap_k_list:
        no_swaps = max_depth/swap_k
        # print swap_k, no_swaps
        d=0

        for swap in xrange(no_swaps):
            d_count = 1
            d=d+swap_k
            # print d, d_count
            swap_node(tree,d,d_count)

        print_in_order(tree)
        print ''