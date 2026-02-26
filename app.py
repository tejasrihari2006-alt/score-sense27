import streamlit as st
import joblib
import numpy as np
import time

st.set_page_config(page_title="Score-Sense", layout="wide")


st.markdown("""
<style>

/* Animated Background */
.stApp {
    background: linear-gradient(-45deg, #ff6ec4, #7873f5, #42e695, #f9ca24);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

/* Remove white blocks */
.block-container {background: transparent !important;}
[data-testid="stVerticalBlock"] {background: transparent !important;}
[data-testid="stHorizontalBlock"] {background: transparent !important;}
[data-testid="column"] {background: transparent !important;}

/* Inputs */
.stNumberInput input {
    background: rgba(255,255,255,0.2) !important;
    color: white !important;
    border-radius: 10px !important;
}

/* Title */
.title {
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:white;
}

/* Glass Card */
.glass {
    background: rgba(255,255,255,0.15);
    padding:40px;
    border-radius:20px;
    backdrop-filter: blur(15px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.37);
}

/* Labels */
label {color:white !important; font-size:18px !important;}

/* Button */
.stButton>button {
    background: linear-gradient(45deg,#ff416c,#ff4b2b);
    color:white;
    font-size:20px;
    padding:12px 30px;
    border-radius:15px;
    border:none;
}

/* Gradient animation */
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

</style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("model.pkl")

# Title
st.markdown("<div class='title'>🎓Score-Sence</div>", unsafe_allow_html=True)
st.write("")

col1, col2 = st.columns(2)

# INPUT SECTION
with col1:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    sleep = st.number_input("😴 Sleep Hours", 0.0, 12.0, step=0.1)
    social = st.number_input("📱 Social Media Hours", 0.0, 12.0, step=0.1)
    study = st.number_input("📚 Study Hours", 0.0, 12.0, step=0.1)
    attendance = st.number_input("🏫 Attendance Percentage", 0.0, 100.0, step=1.0)

    st.markdown("</div>", unsafe_allow_html=True)

# PREDICTION SECTION
with col2:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.write("### 📊 Prediction Result")

    if st.button("🚀 Predict GPA"):

        data = np.array([[study, attendance, social, sleep]])

        with st.spinner("Analyzing Performance..."):
            time.sleep(2)
            result = model.predict(data)[0]

        # Performance Level
        if result >= 8:
            color = "🟢 Excellent"
        elif result >= 6:
            color = "🟡 Average"
        else:
            color = "🔴 Needs Improvement"

        st.success(f"🎯 Predicted GPA: {result:.2f}")
        st.write(f"Performance Level: {color}")

        # Progress Bar
        progress = st.progress(0)
        for i in range(int(result * 10)):
            time.sleep(0.02)
            progress.progress(i)

        # Balloons
        st.balloons()

        # 🎯 SMART SUGGESTIONS
        st.write("### 💡 Suggestions For You")

        if result >= 8:
            st.success("""
            ✅ Excellent Performance!
            • Keep maintaining your study routine  
            • Continue healthy sleep schedule  
            • Revise regularly  
            • Try advanced learning techniques  
            """)

        elif result >= 6:
            st.warning("""
            ⚡ You can improve more!
            • Increase daily study hours  
            • Reduce social media usage  
            • Focus on attendance  
            • Sleep at least 7 hours daily  
            """)

        else:
            st.error("""
            🚨 Immediate Improvement Needed!
            • Create a daily study timetable  
            • Limit phone usage  
            • Attend all classes  
            • Maintain proper sleep cycle  
            • Seek help from teachers  
            """)

    st.markdown("</div>", unsafe_allow_html=True)
