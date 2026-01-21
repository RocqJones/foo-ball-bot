def rank_predictions(predictions, limit=10):
    # Rank by home_win_probability + value_score
    # Handle None value_score by defaulting to 0
    sorted_preds = sorted(
        predictions,
        key=lambda x: (x["home_win_probability"] + (x.get("value_score") or 0)),
        reverse=True
    )
    return sorted_preds[:limit]
