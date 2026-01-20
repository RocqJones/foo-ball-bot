from datetime import date
from app.services.ingestion import ingest_fixtures

def run():
    today = date.today().isoformat()
    ingest_fixtures(today)
    print("Daily ingestion complete")

if __name__ == "__main__":
    run()
