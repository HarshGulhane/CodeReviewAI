**CodeReviewAI — Automated Code Review Assistant**

CodeReviewAI is an AI-powered system that automatically reviews uploaded source code using a Large Language Model (LLM).  
It analyzes readability, structure, modularity, potential bugs, and coding best practices — then generates a detailed improvement report.

Built using **Streamlit** and integrated with **Groq LLaMA 3**, CodeReviewAI provides instant and high-quality code analysis suitable for developers, students, and code reviewers.


---

**How It Works**
1. User uploads a source code file through the Streamlit interface.  
2. The application reads the file content.  
3. The content is sent to an LLM with a specific review prompt.  
4. LLM returns a detailed review covering:
   - Readability  
   - Modularity  
   - Potential bugs  
   - Best practice adherence  
   - Suggestions for improvement  
5. The review is displayed in the UI, and opt   ionally stored in a local SQLite database.

---

**Setup and Run**
1. Clone the repository
cd CodeReviewAI

2. Create and activate a virtual environment
python -m venv venv
venv/Scripts/activate      

3. Install required packages
pip install -r requirements.txt

4. Add your Groq API key
Create a .env file in the project root:
GROQ_API_KEY=your_groq_api_key_here

5. Run the Streamlit app
streamlit run app.py


---

**Features**
1. Automated Code Analysis
Reviews for readability, structure, and bugs.

2. LLM-Powered Insights
Uses Groq LLaMA 3 for fast, accurate suggestions.

3. Easy File Upload
Accepts .py, .java, .cpp, .js, and other plain text code files.

4. Detailed Improvement Report
Includes actionable suggestions and optional improved code samples.

5. Optional History Tracking
Store and retrieve previous code reviews using SQLite.

---

**Notes**
1. Requires an active Groq API Key.
2. Best suited for text-based code files (up to 200MB).
3. Internet connection needed for LLM processing.
4. Streamlit handles both UI and backend execution.

---

**Demo Video**
Watch the full working demo here:

👉 Google Drive Demo Video:
https://docs.google.com/videos/d/1mBNiDgbNL8fsP9lekQO8oFby0bE9ZYEdrGrELYqCCV4/edit?usp=sharing