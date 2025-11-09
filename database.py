from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///fittrack.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    muscle_group = Column(String)
    movement = Column(String)
    reps = Column(Integer)
    weight = Column(Float)
    equipment = Column(String)
    notes = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)
