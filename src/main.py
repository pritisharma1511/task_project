import streamlit as st
import time
from puzzle_generator import generate_puzzle
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

# Page Config
st.set_page_config(page_title="Math Adventures", page_icon="🧮")

# Title and Styles
st.title("🧮 Math Adventures")
st.markdown("""
<style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .stButton>button {
        width: 100%;
        height: 50px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if 'tracker' not in st.session_state:
    st.session_state.tracker = PerformanceTracker()
    st.session_state.adaptive_engine = AdaptiveEngine()
    st.session_state.current_difficulty = "Easy"
    st.session_state.user_name = None
    st.session_state.current_puzzle = None
    st.session_state.start_time = None
    st.session_state.feedback = None

def start_new_question():
    """Generates a new question and resets timer."""
    # Determine difficulty
    next_level = st.session_state.adaptive_engine.decide_difficulty(st.session_state.tracker)
    st.session_state.current_difficulty = next_level
    
    # Generate puzzle
    puzzle = generate_puzzle(st.session_state.current_difficulty)
    st.session_state.current_puzzle = puzzle
    st.session_state.start_time = time.time()
    st.session_state.feedback = None

# --- Login View ---
if not st.session_state.user_name:
    st.header("Welcome Learner!")
    name = st.text_input("Enter your name to start:")
    if st.button("Start Adventure"):
        if name:
            st.session_state.user_name = name
            start_new_question()
            st.rerun()
        else:
            st.warning("Please enter your name.")

# --- Main Game View ---
else:
    # Sidebar stats
    st.sidebar.header(f"Explorer: {st.session_state.user_name}")
    stats = st.session_state.tracker.get_stats()
    st.sidebar.metric("Questions Resolved", stats['total'])
    st.sidebar.metric("Accuracy", f"{stats['accuracy']*100:.1f}%")
    st.sidebar.metric("Current Level", st.session_state.current_difficulty)

    # Main Area
    st.subheader(f"Level: {st.session_state.current_difficulty}")
    
    if st.session_state.current_puzzle:
        puzzle = st.session_state.current_puzzle
        
        st.markdown(f"<p class='big-font'>Calculate: {puzzle['question']} = ?</p>", unsafe_allow_html=True)
        
        user_ans = st.number_input("Your Answer:", step=1, key="answer_input")
        
        if st.button("Submit Answer"):
            elapsed_time = time.time() - st.session_state.start_time
            correct = (user_ans == puzzle['answer'])
            
            # Log result
            st.session_state.tracker.log_attempt(
                difficulty=st.session_state.current_difficulty,
                correct=correct,
                time_taken=elapsed_time
            )
            
            # Feedback
            if correct:
                st.session_state.feedback = "✅ Correct! Great job!"
                st.balloons()
            else:
                st.session_state.feedback = f"❌ Oops! The correct answer was {puzzle['answer']}."
            
            # Wait a moment then load next
            st.info(st.session_state.feedback)
            time.sleep(1.5) # Pause to let user see feedback
            start_new_question()
            st.rerun()
            
    # Session Summary (Always visible at bottom)
    st.divider()
    with st.expander("Session Logs"):
        df = st.session_state.tracker.get_summary()
        if not df.empty:
            st.dataframe(df.sort_index(ascending=False))
