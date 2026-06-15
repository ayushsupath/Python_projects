import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Grade Calculator",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.header {
    background: linear-gradient(90deg, #4F46E5, #7C3AED);
    padding: 25px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.grade-box {
    text-align:center;
    padding:20px;
    border-radius:15px;
    font-size:28px;
    font-weight:bold;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
    <h1>🎓 Student Grade Calculator</h1>
    <p>Calculate Percentage, Grade & Performance Report</p>
</div>
""", unsafe_allow_html=True)

# ---------------- STUDENT INFO ----------------
st.markdown("### 👨‍🎓 Student Details")

col1, col2 = st.columns(2)

with col1:
    student_name = st.text_input("Student Name")

with col2:
    roll_no = st.text_input("Roll Number")

# ---------------- MARKS SECTION ----------------
st.markdown("### 📝 Enter Subject Marks")

subjects = [
    "Mathematics",
    "Science",
    "English",
    "Computer",
    "Social Studies"
]

marks = []

cols = st.columns(5)

for i, subject in enumerate(subjects):
    with cols[i]:
        mark = st.number_input(
            subject,
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )
        marks.append(mark)

# ---------------- CALCULATE BUTTON ----------------
if st.button("🚀 Calculate Result", use_container_width=True):

    total = sum(marks)
    percentage = total / 5

    # Grade Logic
    if percentage >= 90:
        grade = "A"
        color = "#16A34A"
        remarks = "Outstanding Performance 🌟"
    elif percentage >= 80:
        grade = "B"
        color = "#2563EB"
        remarks = "Very Good Performance 👍"
    elif percentage >= 70:
        grade = "C"
        color = "#F59E0B"
        remarks = "Good Performance 😊"
    elif percentage >= 60:
        grade = "D"
        color = "#EA580C"
        remarks = "Needs Improvement 📚"
    else:
        grade = "F"
        color = "#DC2626"
        remarks = "Failed - Keep Trying 💪"

    st.divider()

    # ---------------- METRICS ----------------
    st.markdown("## 📊 Result Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Marks", f"{total}/500")
    c2.metric("Percentage", f"{percentage:.2f}%")
    c3.metric("Grade", grade)

    # ---------------- PROGRESS BAR ----------------
    st.markdown("### 🎯 Percentage Score")
    st.progress(int(percentage))

    # ---------------- GRADE CARD ----------------
    st.markdown(
        f"""
        <div class="grade-box" style="background:{color}">
            Grade : {grade}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"### 💬 Remarks: {remarks}")

    # ---------------- PASS/FAIL ----------------
    if percentage >= 60:
        st.success("✅ Congratulations! You Passed.")
        st.balloons()
    else:
        st.error("❌ You Failed. Better Luck Next Time.")

    # ---------------- CHART ----------------
    st.markdown("## 📈 Subject-wise Performance")

    df = pd.DataFrame({
        "Subject": subjects,
        "Marks": marks
    })

    st.bar_chart(df.set_index("Subject"))

    # ---------------- REPORT CARD ----------------
    st.markdown("## 📄 Report Card")

    report = df.copy()
    report.loc[len(report.index)] = ["Total", total]

    st.dataframe(
        report,
        use_container_width=True,
        hide_index=True
    )

    # ---------------- STUDENT SUMMARY ----------------
    st.markdown("## 🏆 Student Summary")

    st.info(
        f"""
        Name: **{student_name if student_name else 'N/A'}**

        Roll Number: **{roll_no if roll_no else 'N/A'}**

        Percentage: **{percentage:.2f}%**

        Grade: **{grade}**
        """
    )

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")