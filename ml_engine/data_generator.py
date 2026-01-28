import pandas as pd
import numpy as np
import random
import os

def generate_data(num_samples=1200, output_path="resume_dataset.csv"):
    """
    Generates a synthetic dataset for resume success prediction.
    Features:
    - skills_score (0-100)
    - project_score (0-100)
    - experience_score (0-100)
    - education_score (0-100)
    - total_matched_skills (0-20)
    
    Target:
    - hiring_probability (0-100)
    """
    
    data = []
    
    for _ in range(num_samples):
        # Generate realistic correlated features
        # Better candidates tend to score high across multiple categories
        
        base_quality = random.random() # 0 to 1, represents inherent candidate quality
        
        # Skills: correlated with quality but with some noise
        skills_score = int(min(100, max(0, base_quality * 90 + np.random.normal(5, 10))))
        
        # Projects: correlated with skills usually
        project_score = int(min(100, max(0, skills_score * 0.8 + np.random.normal(10, 15))))
        
        # Experience: slightly independent, grows with quality
        experience_score = int(min(100, max(0, base_quality * 85 + np.random.normal(10, 15))))
        
        # Education: often stable but varies
        education_score = int(min(100, max(0, base_quality * 80 + np.random.normal(15, 10))))
        
        # Matched skills count (raw number)
        total_matched_skills = int(min(20, max(0, (skills_score / 100) * 15 + np.random.normal(2, 3))))
        
        # Calculate Target: Hiring Probability
        # Weighted formula with some noise to simulate human bias/randomness
        # Weights: Skills (30%), Experience (30%), Projects (25%), Education (15%)
        raw_prob = (
            (skills_score * 0.30) + 
            (experience_score * 0.30) + 
            (project_score * 0.25) + 
            (education_score * 0.15)
        )
        
        # Add non-linearity: very high scores get a boost, very low get a penalty
        if raw_prob > 80:
            raw_prob += 5
        elif raw_prob < 40:
            raw_prob -= 5
            
        hiring_probability = int(min(100, max(0, raw_prob + np.random.normal(0, 5))))
        
        data.append({
            "skills_score": skills_score,
            "project_score": project_score,
            "experience_score": experience_score,
            "education_score": education_score,
            "total_matched_skills": total_matched_skills,
            "hiring_probability": hiring_probability
        })
        
    df = pd.DataFrame(data)
    
    # Save to CSV
    # Ensure directory exists
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Generated {num_samples} records and saved to {output_path}")
    return output_path

if __name__ == "__main__":
    generate_data(output_path=os.path.join(os.path.dirname(__file__), "resume_dataset.csv"))
