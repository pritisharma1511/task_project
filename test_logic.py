from src.tracker import PerformanceTracker
from src.adaptive_engine import AdaptiveEngine

def test_adaptive_logic():
    print("Starting Adaptive Logic Test...")
    tracker = PerformanceTracker()
    engine = AdaptiveEngine()
    
    # helper
    def log(correct):
        tracker.log_attempt("Easy" if not tracker.history else tracker.history[-1]['difficulty'], correct, 5.0)
    
    # 1. Start at Easy
    diff = engine.decide_difficulty(tracker)
    print(f"Initial: {diff}")
    assert diff == "Easy"
    
    # 2. Get 3 right -> Should move to Medium (Engine logic: last 3 attempts, >= 80% acc)
    print("User gets 3 Correct...")
    tracker.log_attempt("Easy", True, 5.0)
    tracker.log_attempt("Easy", True, 5.0)
    tracker.log_attempt("Easy", True, 5.0)
    
    diff = engine.decide_difficulty(tracker)
    print(f"After 3 Correct: {diff}")
    assert diff == "Medium", f"Expected Medium from Easy after 3 wins, got {diff}"

    # 3. Fail 3 times -> Should move back to Easy
    print("User fails 3 times at Medium...")
    tracker.log_attempt("Medium", False, 5.0)
    tracker.log_attempt("Medium", False, 5.0)
    tracker.log_attempt("Medium", False, 5.0)
    
    diff = engine.decide_difficulty(tracker)
    print(f"After 3 Fails: {diff}")
    assert diff == "Easy", f"Expected Easy from Medium after 3 fails, got {diff}"

    print("✅ Logic Test Passed!")

if __name__ == "__main__":
    test_adaptive_logic()
