import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Student Academic Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# 2. Advanced Modern UI Styling (Cyberpunk Neon Theme)
st.markdown("""
    <style>
    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #0f0c20, #15102a, #06101e, #12002b) !important;
        background-size: 400% 400% !important;
        animation: gradientBG 12s ease infinite !important;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Main Title Styling */
    h1 {
        background: linear-gradient(90deg, #00ffff, #8a2be2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 800 !important;
        font-size: 2.2rem !important;
        margin-bottom: 0px !important;
    }

    /* Subtitle Styling */
    .stCaption {
        text-align: center !important;
        color: #a0a0c0 !important;
        font-size: 1rem !important;
        margin-bottom: 25px !important;
    }

    /* Form Glassmorphism Card with Neon Glow */
    [data-testid="stForm"] {
        background: rgba(22, 22, 35, 0.75) !important;
        border: 1px solid rgba(0, 255, 255, 0.3) !important;
        border-radius: 20px !important;
        padding: 30px !important;
        box-shadow: 0 0 25px rgba(0, 255, 255, 0.15) !important;
    }

    /* Input Fields Styling */
    .stTextInput input, .stNumberInput input, div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 12px !important;
        font-weight: 500 !important;
    }

    /* Glowing Submit Button */
    .stButton>button {
        width: 100% !important;
        background: linear-gradient(90deg, #00ffff, #00bfff) !important;
        color: #0a0a12 !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 12px !important;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.4) !important;
        transition: all 0.3s ease !important;
    }

    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 0 25px rgba(0, 255, 255, 0.8) !important;
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Title Header
st.markdown("<h1>🎓 Student Academic Performance Prediction</h1>", unsafe_allow_html=True)
st.caption("Machine Learning Based Prediction System")

# 4. Form Section
with st.form("student_form"):
    st.markdown("<h3 style='color: #00ffff;'>📋 Enter Student Details</h3>", unsafe_allow_html=True)
    
    student_name = st.text_input("👤 Student Name", placeholder="e.g. Mohd Meraj Ansari")
    roll_no = st.text_input("🪪 Roll No / Enrollment No", placeholder="e.g. 2404161037")
    
    col1, col2 = st.columns(2)
    with col1:
        semester = st.selectbox("📚 Select Semester", [1, 2, 3, 4, 5, 6, 7, 8])
    with col2:
        year = st.selectbox("📅 Select Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
        
    study_hours = st.number_input("📖 Study Hours (Per Day)", min_value=0.0, max_value=24.0, step=0.5, value=4.0)
    attendance = st.number_input("📈 Attendance (%)", min_value=0.0, max_value=100.0, step=1.0, value=75.0)
    
    submit_button = st.form_submit_button("🚀 Predict Performance")

# 5. Output Section - Glassmorphism Result Card
if submit_button:
    if not student_name or not roll_no:
        st.warning("⚠️ Please fill in all student details!")
    else:
        # Prediction Logic (Replace with machine learning model if applicable)
        prediction = "PASS" if (attendance >= 40 and study_hours >= 2) else "FAIL"
        
        # UI Attributes based on Prediction
        if prediction == "PASS":
            badge_bg = "rgba(0, 255, 136, 0.15)"
            badge_border = "#00ff88"
            status_color = "#00ff88"
            status_text = "PASSED / HIGH PERFORMANCE"
            icon = "🎉"
            shadow_color = "rgba(0, 255, 136, 0.3)"
            message = f"Excellent consistency! With <b>{attendance:.1f}%</b> attendance and <b>{study_hours:.1f} hours/day</b> of dedicated study, performance is well above standard thresholds."
        else:
            badge_bg = "rgba(255, 75, 75, 0.15)"
            badge_border = "#ff4b4b"
            status_color = "#ff4b4b"
            status_text = "NEEDS IMPROVEMENT / AT RISK"
            icon = "⚠️"
            shadow_color = "rgba(255, 75, 75, 0.3)"
            message = f"Warning! Attendance (<b>{attendance:.1f}%</b>) or daily study hours (<b>{study_hours:.1f} hrs/day</b>) fall below required targets."

        st.markdown("<hr style='border: 1px solid rgba(0, 255, 255, 0.2); margin: 25px 0;'>", unsafe_allow_html=True)
        
        # Clean Compact HTML Output
        card_html = f"""<div style="background: rgba(18, 18, 30, 0.95); border: 1px solid {badge_border}; border-radius: 20px; padding: 25px; box-shadow: 0 0 30px {shadow_color}; margin-top: 10px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <span style="font-size: 1.1rem; font-weight: bold; color: #00ffff;">📊 OFFICIAL PERFORMANCE CARD</span>
        <span style="background: {badge_bg}; color: {status_color}; border: 1px solid {badge_border}; padding: 6px 16px; border-radius: 50px; font-size: 0.85rem; font-weight: 800;">{icon} {status_text}</span>
    </div>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; background: rgba(255, 255, 255, 0.04); padding: 15px; border-radius: 12px; margin-bottom: 20px; border: 1px solid rgba(255, 255, 255, 0.08);">
        <div><span style="color: #8888a0; font-size: 0.8rem;">STUDENT NAME</span><br><b style="color: #ffffff; font-size: 1rem;">{student_name.upper()}</b></div>
        <div><span style="color: #8888a0; font-size: 0.8rem;">ROLL / ENROLLMENT NO</span><br><b style="color: #ffffff; font-size: 1rem;">{roll_no}</b></div>
        <div><span style="color: #8888a0; font-size: 0.8rem;">SEMESTER</span><br><b style="color: #ffffff; font-size: 1rem;">Semester {semester}</b></div>
        <div><span style="color: #8888a0; font-size: 0.8rem;">ACADEMIC YEAR</span><br><b style="color: #ffffff; font-size: 1rem;">{year}</b></div>
    </div>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; text-align: center; margin-bottom: 20px;">
        <div style="background: rgba(0, 255, 255, 0.05); padding: 12px; border-radius: 10px; border: 1px solid rgba(0, 255, 255, 0.2);">
            <div style="color: #00ffff; font-size: 1.4rem; font-weight: bold;">{attendance:.1f}%</div>
            <div style="color: #aaa; font-size: 0.75rem;">ATTENDANCE RECORD</div>
        </div>
        <div style="background: rgba(138, 43, 226, 0.05); padding: 12px; border-radius: 10px; border: 1px solid rgba(138, 43, 226, 0.2);">
            <div style="color: #c77dff; font-size: 1.4rem; font-weight: bold;">{study_hours:.1f} Hours</div>
            <div style="color: #aaa; font-size: 0.75rem;">DAILY STUDY TIME</div>
        </div>
    </div>
    <div style="background: {badge_bg}; border-left: 4px solid {badge_border}; padding: 12px 18px; border-radius: 8px; color: #e0e0e0; font-size: 0.9rem;">
        {message}
    </div>
</div>"""
        
        st.markdown(card_html, unsafe_allow_html=True)