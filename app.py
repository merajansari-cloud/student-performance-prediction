import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Student Academic Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# Custom Styling (Dark Neon Touch)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #00ffff, #00bfff);
        color: #000;
        font-weight: bold;
        font-size: 18px;
        border-radius: 25px;
        border: none;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 Student Academic Performance Prediction")
st.caption("Machine Learning Based Prediction System")
st.markdown("---")

# Input Form
with st.form("student_form"):
    st.subheader("📋 Enter Student Details")
    
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

# Prediction Output
if submit_button:
    if not student_name or not roll_no:
        st.warning("⚠️ Please fill in all student details!")
    else:
        prediction = "PASS" if (attendance >= 40 and study_hours >= 2) else "FAIL"
        
        st.markdown("---")
        st.subheader("📊 Performance Result Card")
        
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.write(f"**Name:** {student_name}")
            st.write(f"**Roll No:** {roll_no}")
        with res_col2:
            st.write(f"**Semester:** {semester}")
            st.write(f"**Academic Year:** {year}")
            
        st.write("")
        if prediction == "PASS":
            st.success(f"🎉 **PREDICTED STATUS: PASS**\n\nStudent shows strong attendance ({attendance}%) and sufficient study hours ({study_hours} hrs/day).")
        else:
            st.error(f"⚠️ **PREDICTED STATUS: FAIL / NEEDS IMPROVEMENT**\n\nLow attendance ({attendance}%) or insufficient study hours ({study_hours} hrs/day).")