from typing import TypeAlias

# Node alias
Node: TypeAlias = str | int

# Represents edges from a node: {target_node: weight}
Edges: TypeAlias = dict[Node, float]

# Represents the adjacency list graph: {node: {target_node: weight}}
WeightedGraph: TypeAlias = dict[Node, Edges]
