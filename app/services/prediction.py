from app.models.rule_based import predict_home_win
from app.features.team_features import extract_team_features
from datetime import date
from app.db.mongo import get_collection

def predict_match(home_stats, away_stats):
    features = extract_team_features(home_stats, away_stats)
    probability = predict_home_win(features)

    return {
        "home_win_probability": round(probability, 3),
        "confidence": "HIGH" if probability >= 0.8 else "MEDIUM"
    }


def predict_today():
    fixtures_col = get_collection("fixtures")
    today = date.today().isoformat()

    fixtures = fixtures_col.find({
        "fixture.date": {"$regex": f"^{today}"}
    })

    predictions = []

    for f in fixtures:
        home = f["teams"]["home"]
        away = f["teams"]["away"]

        # MVP dummy stats (we’ll replace this soon)
        home_stats = {
            "form": 3,
            "goals_for": 2,
            "goals_against": 1
        }
        away_stats = {
            "form": 1,
            "goals_for": 1,
            "goals_against": 2
        }

        probability = predict_home_win({
            "form_diff": home_stats["form"] - away_stats["form"],
            "goal_diff": (
                home_stats["goals_for"] - home_stats["goals_against"]
            ) - (
                away_stats["goals_for"] - away_stats["goals_against"]
            )
        })

        predictions.append({
            "fixture_id": f["fixture"]["id"],
            "match": f"{home['name']} vs {away['name']}",
            "home_win_probability": round(probability, 3)
        })

    return predictions
