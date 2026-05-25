from typing import Mapping, TypedDict


class FoodItem(TypedDict):
    cost: int
    calories: int


REQUIRED_ITEMS: dict[str, FoodItem] = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


class OptimizationResult(TypedDict):
    selected_items: list[str]
    total_cost: int
    total_calories: int


def validate_inputs(items: Mapping[str, FoodItem], budget: int) -> None:
    if budget < 0:
        raise ValueError("Budget cannot be negative.")
    for name, item in items.items():
        if item["cost"] <= 0:
            raise ValueError(f"Item '{name}' must have positive cost.")
        if item["calories"] < 0:
            raise ValueError(f"Item '{name}' cannot have negative calories.")


def greedy_algorithm(items: Mapping[str, FoodItem], budget: int) -> OptimizationResult:
    """Selects food items using a greedy approach based on calorie-to-cost ratio."""
    validate_inputs(items, budget)

    # Sort items by calories/cost ratio in descending order
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    selected = []
    total_cost = 0
    total_calories = 0

    for name, item in sorted_items:
        if total_cost + item["cost"] <= budget:
            selected.append(name)
            total_cost += item["cost"]
            total_calories += item["calories"]

    return {"selected_items": selected, "total_cost": total_cost, "total_calories": total_calories}


def dynamic_programming(items: Mapping[str, FoodItem], budget: int) -> OptimizationResult:
    """Selects food items using 0/1 knapsack dynamic programming for optimal calories."""
    validate_inputs(items, budget)

    item_names = list(items.keys())
    n = len(item_names)

    # dp[i][w] represents max calories using first i items and budget w
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Reconstruct selected items
    selected = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = item_names[i - 1]
            selected.append(name)
            w -= items[name]["cost"]

    selected.reverse()

    total_cost = sum(items[name]["cost"] for name in selected)
    total_calories = dp[n][budget]

    return {"selected_items": selected, "total_cost": total_cost, "total_calories": total_calories}
