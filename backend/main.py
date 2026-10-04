from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(title="Framework-Free Responsive Site API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class DataItem(BaseModel):
    id: int
    title: str
    status: str
    score: float
    timestamp: str

class ContactForm(BaseModel):
    name: str
    email: str
    message: str

# In-memory seed data
data_store = [
    {"id": 1, "title": "Project Alpha", "status": "active", "score": 95.5, "timestamp": datetime.now().isoformat()},
    {"id": 2, "title": "Project Beta", "status": "pending", "score": 82.0, "timestamp": datetime.now().isoformat()}
]

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/api/analytics", response_model=List[DataItem])
def get_analytics():
    return data_store

@app.post("/api/contact")
def submit_contact(form: ContactForm):
    # Logic for processing form would go here
    return {"message": "Form submitted successfully", "received": form.email}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)