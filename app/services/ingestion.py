from app.data_sources.api_football import get_fixtures
from app.db.mongo import get_collection

def ingest_fixtures(date: str):
    fixtures_col = get_collection("fixtures")
    fixtures = get_fixtures(date)

    for fixture in fixtures:
        fixtures_col.update_one(
            {"fixture_id": fixture["fixture"]["id"]},
            {"$set": fixture},
            upsert=True
        )
