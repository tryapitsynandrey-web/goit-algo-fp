import random
from typing import Optional


def analytical_probabilities() -> dict[int, float]:
    """Returns the analytical probabilities of rolling sums of two six-sided dice."""
    return {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36,
    }


def simulate_dice_rolls(trials: int, seed: Optional[int] = None) -> dict[int, float]:
    """Simulates rolling two six-sided dice and calculates the probabilities of each sum."""
    if trials <= 0:
        raise ValueError("Trials must be positive.")

    if seed is not None:
        random.seed(seed)

    counts = {i: 0 for i in range(2, 13)}

    for _ in range(trials):
        # random.randint(a, b) is inclusive
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        counts[roll1 + roll2] += 1

    probabilities = {k: v / trials for k, v in counts.items()}
    return probabilities


def compare_probabilities(
    simulated: dict[int, float], analytical: dict[int, float]
) -> dict[int, float]:
    """Calculates the absolute difference between simulated and analytical probabilities."""
    return {k: abs(simulated[k] - analytical[k]) for k in analytical}
