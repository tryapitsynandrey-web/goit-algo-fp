import pytest

from src.core.food_optimizer import REQUIRED_ITEMS, FoodItem, dynamic_programming, greedy_algorithm


def test_greedy_stays_within_budget():
    budget = 50
    result = greedy_algorithm(REQUIRED_ITEMS, budget)
    assert result["total_cost"] <= budget


def test_dp_stays_within_budget():
    budget = 50
    result = dynamic_programming(REQUIRED_ITEMS, budget)
    assert result["total_cost"] <= budget


def test_dp_returns_optimal_for_required_dataset():
    # With budget 100 on REQUIRED_ITEMS:
    # DP should find combinations giving more than Greedy if possible, or the exact optimal.
    # Let's test a known optimal.
    budget = 100
    dp_res = dynamic_programming(REQUIRED_ITEMS, budget)

    # We expect pizza (50,300) + potato (25,350) + cola (15,220) + pepsi (10,100)
    # Total cost: 100, Total calories: 970
    assert dp_res["total_calories"] == 970
    assert set(dp_res["selected_items"]) == {"pizza", "potato", "cola", "pepsi"}


def test_invalid_budget_rejection():
    with pytest.raises(ValueError, match="Budget cannot be negative"):
        greedy_algorithm(REQUIRED_ITEMS, -10)

    with pytest.raises(ValueError, match="Budget cannot be negative"):
        dynamic_programming(REQUIRED_ITEMS, -10)


def test_invalid_item_rejection():
    bad_items: dict[str, FoodItem] = {"bad": {"cost": 0, "calories": 100}}  # type: ignore
    with pytest.raises(ValueError, match="must have positive cost"):
        greedy_algorithm(bad_items, 10)

    bad_items2: dict[str, FoodItem] = {"bad": {"cost": 10, "calories": -100}}  # type: ignore
    with pytest.raises(ValueError, match="cannot have negative calories"):
        greedy_algorithm(bad_items2, 10)


def test_dp_outperforms_greedy():
    # Setup a scenario where Greedy picks a high ratio item but leaves leftover budget
    # that can't be used, while DP picks slightly lower ratio items that perfectly fill the budget.
    test_items: dict[str, FoodItem] = {  # type: ignore
        "item1": {"cost": 60, "calories": 600},  # Ratio: 10
        "item2": {"cost": 50, "calories": 400},  # Ratio: 8
        "item3": {"cost": 50, "calories": 400},  # Ratio: 8
    }
    budget = 100

    greedy_res = greedy_algorithm(test_items, budget)
    # Greedy picks item1. Cost=60. Remaining=40. Can't pick anything else. Total cal = 600.
    assert greedy_res["total_calories"] == 600

    dp_res = dynamic_programming(test_items, budget)
    # DP picks item2 + item3. Cost=100. Total cal = 800.
    assert dp_res["total_calories"] == 800
    assert dp_res["total_calories"] > greedy_res["total_calories"]
