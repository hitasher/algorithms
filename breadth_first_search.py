from collections import deque
from typing import Hashable, Iterable


Node = Hashable


def breadth_first_search(
        link_dictionary: dict[Node, Iterable[Node]], start_node: Node, target_node: Node
) -> Node | None:
    assert start_node in link_dictionary
    queue: deque[Node] = deque(link_dictionary[start_node])
    visited_nodes: set[Node] = set()
    while queue:
        current_node: Node = queue.popleft()
        if current_node in visited_nodes:
            continue
        if current_node == target_node:
            return current_node
        if current_node in link_dictionary:
            queue += link_dictionary[current_node]
        visited_nodes.add(current_node)
    return None
