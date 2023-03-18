# Write a function/method to insert an element by index to linked list in array structure
# with a char type node. For example, given ls = Head->S->t->i->n->g->None, the new
# one will be Head->S->t->r->i->n->g->None by calling function insertElem(ls, 3, 'r').

import numpy as np 


class Node:
    def __init__(self, data, idx):
        self.data = data
        self.idx = idx
    
def insertElem(ls, pos, value):
    new_node = Node(value, None)
    prev_node = ls[pos-1]
    next_node = prev_node.idx
    new_node.idx = next_node

    prev_node.idx = new_node

    for i in range(pos, len(ls)):
        if ls[i].idx is not None:
            ls[i].idx += 1
        else: 
            ls[i].idx = 1
    
    ls = np.insert(ls, pos, new_node)

    return ls

elm0 = Node('Head->', 1)
elm1 = Node('S->', 2)
elm2 = Node('t->', 3)
elm3 = Node('i->', 4)
elm4 = Node('n->', 5)
elm5 = Node('g->', 6)
elm6 = Node('None', 7)
ls = np.array([elm0, elm1, elm2, elm3, elm4, elm5, elm6])

print([node.data for node in ls])

ls = insertElem(ls, 3, 'r->')

print([node.data for node in ls])
