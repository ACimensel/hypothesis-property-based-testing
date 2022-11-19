
from functools import cmp_to_key
from collections.abc import Callable
from typing import TypeVar, MutableSequence

import networkx as nx # type: ignore

E = TypeVar('E')


def sortish(sequence, cmp) -> None:
    sequence.sort(key=cmp_to_key(cmp))


def toposortish(nodes, edges):
    dag = nx.DiGraph()
    dag.add_nodes_from(nodes)
    dag.add_edges_from(edges)
    return list(nx.topological_sort(dag))


