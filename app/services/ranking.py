def rank_predictions(predictions, limit=10):
    sorted_preds = sorted(
        predictions,
        key=lambda x: x["home_win_probability"],
        reverse=True
    )
    return sorted_preds[:limit]
