from flask import Flask, request, jsonify
from flask_cors import CORS
from review_service import generate_review
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "reports"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return {"message": "CodeReviewAI Backend Running"}

@app.route("/review", methods=["POST"])
def review_code():
    if "file" not in request.files:
        return {"error": "No file uploaded"}, 400

    uploaded_file = request.files["file"]
    code = uploaded_file.read().decode("utf-8")

    result = generate_review(uploaded_file.filename, code)

    return jsonify(result)

@app.route("/reviews/<int:id>", methods=["GET"])
def get_review(id):
    from database import SessionLocal, ReviewReport
    db = SessionLocal()
    report = db.query(ReviewReport).filter_by(id=id).first()

    if not report:
        return {"error": "Not found"}, 404

    return {"id": report.id, "filename": report.filename, "report": report.report}

if __name__ == "__main__":
    app.run(port=5000, debug=True)
