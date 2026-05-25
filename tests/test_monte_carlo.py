import pytest

from src.core.monte_carlo import analytical_probabilities, simulate_dice_rolls


def test_analytical_probabilities_correctness():
    """Tests that analytical probabilities sum to 1 and are exactly correct."""
    probs = analytical_probabilities()
    assert sum(probs.values()) == pytest.approx(1.0)
    assert probs[2] == 1 / 36
    assert probs[7] == 6 / 36
    assert probs[12] == 1 / 36


def test_simulated_sums_only_2_through_12():
    """Tests that only sums 2-12 are generated."""
    probs = simulate_dice_rolls(100, seed=42)
    assert set(probs.keys()) == set(range(2, 13))


def test_probabilities_sum_to_one():
    """Tests that simulated probabilities sum to approximately 1.0."""
    probs = simulate_dice_rolls(100, seed=42)
    assert sum(probs.values()) == pytest.approx(1.0)


def test_deterministic_seed():
    """Tests that a deterministic seed produces repeatable output."""
    probs1 = simulate_dice_rolls(100, seed=42)
    probs2 = simulate_dice_rolls(100, seed=42)
    assert probs1 == probs2


def test_high_trial_simulation_tolerance():
    """Tests that high-trial simulation approaches analytical probabilities."""
    trials = 100000
    sim = simulate_dice_rolls(trials, seed=42)
    ana = analytical_probabilities()

    for k in ana:
        # with 100k trials, error should be very small, e.g. < 0.5%
        assert abs(sim[k] - ana[k]) < 0.005
