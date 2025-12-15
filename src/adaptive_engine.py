class AdaptiveEngine:
    def __init__(self):
        self.levels = ["Easy", "Medium", "Hard"]
        
    def decide_difficulty(self, tracker):
        """
        Decides the next difficulty based on recent performance.
        
        Args:
            tracker (PerformanceTracker): The user's tracker instance.
            
        Returns:
            str: Next difficulty level ("Easy", "Medium", "Hard")
        """
        history = tracker.history
        
        # If no history or very few questions, stick to current or default (handled by caller usually, but let's default to Easy if empty)
        if not history:
            return "Easy"
            
        # Look at the last N attempts to determine momentum
        window_size = 3
        if len(history) < window_size:
            # Not enough data to switch yet, return the last difficulty
            return history[-1]['difficulty']
            
        recent = history[-window_size:]
        
        # Calculate recent accuracy
        correct_count = sum(1 for h in recent if h['correct'])
        accuracy = correct_count / window_size
        
        current_difficulty = recent[-1]['difficulty']
        current_idx = self.levels.index(current_difficulty)
        
        # Logic Rules:
        # 1. High Accuracy (>= 80%) -> Increase Difficulty
        # 2. Low Accuracy (< 50%) -> Decrease Difficulty
        # 3. Moderate -> Maintain
        
        next_difficulty = current_difficulty
        
        if accuracy >= 0.8:
            # Try to level up
            if current_idx < len(self.levels) - 1:
                next_difficulty = self.levels[current_idx + 1]
                
        elif accuracy < 0.5:
            # Level down
            if current_idx > 0:
                next_difficulty = self.levels[current_idx - 1]
                
        return next_difficulty

# Quick test if run directly
if __name__ == "__main__":
    pass
