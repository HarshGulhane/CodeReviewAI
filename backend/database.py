from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class ReviewReport(Base):
    __tablename__ = "review_reports"
    id = Column(Integer, primary_key=True)
    filename = Column(Text)
    report = Column(Text)

engine = create_engine("sqlite:///reviews.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
