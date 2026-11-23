import streamlit as st
import requests
import math

st.set_page_config(page_title="RahaPath - Empowering Education", page_icon="🎓", layout="centered")

st.markdown("""
<style>
    .main-banner { background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%); padding: 20px; border-radius: 16px; color: white; text-align: center; margin-bottom: 16px; }
    .main-banner h1 { margin: 0; font-size: 2rem; color: white; }
    .main-banner p { margin: 5px 0 0 0; font-size: 0.92rem; }
    .stButton > button { border-radius: 10px; font-weight: 600; width: 100%; }
</style>
<div class="main-banner">
    <h1>🎓 RahaPath</h1>
    <p>Empowering Students Worldwide through AI & Open Education</p>
    <p>پلتفرم هوشمند خودآموزی، زبان انگلیسی، بورسیه‌ها و حل مسائل</p>
</div>
""", unsafe_allow_html=True)

def ask_ai(prompt_text):
    api_key = st.secrets.get("OPENROUTER_API_KEY", "").strip()
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json", "HTTP-Referer": "https://streamlit.app", "X-Title": "RahaPath"}
    free_models = []
    try:
        r = requests.get("https://openrouter.ai", timeout=8)
        if r.status_code == 200:
            for item in r.json().get("data", []):
                if item.get("id", "").endswith(":free"):
                    free_models.append(item.get("id"))
    except Exception:
        pass
    if len(free_models) == 0:
        free_models = ["openrouter/free"]
    for m in free_models[:8]:
        try:
            data = {"model": m, "messages": [{"role": "system", "content": "You are RahaPath AI, a helpful educational assistant. Answer clearly and thoroughly in the exact same language the user asks."}, {"role": "user", "content": prompt_text}]}
            res = requests.post("https://openrouter.ai", headers=headers, json=data, timeout=20)
            if res.status_code == 200:
                for ch in res.json().get("choices", []):
                    txt = ch.get("message", {}).get("content", "").strip()
                    if txt != "":
                        return txt
        except Exception:
            continue
    return ""

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🤖 AI Assistant", "🌍 Scholarships", "📚 English Hub", "📅 Study Planner", "🧮 Math & Solver"])

with tab1:
    st.subheader("🤖 AI Study Assistant | دستیار هوشمند درسی")
    mode = st.selectbox("Select Mode / انتخاب حالت:", ["1. General & Study Q&A (پرسش و پاسخ درسی)", "2. Translator & Grammar Fixer (ترجمه و گرامر)", "3. Simple Explanation (توضیح ساده)"], key="m1")
    q = st.text_area("Ask any question in English or Persian / سوال خود را بنویسید:", height=85, key="q1_in")
    if st.button("✨ Ask AI / دریافت پاسخ", key="b1"):
        if q.strip() != "":
            st.info("⏳ Thinking... / در حال پاسخ‌گویی...")
            p = f"Translate between Persian and English and fix grammar: {q}" if mode.startswith("2.") else (f"Explain simply step-by-step: {q}" if mode.startswith("3.") else q)
            ans = ask_ai(p)
            if ans != "": st.success(ans)
            if ans == "": st.warning("Free servers are busy. Please click Ask AI again in 5 seconds.")

with tab2:
    st.subheader("🌍 Smart Scholarship Matcher | جستجوگر بورسیه")
    sch = st.radio("Section / بخش:", ["1. Find Scholarships (یافتن بورسیه بر اساس شرایط)", "2. Checklist (چک‌لیست مدارک)", "3. AI Motivation Letter (انگیزه‌نامه)"], key="r2")
    if sch.startswith("1."):
        deg = st.selectbox("Degree / مقطع:", ["Bachelor (لیسانس)", "Master (ماستری)", "Online Free University"], key="d2")
        gpa = st.selectbox("GPA / معدل:", ["Above 85% (بالای ۸۵٪)", "70% - 85% (بین ۷۰ تا ۸۵٪)", "Below 70% (زیر ۷۰٪)"], key="g2")
        reg = st.selectbox("Region / منطقه:", ["All Regions (همه کشورها)", "Asia (ترکیه، جاپان، کوریا)", "Europe (اروپا)", "Online from Home"], key="rg2")
        if st.button("🔍 Find Scholarships / پیدا کردن بورسیه", key="b2"):
            st.info("**Online Free:** UoPeople ([uopeople.edu](https://uopeople.edu)) & Coursera ([coursera.org](https://coursera.org))")
            if deg == "Bachelor (لیسانس)" and not gpa.startswith("Below"):
                st.success("**Asia & Europe:** Türkiye Burslari ([turkiyeburslari.gov.tr](https://turkiyeburslari.gov.tr)) | Stipendium Hungaricum ([stipendiumhungaricum.hu](https://stipendiumhungaricum.hu)) | MEXT Japan ([studyinjapan.go.jp](https://studyinjapan.go.jp))")
            if deg == "Master (ماستری)":
                st.success("**Global Master's:** Chevening UK ([chevening.org](https://chevening.org)) | Erasmus Mundus ([eacea.ec.europa.eu](https://europa.eu)) | DAAD ([daad.de](https://daad.de))")
            ai_s = ask_ai(f"Suggest 3 real scholarships with official websites for: Degree={deg}, GPA={gpa}, Region={reg}. Answer in bilingual English and Persian.")
            if ai_s != "": st.success(ai_s)
    if sch.startswith("2."):
        st.checkbox("1. Valid Passport / تذکره الکترونیکی", key="ck1")
        st.checkbox("2. Diploma & Transcripts / شهادت‌نامه و نمرات ترجمه‌شده", key="ck2")
        st.checkbox("3. Motivation Letter & CV / انگیزه‌نامه و رزومه", key="ck3")
        st.checkbox("4. Two Recommendation Letters / دو توصیه‌نامه", key="ck4")
        st.checkbox("5. English Certificate (Duolingo / IELTS) / مدرک زبان", key="ck5")
    if sch.startswith("3."):
        f_in = st.text_input("Field of Study / رشته تحصیلی:", key="f3")
        c_in = st.text_input("Country or Scholarship / کشور یا بورسیه:", key="c3")
        if st.button("✍️ Write Motivation Letter / نگارش انگیزه‌نامه", key="b3") and f_in != "" and c_in != "":
            st.info("⏳ Writing...")
            sop = ask_ai(f"Write a strong 350-word scholarship Motivation Letter in English for {f_in} in {c_in}.")
            if sop != "": st.success(sop)

