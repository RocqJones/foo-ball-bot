def extract_team_features(home_stats, away_stats):
    return {
        "form_diff": home_stats["form"] - away_stats["form"],
        "goal_diff": (
            home_stats["goals_for"] - home_stats["goals_against"]
        ) - (
            away_stats["goals_for"] - away_stats["goals_against"]
        )
    }
