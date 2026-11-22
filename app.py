import streamlit as st

st.set_page_config(page_title="RahaPath - Empowering Education", page_icon="🎓", layout="centered")

st.title("🎓 RahaPath")
st.markdown("**Empowering Afghan Students through AI & Education** | *مسیر رهایی و پیشرفت آموزشی*")
st.markdown("---")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🤖 AI Assistant",
    "🌍 Scholarships",
    "📚 English",
    "📅 Planner",
    "🧮 Solver"
])

with tab1:
    st.header("🤖 AI Study Assistant")
    st.write("Ask about: **python, coding, scholarship, study, english, motivation, cv, university**")
    question = st.text_input("What do you want to learn about? (سوال خود را بنویسید)")

    knowledge_base = {
        "python": """**🐍 Complete Guide to Learning Python:**
Python is one of the easiest and most powerful programming languages in the world, used in Artificial Intelligence, Web Development, and Data Science.
- **Step 1 (Basics):** Master variables, data types, if/else conditions, and for/while loops.
- **Step 2 (Data Structures):** Learn how to organize information using Lists and Dictionaries.
- **Step 3 (Build Real Projects):** Just like you are doing right now with RahaPath, building small apps is the fastest way to become a real developer. Practice at least 1 hour every day!""",

        "coding": """**💻 Why & How to Start Coding:**
Coding is the superpower of the 21st century because it allows you to build global solutions using just a phone or a laptop, from anywhere in the world.
- **Best Path for Beginners:** Start with Python for logic and AI, then explore HTML/CSS for web design.
- **Golden Rule:** Don't worry about memorizing everything. Focus on understanding how problems are broken down into small steps, and practice consistently.""",

        "scholarship": """**🎓 Step-by-Step Guide to Winning International Scholarships:**
1. **Academic Excellence:** Keep your school or university grades (GPA) as high as possible (aim for above 80%).
2. **English Proficiency:** Start preparing for the Duolingo English Test (DET)—it is affordable, taken online from home, and accepted by thousands of universities worldwide.
3. **Motivation Letter (SOP):** Write a sincere story about your background, your resilience, why you chose your field, and how you will help your community after graduating.
4. **Recommendation Letters:** Ask 2 teachers or professors who know your hard work well to write strong letters for you.""",

        "study": """**📖 Scientific Study Techniques for Deep Focus:**
- **The Pomodoro Technique:** Study with 100% focus for 25 minutes (put your phone on silent), then take a 5-minute break to stretch or drink water. After 4 cycles, take a longer 20-minute break.
- **Active Recall:** Instead of just re-reading your notes, close the book and write down or explain out loud everything you remember.
- **Spaced Repetition:** Review new lessons after 1 day, 3 days, 7 days, and 21 days so the information stays in your long-term memory forever.""",

        "english": """**🗣️ Master English Fluently from Home:**
1. **Daily Vocabulary (10 Words):** Learn 10 new words every day inside real sentences, not alone.
2. **Listening & Shadowing:** Listen to English podcasts (like BBC 6 Minute English) or YouTube lessons for 15 minutes daily and repeat sentences out loud to improve your accent.
3. **Writing & Speaking:** Keep a daily English journal—write 5 sentences every night about what you learned today. Consistency beats intensity!""",

        "motivation": """**✨ A Message for Every Determined Student:**
Education is the most powerful tool that no one can ever take away from your mind. Even when doors seem closed, technology and self-learning open windows to the entire world. Every line of code you write, every English word you memorize, and every page you read today is building a brighter, independent future for you. Never give up—your journey has just begun!""",

        "cv": """**📄 How to Write a Strong Academic CV / Resume:**
- **Contact Info:** Full name, professional email address, phone number, and city/country.
- **Education:** List your high school or university, graduation year, and GPA.
- **Skills:** Include languages (Dari, Pashto, English), computer skills (Python, MS Office), and soft skills (Leadership, Teamwork).
- **Volunteer & Projects:** Mention projects you built (like RahaPath!) and any community or teaching activities.""",

        "university": """**🌐 Best Free Online Universities & Learning Platforms:**
- **University of the People (UoPeople):** Tuition-free, accredited American online university offering degrees in Computer Science, Business, and Health Science.
- **Coursera & edX:** Apply for Financial Aid to get free certificates from top universities like Harvard, Stanford, and Google.
- **Khan Academy:** Completely free lessons in Math, Science, and Computing for all levels."""
    }

    if st.button("Ask AI", key="ai_btn"):
        found = False
        for topic in knowledge_base:
            if topic in question.lower():
                st.success(knowledge_base[topic])
                found = True
                break
        if not found:
            st.info("Try asking about: **python, coding, scholarship, study, english, motivation, cv,** or **university** to get a detailed guide!")

