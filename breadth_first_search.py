from collections import deque
from typing import Hashable, Iterable


def breadth_first_search(
        link_dictionary: dict[Hashable, Iterable[Hashable]], start_node: Hashable, target_node: Hashable
) -> Hashable | None:
    assert start_node in link_dictionary
    queue = deque(link_dictionary[start_node])
    visited_nodes = set()
    while queue:
        child = queue.popleft()
        if child in visited_nodes:
            continue
        if child == target_node:
            return child
        if child in link_dictionary:
            queue += link_dictionary[child]
        visited_nodes.add(child)
    return None
