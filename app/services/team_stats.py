"""
Compute basic team statistics from historical fixtures.
"""
from app.db.mongo import get_collection
from datetime import datetime, timedelta


def compute_team_stats_from_fixtures(team_id: int, league_id: int = None, days_back: int = 90):
    """
    Compute simple stats for a team from recent fixtures.
    
    Returns:
        dict with keys: form, goals_for, goals_against, games_played
        Returns None if no fixtures found.
    """
    fixtures_col = get_collection("fixtures")
    
    # Look back N days
    cutoff_date = (datetime.now() - timedelta(days=days_back)).isoformat()
    
    query = {
        "$or": [
            {"teams.home.id": team_id},
            {"teams.away.id": team_id}
        ],
        "fixture.date": {"$gte": cutoff_date},
        "fixture.status.short": {"$in": ["FT", "AET", "PEN"]}  # Only finished matches
    }
    
    if league_id:
        query["league.id"] = league_id
    
    fixtures = list(fixtures_col.find(query).sort("fixture.date", -1).limit(10))
    
    if not fixtures:
        return None
    
    total_goals_for = 0
    total_goals_against = 0
    points = 0
    games = len(fixtures)
    
    for f in fixtures:
        is_home = f["teams"]["home"]["id"] == team_id
        
        goals_for = f["goals"]["home"] if is_home else f["goals"]["away"]
        goals_against = f["goals"]["away"] if is_home else f["goals"]["home"]
        
        total_goals_for += goals_for or 0
        total_goals_against += goals_against or 0
        
        # Points: 3 for win, 1 for draw, 0 for loss
        if goals_for > goals_against:
            points += 3
        elif goals_for == goals_against:
            points += 1
    
    # Form = average points per game (0-3 scale)
    form = points / games if games > 0 else 0
    
    return {
        "team_id": team_id,
        "form": round(form, 2),
        "goals_for": round(total_goals_for / games, 2) if games > 0 else 0,
        "goals_against": round(total_goals_against / games, 2) if games > 0 else 0,
        "games_played": games,
        "computed_at": datetime.now().isoformat()
    }