with tab2:
    st.header("🌍 Scholarship Finder")
    level = st.radio("Select Study Level (مقطع تحصیلی):", ["Bachelor (لیسانس)", "Master (ماستری)", "Online Free Universities"])

    if level == "Bachelor (لیسانس)":
        st.success("**1. Turkiye Burslari (Turkey)**\n- Covers: Full tuition, dorm, monthly stipend, flight.\n- Requirement: High school diploma (GPA > 70%).\n- Website: turkiyeburslari.gov.tr")
        st.success("**2. DAAD Scholarships (Germany)**\n- Covers: Monthly stipend & health insurance.\n- Website: daad.de")
        st.success("**3. Romanian Government Scholarship**\n- Covers: Tuition, accommodation, monthly allowance.\n- Website: scholarships.studyinromania.gov.ro")
    elif level == "Master (ماستری)":
        st.success("**1. Chevening Scholarship (UK)**\n- Covers: Full tuition, living costs, flights.\n- Requirement: Bachelor degree + 2 years work/volunteer experience.\n- Website: chevening.org")
        st.success("**2. Erasmus Mundus (Europe)**\n- Covers: Study in 2-3 European countries with full funding.\n- Website: eacea.ec.europa.eu")
        st.success("**3. Fulbright Program (USA)**\n- Covers: Full Master's funding in the US.\n- Website: foreign.fulbrightonline.org")
    else:
        st.info("**1. University of the People (UoPeople)**\n- 100% Online, American accredited, tuition-free degrees in Computer Science & Business.\n- Website: uopeople.edu")
        st.info("**2. Coursera Financial Aid**\n- Free certificates from Google, Meta, and top universities.\n- Website: coursera.org")

with tab3:
    st.header("📚 English Learning Hub")
    st.subheader("📖 Today's Vocabulary (لغات امروز)")
    st.markdown("""

| English Word | Meaning (معنی فارسی) | Example Sentence |
| :--- | :--- | :--- |
| **Resilient** | مقاوم، تاب‌آور | *Afghan students are strong and resilient.* |
| **Opportunity** | فرصت | *Education creates new opportunities.* |
| **Achieve** | به دست آوردن، موفق شدن | *You can achieve all your dreams.* |
| **Determine** | مصمم بودن | *She is determined to learn coding.* |
""")

    st.markdown("---")
    st.subheader("📝 Quick English Quiz (آزمون کوتاه)")

    q1 = st.radio("1. What is the synonym of 'Resilient'?", ["Weak", "Strong", "Tired"], key="q1")
    q2 = st.radio("2. Which word means 'فرصت'?", ["Achieve", "Opportunity", "Barrier"], key="q2")
    q3 = st.radio("3. Complete: 'She is ____ to succeed.'", ["determined", "tired", "afraid"], key="q3")

    if st.button("Submit Quiz", key="quiz_btn"):
        score = 0
        if q1 == "Strong":
            score += 1
        if q2 == "Opportunity":
            score += 1
        if q3 == "determined":
            score += 1

        st.metric("Your Score", f"{score} / 3")
        if score == 3:
            st.success("🎉 Perfect! 3/3! You mastered today's lesson!")
        elif score == 2:
            st.info("👍 Good job! 2/3! Review the table above once more.")
        else:
            st.warning("💪 Keep practicing! Read the vocabulary table and try again.")

with tab4:
    st.header("📅 Daily Study Planner")
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    new_task = st.text_input("Add a new study task (مثلاً: خواندن فصل دوم):")
    if st.button("Add Task", key="task_btn") and new_task:
        st.session_state.tasks.append(new_task)
        st.success("Task added!")

    st.subheader("Your Study Checklist:")
    if len(st.session_state.tasks) == 0:
        st.write("No tasks yet. Add your first study goal above!")
    for idx, t in enumerate(st.session_state.tasks):
        st.checkbox(t, key=f"task_{idx}")

with tab5:
    st.header("🧮 Smart Problem Solver")
    tool = st.selectbox("Choose a tool:", ["Grade Percentage Calculator (فیصدی نمرات)", "Quick Math Calculator"])

    if tool == "Grade Percentage Calculator (فیصدی نمرات)":
        scores_input = st.text_input("Enter scores separated by commas (مثلاً: 85, 90, 95):")
        if st.button("Calculate Percentage", key="calc_btn") and scores_input:
            try:
                scores = [float(x.strip()) for x in scores_input.split(",")]
                avg = sum(scores) / len(scores)
                st.metric("Average Percentage", f"{avg:.2f}%")
                if avg >= 55:
                    st.success("Status: Passed! Great job! 🎉")
                else:
                    st.warning("Status: Needs more study. Keep trying!")
            except Exception:
                st.error("Please enter valid numbers separated by commas (e.g., 80, 90, 85).")

    elif tool == "Quick Math Calculator":
        num1 = st.number_input("First number:", value=0.0)
        op = st.selectbox("Operation:", ["+", "-", "*", "/"])
