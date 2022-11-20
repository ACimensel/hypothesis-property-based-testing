from typing import TypeVar, Dict

from relational import *

from collections import Counter


# TODO: Complete the sequential sort checking here
def is_valid_sort(original,
                  after,
                  cmp) -> bool:
    # Property 1: 'original' and 'after' must be of type list
    if type(original) != list:
        print("'original' must be of type list")
        return False
    if type(after) != list:
        print("'after' must be of type list")
        return False

    # Property 2: size of the lists must remain the same
    if len(original) != len(after):
        print("Length of lists don't match")
        return False

    for index, item in enumerate(after):
        if index < len(after) - 1:
            diff = cmp(after[index], after[index + 1])
            # Property 3: result of the comparison function should be of type int
            if type(diff) != int:
                print("The result of the comparison function should be of type int")
                return False
            # Property 4: 'after' list must be in ascending sorted order
            if diff > 0:
                print("The 'after' list is not sorted in ascending order")
                return False

    # Property 5: frequency of the integers in each list must be the same
    counter_original = Counter(original)
    counter_after = Counter(after)
    counter_diff = counter_after - counter_original
    if len(counter_diff) != 0:
        print("The 'after' and 'original' lists do not contain the same frequency of elements")
        return False

    # Meets all properties, pass
    return True


# TODO: Complete the topological sort checking here
def is_valid_toposort(original,
                      after,
                      edges) -> bool:
    # Property 1: 'original', 'after', and 'edges' must be of type list
    if type(original) != list:
        print("'original' must be of type list")
        return False
    if type(after) != list:
        print("'after' must be of type list")
        return False
    if type(edges) != list:
        print("'edges' must be of type list")
        return False

    # Property 2: size of the lists of nodes must remain the same
    if len(original) != len(after):
        print("Length of node lists don't match")
        return False

    # Property 3: frequency of the integers in each list must be the same
    counter_original = Counter(original)
    counter_after = Counter(after)
    counter_diff = counter_after - counter_original
    if len(counter_diff) != 0:
        print("The 'after' and 'original' lists do not contain the same frequency of elements")
        return False

    # Property 4: nodes must be unique in a list, i.e. no two nodes are labeled with the same integer value
    most_common = counter_original.most_common(1) # checking 'original' is enough since Property #3 ensured they contain the same elements
    if len(most_common) > 0 and most_common[0][1] != 1:
        print("A node repeats more than once in the list 'original' and 'after' lists")
        return False

    node_dict = {}
    for index, item in enumerate(after):
        # Property 5: nodes in DAG list are of type integer
        node_dict[item] = index
        if type(item) != int:
            print("DAG list contains non integer values")
            return False
    for edge in edges:
        # Property 6: all edges should be of size two
        if len(edge) != 2:
            print("Edge does not contain exactly 2 nodes")
            return False
        # Property 7: DAG should not have self-loops
        if edge[0] == edge[1]:
            print("DAG cannot have self-loops")
            return False
        # Property 8: nodes in each edge exist in the DAG, also ensures nodes in edges are of type int
        if edge[0] not in node_dict:
            print("Node ", edge[0], " in edge ", edge, " is not a node in the DAG")
            return False
        if edge[1] not in node_dict:
            print("Node ", edge[1], " in edge ", edge, " is not a node in the DAG")
            return False
        # Property 9: 'after' is in topological order, i.e. no edges that lead backwards, or
        # linear ordering of vertices such that for every directed edge (u, v), vertex u comes before v in the ordering
        if node_dict[edge[1]] < node_dict[edge[0]]:
            print("There is an edge that leads backwards")
            return False

    # Meets all properties, pass
    return True
