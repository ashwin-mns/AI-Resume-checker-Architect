# 🚀 AI Resume Architect

**Autonomous Multi-Agent System for Resume Optimization & Interview Prep**

A powerful AI-driven application that uses a team of autonomous agents to analyze, score, and rewrite your resume for specific job roles. Built with a premium **Glassmorphism React UI** and a robust **Flask Multi-Agent Backend**.

---

## 🌟 Key Features

### 🤖 Multi-Agent Architecture
The system orchestrates **Smart AI Agents & ML Models** to process your data:
1.  **🕵️ Skill Extractor Agent**: Parses your PDF to extract technical and soft skills, experience, and projects.
2.  **🎯 ATS Matcher Agent**: Compares your resume against the target role (e.g., "Software Engineer") to calculate a match score and identify missing keywords.
3.  **✍️ Resume Writer Agent**: Automatically rewrites your resume content to include missing skills and optimize for Applicant Tracking Systems (ATS).
4.  **🎤 Interview Coach Agent**: Generates tailored technical and behavioral interview questions based on your specific profile.
5.  **🔮 Hiring Probability Predictor**: Uses trained ML models (Random Forest) to predict your likelihood of getting hired.

### 🎨 Premium User Experience
*   **Glassmorphism UI**: Modern, transparent design with interactive elements.
*   **Visual Feedback**: Color-coded skill pills (✅ Match / ❌ Missing) and animated score indicators.
*   **Instant PDF Generation**: Download your significantly improved resume with one click.
*   **Fallback 'Demo Mode'**: Even without an API key, the system provides high-quality mock optimizations for demonstration.

---

## 🛠️ Tech Stack

### Frontend (User Interface)
*   **React.js**: Component-based UI library.
*   **CSS3**: Custom variables, gradients, `backdrop-filter` for glass effect.
*   **Axios**: For API communication.

### Backend (Core Logic)
*   **Python + Flask**: RESTful API server.
*   **OpenAI API (GPT-4o)**: Powers the intelligence of the agents.
*   **Scikit-learn & Pandas**: Powers the ML prediction engine.
*   **PDFPlumber**: For accurate text extraction from uploaded PDFs.
*   **FPDF**: For generating professional, clean PDF outputs.

---

## 🚀 Installation & Setup

### Prerequisites
*   **Python 3.8+**
*   **Node.js & npm**

### 1️⃣ Backend Setup (Flask)
Navigate to the backend directory and install dependencies:

```bash
cd resume_agent
pip install -r requirements.txt
```

Start the Flask server:
```bash
python app.py
```
*✅ Server will run at `http://127.0.0.1:5000`*

### 2️⃣ Frontend Setup (React)
Open a new terminal, navigate to the frontend directory, and install dependencies:

```bash
cd resume-agent-ui
npm install
```

Start the React Development Server:
```bash
npm start
```
*✅ Dashboard will launch at `http://localhost:3000`*

---

## 📂 Project Structure

```bash
resume-agent/
│
├── 📁 resume-agent-ui/       # ⚛️ React Frontend
│   ├── src/
│   │   ├── App.js            # Dashboard Component
│   │   └── App.css           # Glassmorphism Styling
│   └── package.json
│
├── 📁 resume_agent/          # 🐍 Flask Backend
│   ├── 📁 agents/            # 🤖 AI Agent Modules
│   │   ├── skill_agent.py
│   │   ├── ats_agent.py
│   │   ├── writer_agent.py
│   │   └── interview_agent.py
│   ├── 📁 ml_engine/         # 🧠 Machine Learning Engine
│   │   ├── model_factory.py
│   │   ├── predictor.py
│   │   ├── data_generator.py
│   │   └── best_model.pkl
│   ├── app.py                # API Gateway & Orchestrator
│   ├── pdf_parser.py         # PDF Extraction Logic
│   ├── pdf_generator.py      # PDF Creation Logic
│   └── uploads/              # Storage for Generated PDFs
│
└── README.md                 # Project Documentation
```

## 🔑 AI Configuration (Optional)
To enable the **Real AI Capabilities** (instead of the Demo Mode):
1.  Create a `.env` file in the `resume_agent/` folder.
2.  Add your OpenAI API Key:
    ```env
    OPENAI_API_KEY=sk-your-api-key-here
    ```

---

## 📸 Usage
1.  Open the web dashboard.
2.  **Upload** your current Resume (PDF).
3.  **Select** your target job role (e.g., "Cybersecurity Analyst").
4.  Click **"Analyze Resume ⚡"**.
5.  View your **ATS Score**, **Missing Skills**, and **Interview Questions**.
6.  **Download** your new optimized resume!

---
<img width="1919" height="857" alt="Screenshot 2026-01-28 231451" src="https://github.com/user-attachments/assets/5686a42e-55fd-4c73-84f0-32281710087b" />

<img width="1917" height="859" alt="Screenshot 2026-01-28 231549" src="https://github.com/user-attachments/assets/52ffafd9-2ee1-4d4d-b7fe-06b8be096a7b" />

<img width="1894" height="852" alt="Screenshot 2026-01-28 231644" src="https://github.com/user-attachments/assets/20afc1fd-0fc4-4c09-9230-e3edfd11d1d5" />

<img width="1902" height="857" alt="Screenshot 2026-01-28 231700" src="https://github.com/user-attachments/assets/8f9e89cd-d55f-4511-a75c-0823546ce826" />
