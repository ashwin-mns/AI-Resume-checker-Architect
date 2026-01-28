import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

class ModelFactory:
    def __init__(self, data_path=None, model_save_path=None):
        self.data_path = data_path or os.path.join(os.path.dirname(__file__), "resume_dataset.csv")
        self.model_save_path = model_save_path or os.path.join(os.path.dirname(__file__), "best_model.pkl")
        
    def load_data(self):
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Data file not found at {self.data_path}. Please run data_generator.py first.")
        
        df = pd.read_csv(self.data_path)
        X = df[['skills_score', 'project_score', 'experience_score', 'education_score', 'total_matched_skills']]
        y = df['hiring_probability']
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_and_select_best(self):
        X_train, X_test, y_train, y_test = self.load_data()
        
        models = {
            "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
            "DecisionTree": DecisionTreeRegressor(random_state=42),
            "KNN": KNeighborsRegressor(n_neighbors=5)
        }
        
        results = {}
        best_model = None
        best_score = -np.inf
        best_name = ""
        
        print(f"{'Model':<15} | {'MSE':<10} | {'R2 Score':<10}")
        print("-" * 40)
        
        for name, model in models.items():
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            
            mse = mean_squared_error(y_test, predictions)
            r2 = r2_score(y_test, predictions)
            
            results[name] = {"MSE": mse, "R2": r2}
            
            print(f"{name:<15} | {mse:<10.4f} | {r2:<10.4f}")
            
            # Select based on R2 score (higher is better)
            if r2 > best_score:
                best_score = r2
                best_model = model
                best_name = name
                
        print("-" * 40)
        print(f"Best Model Selected: {best_name} (R2: {best_score:.4f})")
        
        # Save the best model
        joblib.dump(best_model, self.model_save_path)
        print(f"Model saved to {self.model_save_path}")
        
        return best_name, best_score

if __name__ == "__main__":
    # Ensure data exists before training
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "resume_dataset.csv")):
        from data_generator import generate_data
        print("Generating synthetic data...")
        target_path = os.path.join(os.path.dirname(__file__), "resume_dataset.csv")
        generate_data(output_path=target_path)
        
    factory = ModelFactory()
    factory.train_and_select_best()
