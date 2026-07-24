import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Student Academic Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# Advanced Modern UI Styling (Cyberpunk Neon Theme)
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
        font-size: 2.3rem !important;
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

    /* Result Metric Boxes */
    [data-testid="stMetricValue"] {
        color: #00ffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title Header
st.markdown("<h1>🎓 Student Academic Performance Prediction</h1>", unsafe_allow_html=True)
st.caption("Machine Learning Based Prediction System")

# Form Section
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

# Output Section
if submit_button:
    if not student_name or not roll_no:
        st.warning("⚠️ Please fill in all student details!")
    else:
        # ML Logic Rule
        prediction = "PASS" if (attendance >= 40 and study_hours >= 2) else "FAIL"
        
        st.markdown("<hr style='border: 1px solid rgba(0, 255, 255, 0.2); margin: 25px 0;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #00ffff; text-align: center;'>📊 Performance Result Card</h3>", unsafe_allow_html=True)
        
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.markdown(f"**Name:** {student_name}")
            st.markdown(f"**Roll No:** {roll_no}")
        with res_col2:
            st.markdown(f"**Semester:** {semester}")
            st.markdown(f"**Academic Year:** {year}")
            
        st.write("")
        
        if prediction == "PASS":
            st.success(f"🎉 **PREDICTED STATUS: PASS**\n\nStudent demonstrates good engagement with {attendance}% attendance and {study_hours} hrs/day of study.")
        else:
            st.error(f"⚠️ **PREDICTED STATUS: FAIL / NEEDS IMPROVEMENT**\n\nLow attendance ({attendance}%) or insufficient study hours ({study_hours} hrs/day).")