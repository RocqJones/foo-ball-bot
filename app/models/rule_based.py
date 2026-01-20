import math

def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))

def predict_home_win(features: dict) -> float:
    score = 0.0

    # Home advantage
    score += 2.0

    # Form & goals
    score += features.get("form_diff", 0) * 0.8
    score += features.get("goal_diff", 0) * 0.6

    # Missing players (optional)
    score -= features.get("missing_key_players", 0) * 1.2

    return sigmoid(score)