with tab3:
    st.subheader("📚 Unlimited English Academy | آکادمی انگلیسی")
    et = st.selectbox("Module / بخش:", ["1. Unlimited Vocabulary (لغات نامحدود)", "2. Custom Lesson Generator (درس‌ساز موضوعی)", "3. Grammar Guide (گرامر)", "4. Conversations (مکالمات)", "5. Interactive Quiz (آزمون)"], key="e3")
    if et.startswith("1."):
        vt = st.selectbox("Topic / موضوع:", ["Academic & Scholarship", "Technology & AI", "Daily Life & Travel", "Business & Leadership"], key="vt3")
        if st.button("🔄 Load 10 New Words / دریافت ۱۰ لغت جدید", key="bw3"):
            st.info("⏳ Loading new words...")
            wr = ask_ai(f"Give 10 fresh English vocabulary words about '{vt}' as a markdown table: English Word | Persian Meaning | Example Sentence.")
            if wr != "": st.session_state["w_list"] = wr
        st.markdown(st.session_state.get("w_list", "| Word | معنی | Example |\n| :--- | :--- | :--- |\n| **Resilient** | مقاوم، تاب‌آور | *Students are resilient.* |\n| **Opportunity** | فرصت | *Education creates opportunities.* |\n| **Achieve** | موفق شدن | *You can achieve your dreams.* |\n| **Perseverance** | پشتکار | *Success needs perseverance.* |\n| **Fluently** | روان و سلیس | *She speaks English fluently.* |"))
    if et.startswith("2."):
        ct = st.text_input("Enter any topic / هر موضوعی بنویسید:", key="ct3")
        if st.button("📚 Build Lesson / ساخت درس", key="bl3") and ct.strip() != "":
            st.info("⏳ Building lesson...")
            lo = ask_ai(f"Create an English lesson about '{ct}' for Persian speakers with 8 words (Persian meanings), a 6-line dialogue with Persian translation, and 2 grammar tips.")
            if lo != "": st.success(lo)
    if et.startswith("3."):
        st.success("**Simple Present:** I/You/We/They + Verb (*We study daily.*) | He/She/It + Verb+s (*She codes nightly.*)")
        st.success("**Simple Past:** Subject + Past Verb (*I built my website yesterday.*)")
        st.success("**Simple Future:** Subject + will + Verb (*I will win a scholarship.*)")
        st.success("**Present Continuous:** Subject + am/is/are + Verb-ing (*I am learning Python now.*)")
    if et.startswith("4."):
        st.info("**Intro:** *Hello! My name is Rayhana. I am passionate about coding and education.* (سلام! نام من ریحانه است و به کدنویسی و آموزش علاقه‌مندم.)")
        st.info("**Project:** *I built RahaPath to empower students worldwide.* (من RahaPath را برای توانمندسازی دانشجویان ساختم.)")
    if et.startswith("5."):
        q1 = st.radio("1. Synonym of 'Resilient'?", ["Weak", "Strong", "Tired"], key="qq1")
        q2 = st.radio("2. Meaning of 'Perseverance'?", ["پشتکار", "مانع", "اشتباه"], key="qq2")
        q3 = st.radio("3. 'She ____ Python daily.'", ["learn", "learns", "learning"], key="qq3")
        q4 = st.radio("4. Past tense of 'Build'?", ["Builded", "Built", "Building"], key="qq4")
        q5 = st.radio("5. 'If you study, you ____ succeed.'", ["will", "did", "was"], key="qq5")
        if st.button("✅ Submit Quiz / ثبت آزمون", key="bq3"):
            sc = sum([q1 == "Strong", q2 == "پشتکار", q3 == "learns", q4 == "Built", q5 == "will"])
            st.metric("Score / نمره", f"{sc} / 5")
            st.success("🎉 Excellent! 5/5!" if sc == 5 else "👍 Good job! Review and try again.")
        if st.button("🎲 New AI Quiz / آزمون جدید با AI", key="bnq3"):
            st.info("⏳ Creating new quiz...")
            nq = ask_ai("Create 5 new multiple-choice English vocabulary and grammar questions with answers and Persian explanations.")
            if nq != "": st.info(nq)

with tab4:
    st.subheader("📅 Smart Study Planner | برنامه‌ریز درسی")
    st.info("⏱️ **Pomodoro Rule:** 25 mins study + 5 mins break | ۲۵ دقیقه مطالعه + ۵ دقیقه استراحت")
    if "tasks" not in st.session_state: st.session_state.tasks = []
    nt = st.text_input("Study Goal / هدف درسی امروز:", key="nt4")
    if st.button("➕ Add Goal / افزودن هدف", key="ba4") and nt.strip() != "":
        st.session_state.tasks.append(nt.strip())
