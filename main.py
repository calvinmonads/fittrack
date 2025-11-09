from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Workout, SessionLocal, init_db
from pydantic import BaseModel
from typing import List

app = FastAPI(title="FitTrack API")

# Initialize the database when app starts
init_db()

# Dependency for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Pydantic model for data validation ---
class WorkoutCreate(BaseModel):
    muscle_group: str
    movement: str
    reps: int
    weight: float
    equipment: str
    notes: str | None = None

# --- ROUTES ---

@app.get("/")
def home():
    return {"message": "Welcome to FitTrack API"}

@app.post("/workouts/", response_model=dict)
def create_workout(workout: WorkoutCreate, db: Session = Depends(get_db)):
    new_workout = Workout(**workout.dict())
    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)
    return {"message": "Workout added successfully", "id": new_workout.id}

@app.get("/workouts/", response_model=List[dict])
def list_workouts(db: Session = Depends(get_db)):
    workouts = db.query(Workout).all()
    return [w.__dict__ for w in workouts]
