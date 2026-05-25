# Data Structures and Algorithms Final Project

## Description

This repository contains the final course project demonstrating advanced proficiency in core data structures and algorithms in Python. The project is implemented using a strict modular architecture and satisfies all assignment criteria.

## Assignment Task Overview

1. **Linked List Operations**: Implement reverse, merge sort, and merging for singly linked lists by changing node references.

2. **Pythagoras Tree Fractal**: Generate and visualize a Pythagoras tree fractal using recursion.

3. **Dijkstra Shortest Path**: Compute shortest paths on a weighted graph using a binary heap (priority queue).

4. **Binary Heap Visualization**: Convert an array-based binary heap into a binary tree structure and visualize it with NetworkX.

5. **Tree Traversal Visualization**: Implement non-recursive (iterative) DFS using a stack and BFS using a queue, highlighting traversal order with a hex color gradient.

6. **Food Optimization**: Select optimal food items within a budget using a greedy algorithm (by calorie-to-cost ratio) and dynamic programming (0/1 knapsack).

7. **Monte Carlo Simulation**: Simulate rolling two six-sided dice, compute probabilities, compare with analytical expectations, and visualize the results.

## Architecture Overview

The project uses a clean modular architecture:

- `config/`: Application settings and constants.

- `src/models/`: Pure typed data structures (`LinkedListNode`, `TreeNode`, `graph_types`).

- `src/core/`: Algorithmic logic decoupled from visualization.

- `src/visualization/`: Rendering logic using `matplotlib` and `networkx`.

- `src/utils/`: Shared utilities (validation, colors, logging).

- `scripts/`: Thin executable entry points orchestrating data flow.

- `tests/`: Comprehensive `pytest` suite ensuring algorithmic correctness.

## Project Structure

```text
goit-algo-fp/
├── config/
│   └── settings.py
├── data/
│   └── outputs/                 # Generated visualizations
├── reports/
│   └── monte_carlo_summary.md   # Generated probability analysis
├── scripts/                     # Executable tasks
├── src/
│   ├── core/                    # Core algorithms
│   ├── models/                  # Data models
│   ├── utils/                   # Helpers
│   └── visualization/           # Plotters
└── tests/                       # Pytest test suite

```

## Installation

Ensure you have Python 3.11+ installed.

```bash

# Create and activate virtual environment (optional but recommended)

python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies

pip install -r requirements.txt

```

## How to Run All Tasks

To execute all assignment tasks sequentially, run:

```bash
python scripts/run_all.py

```

## How to Run Individual Tasks

You can run any task script individually:

```bash
python scripts/run_task_01_linked_list.py
python scripts/run_task_02_pythagoras_tree.py --depth 6
python scripts/run_task_03_dijkstra.py
python scripts/run_task_04_heap_visualization.py
python scripts/run_task_05_tree_traversals.py
python scripts/run_task_06_food_optimization.py
python scripts/run_task_07_monte_carlo.py --trials 1000000

```

## Testing Instructions

To run the automated test suite, which verifies algorithmic correctness without relying on manual visual inspection:

```bash
python -m pytest -v

```

## Results Summary

- **Task 1**: Successfully reverses, sorts, and merges linked lists by manipulating node references directly.

- **Task 2**: Visually generates the Pythagoras tree. Depth is configurable via `--depth`. Output saved to `data/outputs/pythagoras_tree.png`.

- **Task 3**: Efficiently computes exact shortest paths using a binary heap, correctly rejecting negative weights.

- **Task 4**: Converts heap arrays to binary tree node references accurately and plots them to `data/outputs/binary_heap.png`.

- **Task 5**: Traverses graphs iteratively (DFS via stack, BFS via deque) and produces clear color gradients based on visit order. Plots saved to `data/outputs/dfs_traversal.png` and `data/outputs/bfs_traversal.png`.

- **Task 6**: Solves the food budget optimization. The DP knapsack guarantees an optimal calorie yield, while the greedy algorithm provides a fast approximation.

- **Task 7**: Demonstrates that high-trial Monte Carlo simulation converges to exact analytical probabilities.

## Monte Carlo Analytical Comparison Table

| Sum | Analytical Probability | Simulated Probability | Difference |
| --- | --- | --- | --- |
| 2 | 2.78% | 2.77% | 0.01% |
| 3 | 5.56% | 5.55% | 0.01% |
| 4 | 8.33% | 8.37% | 0.04% |
| 5 | 11.11% | 11.12% | 0.01% |
| 6 | 13.89% | 13.86% | 0.03% |
| 7 | 16.67% | 16.68% | 0.01% |
| 8 | 13.89% | 13.91% | 0.02% |
| 9 | 11.11% | 11.08% | 0.03% |
| 10 | 8.33% | 8.33% | 0.00% |
| 11 | 5.56% | 5.52% | 0.04% |
| 12 | 2.78% | 2.79% | 0.01% |

## Monte Carlo Conclusion

The Monte Carlo simulation accurately models the distribution of two six-sided dice rolls. The deviations observed between the simulated and analytical probabilities are consistently negligible (generally under 0.05% with 100,000 trials). This verifies the correctness of the analytical logic and demonstrates the Law of Large Numbers.

## Assumptions and Limitations

- Visualization node coordinates in NetworkX use simple hierarchical offsets; very large heaps might overlap nodes visually.

- The linked list merge sort relies on finding the middle using slow/fast pointers which requires multiple passes over sublists.

- Dijkstra's algorithm implemented does not support negative weights and will raise a `ValueError`.

- DP food optimization assumes budget and item costs are strictly non-negative integers.

## Skills Demonstrated

- Algorithm Implementation (Merge Sort, Dijkstra, DFS, BFS, Greedy, Dynamic Programming)

- Mathematical Modeling (Monte Carlo simulations, probability)

- Data Structure Design (Linked Lists, Binary Trees, Graphs, Priority Queues)

- Clean Architecture (Separation of concerns between logic, models, and visualization)

- Automated Testing (Pytest, edge-case coverage)

## Acceptance Criteria Mapping Table

| Task | Requirement | Implemented In | Verification Method | Status |
| --- | --- | --- | --- | --- |
| 1 | Reverse, sort, and merge linked lists by changing references | `src/core/linked_list.py` | `pytest tests/test_linked_list.py` | Complete |
| 2 | Recursive Pythagoras tree with user depth configuration | `src/core/fractal.py` | Run `scripts/run_task_02_pythagoras_tree.py` | Complete |
| 3 | Dijkstra shortest path using binary heap | `src/core/dijkstra.py` | `pytest tests/test_dijkstra.py` | Complete |
| 4 | Convert heap array to binary tree and visualize | `src/core/heap_tree.py` | Run `scripts/run_task_04_heap_visualization.py` | Complete |
| 5 | Iterative DFS/BFS visualization with hex color gradients | `src/core/tree_traversal.py` | `pytest tests/test_tree_traversal.py` | Complete |
| 6 | Greedy and DP optimization on assignment food dictionary | `src/core/food_optimizer.py` | `pytest tests/test_food_optimizer.py` | Complete |
| 7 | Monte Carlo dice probabilities vs Analytical probabilities | `src/core/monte_carlo.py` | Run `scripts/run_task_07_monte_carlo.py` | Complete |
