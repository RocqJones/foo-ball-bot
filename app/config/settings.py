from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    API_FOOTBALL_KEY = os.getenv("API_FOOTBALL_KEY")
    ODDS_API_KEY = os.getenv("ODDS_API_KEY")

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "foo_ball_bot")

    # Leagues to track - easily configurable
    TRACKED_LEAGUES = [
        'UEFA Champions League',
        'Premier League',
        'La Liga',
        'Serie A',
        'Bundesliga'
    ]

    # Default prediction limit (None = no limit)
    PREDICTION_LIMIT = 30

settings = Settings()
