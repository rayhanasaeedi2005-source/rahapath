import streamlit as st

st.set_page_config(page_title="RahaPath - Empowering Education", page_icon="🎓", layout="centered")

st.title("🎓 RahaPath")
st.subheader("Empowering Afghan Students through AI & Education")
st.markdown("---")

menu = st.sidebar.selectbox(
    "📌 Select a Feature:",
    ["AI Study Assistant", "Scholarship Finder", "English Learning", "Study Planner", "Smart Problem Solver"]
)

if menu == "AI Study Assistant":
    st.header("🤖 AI Study Assistant")
    st.write("Ask about: **python, scholarship, study, english, motivation**")
    question = st.text_input("What do you want to learn about?")
    
    knowledge_base = {
        "python": "Python is a beginner-friendly programming language used in AI, web development, and data science. Start with variables, loops, and functions!",
        "scholarship": "To win a scholarship, focus on a high GPA, strong English (IELTS/Duolingo), a clear Motivation Letter, and recommendation letters.",
        "study": "Use the Pomodoro technique: study with full focus for 25 minutes, then take a 5-minute break. Repeat this 4 times!",
        "english": "Practice 10 new words daily, listen to English podcasts, and try speaking or writing short paragraphs every day.",
        "motivation": "Education is the most powerful weapon you can use to change your future. Every small step you take today builds your success tomorrow!"
    }
    
    if st.button("Ask AI"):
        found = False
        for topic in knowledge_base:
            if topic in question.lower():
                st.success(knowledge_base[topic])
                found = True
                break
        if not found:
            st.info("Try asking about: python, scholarship, study, english, or motivation.")

elif menu == "Scholarship Finder":
    st.header("🌍 Scholarship Finder")
    level = st.radio("Choose your study level:", ["Bachelor", "Master"])
    
    if level == "Bachelor":
        st.success("✅ **DAAD Scholarship** (Germany)")
        st.success("✅ **Turkiye Burslari** (Turkey)")
        st.success("✅ **University of the People** (Online - Tuition Free)")
    else:
        st.success("✅ **Chevening Scholarship** (UK)")
        st.success("✅ **Fulbright Program** (USA)")
        st.success("✅ **Erasmus Mundus** (Europe)")

elif menu == "English Learning":
    st.header("📚 English Vocabulary Quiz")
    st.write("What is the synonym of **'Resilient'**?")
    answer = st.radio("Choose the correct meaning:", ["Weak", "Strong", "Tired"])
    
    if st.button("Check Answer"):
        if answer == "Strong":
            st.success("🎉 Correct! 'Resilient' means strong and able to recover quickly.")
        else:
            st.error("❌ Not quite! The correct answer is 'Strong'.")

elif menu == "Study Planner":
    st.header("📅 Daily Study Planner")
    if "tasks" not in st.session_state:
        st.session_state.tasks = []
        
    new_task = st.text_input("Add a new study task (e.g., Read Chapter 2):")
    if st.button("Add Task") and new_task:
        st.session_state.tasks.append(new_task)
        st.success("Task added!")
        
    st.subheader("Your Tasks:")
    for t in st.session_state.tasks:
        st.write(f"- 📌 {t}")

elif menu == "Smart Problem Solver":
    st.header("🧮 Smart Problem Solver")
    tool = st.selectbox("Choose a tool:", ["Grade Percentage Calculator", "Quick Math Calculator"])
    
    if tool == "Grade Percentage Calculator":
        scores_input = st.text_input("Enter your scores separated by commas (e.g., 85, 90, 95):")
        if st.button("Calculate Percentage") and scores_input:
            scores = [float(x.strip()) for x in scores_input.split(",")]
            avg = sum(scores) / len(scores)
            st.metric("Average Percentage", f"{avg:.2f}%")
            if avg >= 55:
                st.success("Status: Passed! Great job!")
            else:
                st.warning("Status: Needs more study. Keep trying!")
                
    elif tool == "Quick Math Calculator":
        num1 = st.number_input("First number:", value=0.0)
        op = st.selectbox("Operation:", ["+", "-", "*", "/"])
        num2 = st.number_input("Second number:", value=0.0)
        if st.button("Solve"):
            if op == "+":
                st.success(f"Result: {num1 + num2}")
            elif op == "-":
                st.success(f"Result: {num1 - num2}")
            elif op == "*":
                st.success(f"Result: {num1 * num2}")
            elif op == "/" and num2 != 0:
                st.success(f"Result: {num1 / num2}")
            else:
                st.error("Cannot divide by zero!")
