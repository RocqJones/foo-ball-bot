from fastapi import FastAPI
from app.services.prediction import predict_today
from app.services.ranking import rank_predictions

app = FastAPI(title="Foo Ball Bot")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/predictions/today")
def get_predictions_today():
    predictions = predict_today()
    ranked = rank_predictions(predictions)
    return {
        "count": len(ranked),
        "predictions": ranked
    }
