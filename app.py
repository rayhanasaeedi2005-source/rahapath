import streamlit as st
import requests
from tools import render_planner_and_solver

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
    models = ["openrouter/free", "google/gemma-3-27b-it:free", "meta-llama/llama-3.3-70b-instruct:free", "mistralai/mistral-small-3.1-24b-instruct:free"]
    for m in models:
        try:
            data = {"model": m, "messages": [{"role": "system", "content": "You are RahaPath AI, a helpful educational assistant. Answer clearly and thoroughly in the exact same language the user asks."}, {"role": "user", "content": prompt_text}]}
            res = requests.post("https://openrouter.ai", headers=headers, json=data, timeout=25)
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
    st.subheader("🤖 AI Study Assistant | دستیار هوشمند")
    mode = st.selectbox("Mode / حالت:", ["1. Study Q&A (پرسش و پاسخ درسی)", "2. Translator & Grammar (ترجمه و گرامر)", "3. Simple Explanation (توضیح ساده)"], key="m1")
    q = st.text_area("Ask any question / سوال خود را بنویسید:", height=85, key="q1_in")
    if st.button("✨ Ask AI / دریافت پاسخ", key="b1") and q.strip() != "":
        p = f"Translate between Persian and English and fix grammar: {q}" if mode.startswith("2.") else (f"Explain simply step-by-step: {q}" if mode.startswith("3.") else q)
        ans = ask_ai(p)
        if ans != "": st.success(ans)
        if ans == "": st.warning("Server is busy, please click Ask AI again.")

with tab2:
    st.subheader("🌍 Smart Scholarship Matcher | بورسیه‌ها")
    sch = st.radio("Section / بخش:", ["1. Find Scholarships (یافتن بورسیه)", "2. Checklist (چک‌لیست)", "3. AI Motivation Letter (انگیزه‌نامه)"], key="r2")
    if sch.startswith("1."):
        deg = st.selectbox("Degree / مقطع:", ["Bachelor (لیسانس)", "Master (ماستری)", "Online Free University"], key="d2")
        gpa = st.selectbox("GPA / معدل:", ["Above 85%", "70% - 85%", "Below 70%"], key="g2")
        reg = st.selectbox("Region / منطقه:", ["All Regions", "Asia", "Europe", "Online"], key="rg2")
        if st.button("🔍 Find Scholarships / پیدا کردن", key="b2"):
            st.info("**Online:** UoPeople ([uopeople.edu](https://uopeople.edu)) & Coursera ([coursera.org](https://coursera.org))")
            if deg == "Bachelor (لیسانس)": st.success("**Bachelor:** Türkiye Burslari ([turkiyeburslari.gov.tr](https://turkiyeburslari.gov.tr)) | Stipendium Hungaricum ([stipendiumhungaricum.hu](https://stipendiumhungaricum.hu))")
            if deg == "Master (ماستری)": st.success("**Master:** Chevening ([chevening.org](https://chevening.org)) | Erasmus Mundus ([eacea.ec.europa.eu](https://europa.eu))")
            ai_s = ask_ai(f"Suggest 3 real scholarships with official websites for: Degree={deg}, GPA={gpa}, Region={reg}. Bilingual English and Persian.")
            if ai_s != "": st.success(ai_s)
    if sch.startswith("2."):
        st.checkbox("1. Valid Passport / تذکره الکترونیکی", key="ck1")
        st.checkbox("2. Diploma & Transcripts / شهادت‌نامه و نمرات", key="ck2")
        st.checkbox("3. Motivation Letter & CV / انگیزه‌نامه و رزومه", key="ck3")
        st.checkbox("4. Recommendation Letters / توصیه‌نامه", key="ck4")
    if sch.startswith("3."):
        f_in = st.text_input("Field / رشته تحصیلی:", key="f3")
        c_in = st.text_input("Country / کشور مقصد:", key="c3")
        if st.button("✍️ Write Letter / نگارش انگیزه‌نامه", key="b3") and f_in != "" and c_in != "":
            sop = ask_ai(f"Write a strong 350-word scholarship Motivation Letter in English for {f_in} in {c_in}.")
            if sop != "": st.success(sop)

with tab3:
    st.subheader("📚 English Academy | آکادمی انگلیسی")
    et = st.selectbox("Module / بخش:", ["1. Unlimited Vocabulary (لغات نامحدود)", "2. Custom Lesson (درس‌ساز موضوعی)", "3. Grammar (گرامر)", "4. Conversations (مکالمات)", "5. Quiz (آزمون)"], key="e3")
    if et.startswith("1."):
        vt = st.selectbox("Topic / موضوع:", ["Academic & Scholarship", "Technology & AI", "Daily Life & Travel", "Business"], key="vt3")
        if st.button("🔄 Load 10 New Words / ۱۰ لغت جدید", key="bw3"):
            wr = ask_ai(f"Give 10 fresh English vocabulary words about '{vt}' as a markdown table: English Word | Persian Meaning | Example Sentence.")
            if wr != "": st.session_state["w_list"] = wr
        st.markdown(st.session_state.get("w_list", "| Word | معنی | Example |\n| :--- | :--- | :--- |\n| **Resilient** | مقاوم، تاب‌آور | *Students are resilient.* |\n| **Opportunity** | فرصت | *Education creates opportunities.* |\n| **Achieve** | موفق شدن | *You can achieve your dreams.* |"))
    if et.startswith("2."):
        ct = st.text_input("Topic / موضوع دلخواه:", key="ct3")
        if st.button("📚 Build Lesson / ساخت درس", key="bl3") and ct.strip() != "":
            lo = ask_ai(f"Create an English lesson about '{ct}' for Persian speakers with 8 words (Persian meanings) and a 6-line dialogue with Persian translation.")
            if lo != "": st.success(lo)
    if et.startswith("3."):
        st.success("**Present:** We study daily. / She codes nightly.\n\n**Past:** I built my website.\n\n**Future:** I will win a scholarship.")
    if et.startswith("4."):
        st.info("**Intro:** *Hello! My name is Rayhana. I love coding and education.* (سلام! نام من ریحانه است و به کدنویسی علاقه‌مندم.)")
    if et.startswith("5."):
        q1 = st.radio("1. Synonym of 'Resilient'?", ["Weak", "Strong", "Tired"], key="qq1")
        q2 = st.radio("2. Meaning of 'Perseverance'?", ["پشتکار", "مانع", "اشتباه"], key="qq2")
        q3 = st.radio("3. 'She ____ Python daily.'", ["learn", "learns", "learning"], key="qq3")
        if st.button("✅ Submit / ثبت نمره", key="bq3"):
            sc = sum([q1 == "Strong", q2 == "پشتکار", q3 == "learns"])
            st.metric("Score / نمره", f"{sc} / 3")
        if st.button("🎲 New AI Quiz / آزمون جدید", key="bnq3"):
            nq = ask_ai("Create 5 new multiple-choice English vocabulary and grammar questions with answers and Persian explanations.")
            if nq != "": st.info(nq)

render_planner_and_solver(tab4, tab5, ask_ai)
st.markdown("---")
st.caption("Built with ❤️ by Rayhana | RahaPath Global (2026)")
