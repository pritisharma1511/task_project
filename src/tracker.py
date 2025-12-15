import time
import pandas as pd

class PerformanceTracker:
    def __init__(self):
        self.history = []
        
    def log_attempt(self, difficulty, correct, time_taken):
        """
        Logs a single puzzle attempt.
        """
        self.history.append({
            "timestamp": time.time(),
            "difficulty": difficulty,
            "correct": correct,
            "time_taken": time_taken
        })
        
    def get_summary(self):
        """
        Returns a DataFrame summary of performance.
        """
        if not self.history:
            return pd.DataFrame()
        return pd.DataFrame(self.history)
    
    def get_stats(self):
        """
        Returns aggregate stats: total attempts, accuracy, avg time.
        """
        if not self.history:
            return {"total": 0, "accuracy": 0, "avg_time": 0}
            
        df = pd.DataFrame(self.history)
        total = len(df)
        accuracy = df["correct"].mean()
        avg_time = df["time_taken"].mean()
        
        return {
            "total": total,
            "accuracy": accuracy,
            "avg_time": avg_time
        }
