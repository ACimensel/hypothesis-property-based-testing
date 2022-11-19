from typing import TypeVar, Dict

from relational import *

from collections import Counter


# TODO: Complete the sequential sort checking here
def is_valid_sort(original,
                  after,
                  cmp) -> bool:

    counter = Counter(after)
    print('\n', after)
    print(counter)
    print(len(counter))
    counter2 = counter - counter
    print(len(counter2))

    # Property 1: size of the lists must remain the same
    if len(original) != len(after):
        print("Length of lists don't match")
        return False

    for index, item in enumerate(after):
        # Property 2: list types must be the integers
        # if type(original[index]) != int:
        #     print("The 'original' contains a non integer value")
        #     return False
        # if type(after[index]) != int:
        #     print("The 'after' contains a non integer value")
        #     return False

        # Property 3: 'after' list must be in ascending sorted order
        if index < len(after) - 1:
            diff = cmp(after[index], after[index + 1])
            if diff > 0:
                print("The 'after' list is not sorted in ascending order")
                return False

    # Property 4: frequency of the integers in each list must be the same
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
    # return False
    return True
