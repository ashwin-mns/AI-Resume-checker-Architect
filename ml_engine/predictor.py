import joblib
import os
import pandas as pd
import numpy as np

class ResumeMLPredictor:
    def __init__(self, model_path=None):
        self.model_path = model_path or os.path.join(os.path.dirname(__file__), "best_model.pkl")
        self.model = None
        self.load_model()
        
    def load_model(self):
        if os.path.exists(self.model_path):
            try:
                self.model = joblib.load(self.model_path)
            except Exception as e:
                print(f"Error loading model: {e}")
                self.model = None
        else:
            print(f"Model not found at {self.model_path}")
            self.model = None

    def predict_success(self, skills_score, project_score, experience_score, education_score, total_matched_skills):
        """
        Returns a hiring probability score (0-100).
        If model is missing, returns None.
        """
        if not self.model:
            return None
            
        # Create a DataFrame for prediction to match training features columns
        features = pd.DataFrame([{
            'skills_score': skills_score,
            'project_score': project_score,
            'experience_score': experience_score,
            'education_score': education_score,
            'total_matched_skills': total_matched_skills
        }])
        
        try:
            prediction = self.model.predict(features)[0]
            # Clip result between 0 and 100
            return int(min(100, max(0, prediction)))
        except Exception as e:
            print(f"Prediction error: {e}")
            return None
