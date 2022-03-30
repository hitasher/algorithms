from dataclasses import dataclass
from typing import Sequence


@dataclass
class Item:
    value: int
    weight: int


class KnapsackProblem:
    def __init__(self, items: Sequence[Item]):
        self.items: Sequence[Item] = items
        self.__max_weight: int = sum((item.weight for item in self.items))
        self.__matrix: list[list[int]] = [[0 for _ in range(len(self.items) + 1)] for _ in range(len(self.items) + 1)]

    def solve(self):
        self.__matrix = [[0 for _ in range(self.__max_weight + 1)] for _ in range(len(self.items) + 1)]
        matrix = self.__matrix
        for i in range(len(self.items) + 1):
            for j in range(self.__max_weight + 1):
                if i == 0 or j == 0:
                    matrix[i][j] = 0
                elif self.items[i - 1].weight <= j:
                    matrix[i][j] = max(
                        matrix[i - 1][j],
                        self.items[i - 1].value + matrix[i - 1][j - self.items[i - 1].weight]
                    )
                else:
                    matrix[i][j] = matrix[i - 1][j]
        print(matrix)

    def get_value_for_weight(self, weight: int):
        weight = min(weight, self.__max_weight)
        return self.__matrix[-1][weight]
