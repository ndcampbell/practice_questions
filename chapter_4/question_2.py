#given sorted (inceasing) array, write algo to make BST with minimal height

#example list: [1,2,3,4,5,6]

def build_bst(sorted_list, start, end):
    if len(sorted_list) == 1:
        node = Node(sorted_list[0])
        return node
    mid = len(sorted_list)/2
    node = Node(sorted_list[mid])
    left = sortedlist[0:mid]
    right = sortedlist[mid:0]
    node.left = build_bst(left)
    node.right = build_bst(right)
    return node



