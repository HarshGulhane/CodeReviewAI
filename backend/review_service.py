from llm_client import analyze_code_with_llm
from database import ReviewReport, SessionLocal

def generate_review(filename: str, code: str):
    review_text = analyze_code_with_llm(code)

    db = SessionLocal()
    entry = ReviewReport(filename=filename, report=review_text)
    db.add(entry)
    db.commit()
    db.refresh(entry)

    return {"id": entry.id, "filename": filename, "report": review_text}
