from collections import Counter
from random import shuffle
from hypothesis import given, example
import hypothesis.strategies as st

from relational import sortish, toposortish
from invariants import is_valid_sort, is_valid_toposort


# NOTE: The invariants that you define might be  broken into several smaller
# invariants, as we saw in class. In practice, you could have a separate
# test for each individual invariant. That would provide you a more
# descriptive test failure in those cases where the invariant fails.
#
# For our purposes, we are defining a single invariant function,
# such as `is_valid_sort()`, so that you can decide what properties you
# want to include in your invariants while we focus on the test data
# generation and test outcomes during grading.

###write custom case for each property, ex. where lengths don't match
@given(st.lists(st.integers()))  ###Gives some list of integers, don't care about values
# @example([])
def test_sort_integers(integers):  ###Returns nothing
    original = integers[:]
    comparison = lambda x, y: x - y
    sortish(integers, comparison)

    # NOTE: Your implementation of is_valid_sort should
    # be implemented within `is_valids.py`. You will end
    # up submitting only that one file.
    assert is_valid_sort(original, integers, comparison)


class Cat:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Cat({}, {})'.format(self.name, self.age)


@given(st.lists(st.builds(Cat,
                          st.text(alphabet="acdefghijklmnopqrstuvwxyz", min_size=1),
                          st.integers(min_value=2, max_value=5))))
def test_sort_objects(cats):
    original = cats[:]
    compare_ages = lambda x, y: x.age - y.age
    sortish(cats, compare_ages)
    assert is_valid_sort(original, cats, compare_ages)


@st.composite
def directed_acyclic_graphs(draw, min_size: int = 0, max_size: int = 20):
    node_count = draw(st.integers(min_value=min_size, max_value=max_size))
    nodes = list(range(node_count))
    shuffle(nodes)
    edges = [(source, target) for index, source in enumerate(nodes)
             for target in nodes[index + 1:]
             if draw(st.booleans())]
    nodes.sort()
    return (nodes, edges)


@given(directed_acyclic_graphs())
def test_toposort(dag):
    original, edges = dag
    nodes = toposortish(original, edges)
    assert is_valid_toposort(original, nodes, edges)


if __name__ == "__main__":
    d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18, 10, 10]
    counter = Counter(d)
    print("counter", counter)
    print("counter_original.most_common: ", counter.most_common(1))
    print("counter_original.most_common: ", counter.most_common(1)[0])
    print("counter_original.most_common: ", counter.most_common(1)[0][1])