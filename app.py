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
                    m_res = requests.get("https://openrouter.ai", timeout=10)
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
                        response = requests.post("https://openrouter.ai", headers=headers, json=data, timeout=20)
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
                    st.warning("سرورهای رایگان در این لحظه بسیار شلوغ هستند. لطفاً ۵ ثانیه صبر کنید و دوباره دکمه Ask AI را بزنید.")

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
    eng_section = st.radio("Choose a lesson (بخش مورد نظر را انتخاب کنید):", [
        "📖 Vocabulary (لغات مهم)",
        "🗣️ Daily Conversation (مکالمه روزمره)",
        "📐 Grammar (گرامر کاربردی)",
        "📝 English Quiz (آزمون ۵ سوالی)"
    ])

    if eng_section == "📖 Vocabulary (لغات مهم)":
        st.subheader("Essential Academic & Motivational Words")
        st.markdown("""

| English Word | Meaning (معنی فارسی) | Example Sentence |
| :--- | :--- | :--- |
| **Resilient** | مقاوم، تاب‌آور | *Afghan students are strong and resilient.* |
| **Opportunity** | فرصت | *Education creates new opportunities.* |
| **Achieve** | به دست آوردن، موفق شدن | *You can achieve all your dreams.* |
| **Determine** | مصمم بودن | *She is determined to learn coding.* |
| **Knowledge** | دانش، علم | *Knowledge is power that no one can take.* |
| **Perseverance** | پشتکار، استقامت | *Success comes through daily perseverance.* |
| **Fluently** | روان و سلیس | *I want to speak English fluently.* |
| **Independent** | مستقل | *Learning skills makes you independent.* |
""")

    if eng_section == "🗣️ Daily Conversation (مکالمه روزمره)":
        st.subheader("Useful Everyday Phrases")
        st.info("**1. Introducing Yourself (معرفی خود):**\n- *Hello! My name is Rayhana, and I am passionate about technology.*\n- سلام! نام من ریحانه است و به تکنولوژی علاقه‌مند هستم.")
        st.info("**2. Talking About Goals (صحبت درباره اهداف):**\n- *I am studying hard to win an international scholarship.*\n- من سخت درس می‌خوانم تا یک بورسیه بین‌المللی به دست بیاورم.")
        st.info("**3. Asking for Help (درخواست کمک درسی):**\n- *Could you please explain this topic in simple words?*\n- آیا می‌توانید لطفاً این موضوع را با کلمات ساده توضیح دهید؟")
        st.info("**4. Encouraging Friends (انگیزه دادن به دوستان):**\n- *Never give up! Every small step brings us closer to success.*\n- هرگز تسلیم نشو! هر قدم کوچک ما را به موفقیت نزدیک‌تر می‌کند.")

    if eng_section == "📐 Grammar (گرامر کاربردی)":
        st.subheader("Simple Present Tense (زمان حال ساده)")
        st.write("از این زمان برای بیان **عادت‌های روزمره، حقایق علمی و برنامه‌های همیشگی** استفاده می‌کنیم.")
        st.success("**Formula (فرمول):**\n- **I / You / We / They** + Verb (فعل ساده)\n  *Example:* We **study** English every day.\n- **He / She / It** + Verb + **s / es**\n  *Example:* She **codes** on her phone every evening.")
        st.warning("**Negative (منفی کردن):**\n- Use **do not (don't)** or **does not (doesn't)**:\n  *Example:* They **don't** give up. / He **doesn't** waste time.")

    if eng_section == "📝 English Quiz (آزمون ۵ سوالی)":
        st.subheader("Test Your English Skills!")
        q1 = st.radio("1. What is the synonym of 'Resilient'?", ["Weak", "Strong", "Tired"], key="q1")
        q2 = st.radio("2. Which word means 'پشتکار و استقامت'?", ["Perseverance", "Barrier", "Mistake"], key="q2")
        q3 = st.radio("3. Complete: 'She ____ Python every day.'", ["learn", "learns", "learning"], key="q3")
        q4 = st.radio("4. Complete: 'We ____ give up on our dreams.'", ["doesn't", "don't", "isn't"], key="q4")
        q5 = st.radio("5. Which word means 'روان و سلیس'?", ["Slowly", "Fluently", "Quietly"], key="q5")

        if st.button("Submit Quiz", key="quiz_btn"):
            score = 0
            if q1 == "Strong":
                score = score + 1
            if q2 == "Perseverance":
                score = score + 1
            if q3 == "learns":
                score = score + 1
            if q4 == "don't":
                score = score + 1
            if q5 == "Fluently":
                score = score + 1

            st.metric("Your Final Score", f"{score} / 5")
            if score == 5:
                st.success("🎉 Amazing! 5/5! You mastered all the lessons!")
            if score == 3 or score == 4:
                st.info("👍 Great job! Review the Vocabulary and Grammar sections to get 5/5!")
            if score < 3:
                st.warning("💪 Good start! Read the lessons above once more and try again.")

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
