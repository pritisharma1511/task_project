# Technical Note: Math Adventures Adaptive System

## Architecture
The system follows a simple modular architecture:

1.  **Frontend (Streamlit)**: Handles user interaction, state management (Session State), and visual feedback.
2.  **Core Logic Modules**:
    *   `Puzzle Generator`: Stateless factory for creating math problems.
    *   `Performance Tracker`: Stateful logger that records timestamp, correctness, and difficulty for each attempt.
    *   `Adaptive Engine`: Pure logic component that analyzes tracker history to recommend the next state.

### Flow Diagram
```mermaid
graph TD
    A[Start Session] --> B[Generate Puzzle (Current Difficulty)]
    B --> C[User Input]
    C --> D{Check Answer}
    D --> E[Log Result (Tracker)]
    E --> F[Adaptive Engine Analysis]
    F --> G{Performance Check}
    G -- High Accuracy --> H[Increase Difficulty]
    G -- Low Accuracy --> I[Decrease Difficulty]
    G -- Stable --> J[Maintain Difficulty]
    H & I & J --> B
```

## Adaptive Logic Implementation
The current iteration uses a **Rule-Based Heuristic approach** rather than a trained ML model. This decision was made for the following reasons:
1.  **Determinism**: For a simple prototype, predictable behavior is easier to debug and demonstrate.
2.  **Cold Start**: ML models require training data. A rule-based system works immediately for the first user.
3.  **Simplicity**: The logic fits within a compact window-based algorithm without external heavy libraries (like PyTorch/TensorFlow).

### Logic Rules
The engine looks at a **rolling window of the last 3 attempts**:
*   **Upgrade Condition**: Accuracy ≥ 80%. This ensures the user has mastered the current level before moving up.
*   **Downgrade Condition**: Accuracy < 50%. This prevents frustration by quickly lowering the bar when the user fails.
*   **Maintain Condition**: 50-79% Accuracy. This represents the "Zone of Proximal Development" where learning happens.

## Key Metrics
*   **Correctness**: The primary driver for adaptation.
*   **Time Taken**: Logged but currently secondary in the decision logic (future improvements could use low time + high accuracy as a "Mastery" signal).

## Future Improvements
*   **Reinforcement Learning**: Implement a Q-learning agent where "State" is the current difficulty/streak, "Action" is the difficulty adjustment, and "Reward" is user engagement/success.
*   **Content granularity**: Break "Medium" into smaller sub-skills (e.g., "Multiplication only").
