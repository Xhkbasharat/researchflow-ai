
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="ResearchFlow AI",
    description="Multi-Agent Research and Reporting System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "ResearchFlow AI",
        "message": "Welcome to ResearchFlow AI API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    
