import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [role, setRole] = useState("Cybersecurity Analyst");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  // Handle Upload
  const handleUpload = async () => {
    if (!file) {
      alert("Please upload a resume PDF!");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);
    formData.append("role", role);

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/multi_agent",
        formData
      );

      setResult(response.data);
    } catch (error) {
      console.log(error);
      const msg = error.response?.data?.error || error.message || "Error uploading resume!";
      alert("Error: " + msg);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>✨ AI Resume Architect</h1>

      {/* Upload Section */}
      <div className="glass-card">
        <h2 style={{ marginTop: 0 }}>🚀 Optimization Control</h2>

        <div className="input-group">
          <label>Upload Resume (PDF)</label>
          <input
            type="file"
            accept=".pdf"
            className="glass-input"
            onChange={(e) => setFile(e.target.files[0])}
          />
        </div>

        <div className="input-group">
          <label>Target Role</label>
          <select
            className="glass-select"
            value={role}
            onChange={(e) => setRole(e.target.value)}
          >
            <option>Cybersecurity Analyst</option>
            <option>Software Engineer</option>
            <option>Data Analyst</option>
            <option>Machine Learning Engineer</option>
            <option>Product Manager</option>
            <option>DevOps Engineer</option>
          </select>
        </div>

        <button
          className="glass-btn"
          onClick={handleUpload}
          disabled={loading}
        >
          {loading ? "🤖 Analyzing & Optimizing..." : "Analyze Resume ⚡"}
        </button>
      </div>

      {/* Results Section */}
      {result && (
        <div className="glass-card fade-in">
          <div style={{ textAlign: 'center' }}>
            <div className="score-circle">
              {result.ats_score}
            </div>
            <h3>ATS Match Score</h3>
          </div>

          <div className="results-grid">
            <div>
              <h3>✅ Matched Skills</h3>
              <div className="pill-container">
                {result.matched_skills.map((skill, i) => (
                  <span key={i} className="skill-pill match">{skill}</span>
                ))}
              </div>
            </div>

            <div>
              <h3>❌ Missing Skills</h3>
              <div className="pill-container">
                {result.missing_skills.map((skill, i) => (
                  <span key={i} className="skill-pill missing">{skill}</span>
                ))}
              </div>
            </div>
          </div>

          <div style={{ marginTop: '30px' }}>
            <h3>📄 Improved Resume</h3>
            <a
              href={"http://127.0.0.1:5000" + result.improved_resume_download}
              target="_blank"
              rel="noreferrer"
              className="download-link"
            >
              📥 Download Optimized PDF
            </a>
          </div>

          <div style={{ marginTop: '30px' }}>
            <h3>🎯 AI Interview Prep</h3>
            <div className="interview-box">
              {result.interview_questions}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
