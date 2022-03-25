from typing import Hashable


Node = Hashable


class DijkstraAlgorithm:
    __actual_costs: dict[Node, int]
    __parents: dict[Node, Node]

    def __init__(self, link_dictionary: dict[Node, dict[Node, int]], start_node: Node):
        not_processed_nodes: set[Node] = set(link_dictionary[start_node].keys())
        self.__actual_costs: dict[Node, int] = link_dictionary[start_node]
        self.__parents: dict[Node, Node] = {neighbor: start_node for neighbor in link_dictionary[start_node]}
        while not_processed_nodes:
            node: Node = min(not_processed_nodes, key=self.__actual_costs.get)
            not_processed_nodes.remove(node)
            cost_for_node: int = self.__actual_costs[node]
            for neighbor in link_dictionary[node]:
                new_cost_for_neighbor: int = cost_for_node + link_dictionary[node][neighbor]
                if neighbor not in not_processed_nodes:
                    not_processed_nodes.add(neighbor)
                    self.__actual_costs[neighbor] = new_cost_for_neighbor
                    continue
                actual_cost_for_neighbor: int = self.__actual_costs[neighbor]
                if new_cost_for_neighbor < actual_cost_for_neighbor:
                    self.__actual_costs[neighbor] = new_cost_for_neighbor
                    self.__parents[neighbor] = node

    def calculate_way(self, target_node: Node) -> tuple[list[Node], int]:
        way: list[Node] = [target_node]
        current_node: Node = target_node
        while True:
            parent = self.__parents.get(current_node)
            if parent is None:
                break
            way.append(parent)
            current_node = parent
        way.reverse()
        return way, self.__actual_costs[target_node]
