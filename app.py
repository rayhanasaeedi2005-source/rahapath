import streamlit as st
import requests

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
    st.write("Ask ANY question in English or Persian (هر سوال درسی یا عمومی دارید بپرسید):")
    question = st.text_input("Type your question here (سوال خود را بنویسید):")
    if st.button("Ask AI", key="ai_btn"):
        if question.strip() == "":
            st.warning("Please type a question first! (لطفاً اول یک سوال بنویسید)")
        if question.strip() != "":
            with st.spinner("Thinking... (در حال دریافت پاسخ از هوش مصنوعی...)"):
                answered = False
                api_key = st.secrets.get("OPENROUTER_API_KEY", "").strip()
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://streamlit.app",
                    "X-Title": "RahaPath"
                }
                live_free_models = []
                try:
                    m_res = requests.get("https://openrouter.ai/api/v1/models", timeout=10)
                    if m_res.status_code == 200:
                        for m in m_res.json().get("data", []):
                            mid = m.get("id", "")
                            if mid.endswith(":free"):
                                live_free_models.append(mid)
                except Exception:
                    pass
                if len(live_free_models) == 0:
                    live_free_models = ["openrouter/free"]

                for model_name in live_free_models[:6]:
                    if answered:
                        break
                    try:
                        data = {
                            "model": model_name,
                            "messages": [
                                {"role": "system", "content": "You are RahaPath AI, a helpful educational assistant for Afghan students. Answer clearly, accurately, and thoroughly in the same language the user asks."},
                                {"role": "user", "content": question}
                            ]
                        }
                        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data, timeout=20)
                        if response.status_code == 200:
                            result = response.json()
                            for item in result.get("choices", []):
                                text = item.get("message", {}).get("content", "").strip()
                                if text != "":
                                    st.success(text)
                                    answered = True
                                    break
                    except Exception:
                        continue
                if not answered:
                    st.error("لطفاً در صفحه Privacy سایت OpenRouter گزینه دوم (Allow free endpoints that publish prompts) را هم روشن کنید و دوباره Ask AI را بزنید.")

with tab2:
    st.header("🌍 Scholarship Finder")
    level = st.radio("Select Study Level (مقطع تحصیلی):", ["Bachelor (لیسانس)", "Master (ماستری)", "Online Free Universities"])
    if level == "Bachelor (لیسانس)":
        st.success("**1. Turkiye Burslari (Turkey)**\n- Covers: Full tuition, dorm, monthly stipend, flight.\n- Requirement: High school diploma (GPA > 70%).\n- Website: turkiyeburslari.gov.tr")
        st.success("**2. DAAD Scholarships (Germany)**\n- Covers: Monthly stipend & health insurance.\n- Website: daad.de")
        st.success("**3. Romanian Government Scholarship**\n- Covers: Tuition, accommodation, monthly allowance.\n- Website: scholarships.studyinromania.gov.ro")
    if level == "Master (ماستری)":
        st.success("**1. Chevening Scholarship (UK)**\n- Covers: Full tuition, living costs, flights.\n- Requirement: Bachelor degree + 2 years work/volunteer experience.\n- Website: chevening.org")
        st.success("**2. Erasmus Mundus (Europe)**\n- Covers: Study in 2-3 European countries with full funding.\n- Website: eacea.ec.europa.eu")
        st.success("**3. Fulbright Program (USA)**\n- Covers: Full Master's funding in the US.\n- Website: foreign.fulbrightonline.org")
    if level == "Online Free Universities":
        st.info("**1. University of the People (UoPeople)**\n- 100% Online, American accredited, tuition-free degrees in Computer Science & Business.\n- Website: uopeople.edu")
        st.info("**2. Coursera Financial Aid**\n- Free certificates from Google, Meta, and top universities.\n- Website: coursera.org")

with tab3:
    st.header("📚 English Learning Hub")
    st.subheader("📖 Today's Vocabulary (لغات امروز)")
    st.markdown("| English Word | Meaning (معنی فارسی) | Example Sentence |\n| :--- | :--- | :--- |\n| **Resilient** | مقاوم، تاب‌آور | *Afghan students are strong and resilient.* |\n| **Opportunity** | فرصت | *Education creates new opportunities.* |\n| **Achieve** | به دست آوردن، موفق شدن | *You can achieve all your dreams.* |\n| **Determine** | مصمم بودن | *She is determined to learn coding.* |")
    st.markdown("---")
    st.subheader("📝 Quick English Quiz (آزمون کوتاه)")
    q1 = st.radio("1. What is the synonym of 'Resilient'?", ["Weak", "Strong", "Tired"], key="q1")
    q2 = st.radio("2. Which word means 'فرصت'?", ["Achieve", "Opportunity", "Barrier"], key="q2")
    q3 = st.radio("3. Complete: 'She is ____ to succeed.'", ["determined", "tired", "afraid"], key="q3")
    if st.button("Submit Quiz", key="quiz_btn"):
        score = 0
        if q1 == "Strong":
            score = score + 1
        if q2 == "Opportunity":
            score = score + 1
        if q3 == "determined":
            score = score + 1
        st.metric("Your Score", f"{score} / 3")
        if score == 3:
            st.success("🎉 Perfect! 3/3! You mastered today's lesson!")
        if score == 2:
            st.info("👍 Good job! 2/3! Review the table above once more.")
        if score < 2:
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
            scores = [float(x.strip()) for x in scores_input.split(",")]
            avg = sum(scores) / len(scores)
            st.metric("Average Percentage", f"{avg:.2f}%")
            if avg >= 55:
                st.success("Status: Passed! Great job! 🎉")
            if avg < 55:
                st.warning("Status: Needs more study. Keep trying!")
    if tool == "Quick Math Calculator":
        num1 = st.number_input("First number:", value=0.0)
        op = st.selectbox("Operation:", ["+", "-", "*", "/"])
        num2 = st.number_input("Second number:", value=0.0)
        if st.button("Solve", key="math_btn"):
            if op == "+":
                st.success(f"Result: {num1 + num2}")
            if op == "-":
                st.success(f"Result: {num1 - num2}")
            if op == "*":
                st.success(f"Result: {num1 * num2}")
            if op == "/" and num2 != 0:
                st.success(f"Result: {num1 / num2}")
            if op == "/" and num2 == 0:
                st.error("Cannot divide by zero!")
