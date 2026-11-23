import streamlit as st
import requests
import math

st.set_page_config(page_title="RahaPath - Empowering Education", page_icon="🎓", layout="centered")

st.markdown("""
<style>
    .main-banner {
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
        padding: 20px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 16px;
    }
    .main-banner h1 { margin: 0; font-size: 2rem; color: white; }
    .main-banner p { margin: 5px 0 0 0; font-size: 0.95rem; }
    .stButton > button { border-radius: 10px; font-weight: 600; width: 100%; }
</style>
<div class="main-banner">
    <h1>🎓 RahaPath</h1>
    <p>Empowering Students Worldwide through AI & Open Education</p>
    <p style="font-size: 0.88rem;">پلتفرم هوشمند خودآموزی، زبان انگلیسی، بورسیه‌ها و حل مسائل</p>
</div>
""", unsafe_allow_html=True)

def ask_ai(prompt_text):
    api_key = st.secrets.get("OPENROUTER_API_KEY", "").strip()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://streamlit.app",
        "X-Title": "RahaPath"
    }
    live_models = []
    try:
        r = requests.get("https://openrouter.ai", timeout=8)
        if r.status_code == 200:
            for item in r.json().get("data", []):
                mid = item.get("id", "")
                if mid.endswith(":free"):
                    live_models.append(mid)
    except Exception:
        pass
    if len(live_models) == 0:
        live_models = ["openrouter/free", "meta-llama/llama-3.3-70b-instruct:free"]

    for m in live_models[:6]:
        try:
            data = {
                "model": m,
                "messages": [
                    {"role": "system", "content": "You are RahaPath AI, a helpful educational assistant for students. Answer clearly, accurately, and thoroughly in the exact same language the user asks."},
                    {"role": "user", "content": prompt_text}
                ]
            }
            res = requests.post("https://openrouter.ai", headers=headers, json=data, timeout=25)
            if res.status_code == 200:
                for ch in res.json().get("choices", []):
                    txt = ch.get("message", {}).get("content", "").strip()
                    if txt != "":
                        return txt
        except Exception:
            continue
    return ""

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🤖 AI Assistant",
    "🌍 Scholarships",
    "📚 English Hub",
    "📅 Study Planner",
    "🧮 Math & Solver"
])

# --- Tab 1: AI Assistant ---
with tab1:
    st.subheader("🤖 AI Study Assistant | دستیار هوشمند درسی")
    mode = st.selectbox("Select Mode / انتخاب حالت:", [
        "1. General & Study Q&A (پرسش و پاسخ عمومی و درسی)",
        "2. Translator & Grammar Fixer (ترجمه و اصلاح گرامر)",
        "3. Explain Complex Topics Simply (توضیح ساده موضوعات سخت)"
    ], key="ai_mode")
    question = st.text_area("Ask any question in English or Persian / سوال خود را بنویسید:", height=90, key="ai_q")
    if st.button("✨ Ask AI / دریافت پاسخ", key="ai_btn"):
        if question.strip() == "":
            st.warning("Please enter your question first! / لطفاً اول سوال خود را بنویسید!")
        if question.strip() != "":
            with st.spinner("Thinking... / در حال پردازش پاسخ..."):
                p = question
                if mode.startswith("2."): p = f"Translate between Persian and English and correct any grammar mistakes with clear explanations: {question}"
                if mode.startswith("3."): p = f"Explain this topic simply step-by-step with clear examples in the same language as the input: {question}"
                ans = ask_ai(p)
                if ans != "": st.success(ans)
                if ans == "": st.warning("Free AI servers are busy right now. Please wait 5 seconds and try again.")

# --- Tab 2: Smart Scholarship Matcher ---
with tab2:
    st.subheader("🌍 Smart Scholarship Matcher | جستجوگر هوشمند بورسیه")
    st.write("Select your profile to find matching scholarships / شرایط خود را انتخاب کنید:")

    sch_mode = st.radio("Choose Section / انتخاب بخش:", [
        "1. Find Matching Scholarships (یافتن بورسیه بر اساس شرایط)",
        "2. Application Checklist (چک‌لیست مدارک لازم)",
        "3. AI Motivation Letter Writer (نگارش انگیزه‌نامه)"
    ], key="sch_radio")

    if sch_mode.startswith("1."):
        c1, c2 = st.columns(2)
        with c1:
            deg = st.selectbox("Degree Level / مقطع تحصیلی:", ["Bachelor (لیسانس)", "Master (ماستری)", "Online Free University"], key="s_deg")
            gpa = st.selectbox("GPA / فیصدی نمرات:", ["Above 85% (بالای ۸۵٪)", "70% - 85% (بین ۷۰ تا ۸۵٪)", "Below 70% (زیر ۷۰٪)"], key="s_gpa")
        with c2:
            eng_lvl = st.selectbox("English Level / سطح زبان:", ["Certified (Duolingo/IELTS)", "Intermediate (بدون مدرک)", "Beginner (مبتدی)"], key="s_eng")
            region = st.selectbox("Preferred Region / منطقه:", ["All Regions (همه کشورها)", "Asia (ترکیه، جاپان، کوریا)", "Europe (اروپا)", "USA & Australia", "Online from Home"], key="s_reg")

        if st.button("🔍 Find Scholarships / پیدا کردن بورسیه‌ها", key="find_sch"):
            st.markdown("### 🎯 Matching Opportunities / نتایج مناسب شما:")
            if deg == "Online Free University" or region == "Online from Home" or eng_lvl.startswith("Beginner"):
                st.info("**1. University of the People (UoPeople):** Tuition-free, accredited American online university | [uopeople.edu](https://uopeople.edu)")
                st.info("**2. Coursera Financial Aid:** Free certificates from top global universities | [coursera.org](https://coursera.org)")
            if deg == "Bachelor (لیسانس)" and not gpa.startswith("Below"):
                if region in ["All Regions (همه کشورها)", "Asia (ترکیه، جاپان، کوریا)"]:
                    st.success("**1. Türkiye Burslari (Turkey):** Full tuition, dorm, stipend & flight | [turkiyeburslari.gov.tr](https://turkiyeburslari.gov.tr)")
                    st.success("**2. MEXT (Japan) & GKS (South Korea):** Fully funded government scholarships | [studyinjapan.go.jp](https://studyinjapan.go.jp)")
                if region in ["All Regions (همه کشورها)", "Europe (اروپا)"]:
                    st.success("**3. Stipendium Hungaricum (Hungary):** Free tuition, housing & stipend in Europe | [stipendiumhungaricum.hu](https://stipendiumhungaricum.hu)")
                    st.success("**4. Romanian Government Scholarship:** Fully funded bachelor programs | [studyinromania.gov.ro](https://studyinromania.gov.ro)")
            if deg == "Master (ماستری)":
                st.success("**1. Chevening (UK) & Erasmus Mundus (Europe):** Fully funded Master's degrees | [chevening.org](https://chevening.org)")
                st.success("**2. DAAD (Germany) & Fulbright (USA):** Prestigious graduate scholarships | [daad.de](https://daad.de)")

            with st.spinner("Searching personalized AI recommendations..."):
                ai_s = ask_ai(f"Recommend 3 specific real scholarships with official websites for a student with: Degree={deg}, GPA={gpa}, English={eng_lvl}, Region={region}. Provide bilingual English and Persian bullet points.")
                if ai_s != "":
                    st.markdown("#### ✨ Personalized AI Recommendations:")
                    st.success(ai_s)

    if sch_mode.startswith("2."):
        st.checkbox("1. Valid Passport or National ID (پاسپورت یا تذکره الکترونیکی)", key="c1")
        st.checkbox("2. High School Diploma & Transcripts (شهادت‌نامه و نمرات سه‌ساله)", key="c2")
        st.checkbox("3. Official English Translations (ترجمه رسمی انگلیسی مدارک)", key="c3")
        st.checkbox("4. Motivation Letter / SOP (انگیزه‌نامه اختصاصی)", key="c4")
        st.checkbox("5. Two Academic Recommendation Letters (دو توصیه‌نامه از استادان)", key="c5")
        st.checkbox("6. English Proficiency Certificate - Duolingo / IELTS (مدرک زبان)", key="c6")
        st.checkbox("7. Academic CV / Resume (رزومه تحصیلی)", key="c7")

    if sch_mode.startswith("3."):
        f_in = st.text_input("Field of Study / رشته تحصیلی (e.g., Computer Science):", key="sop_f")
        c_in = st.text_input("Target Country or Scholarship / کشور یا بورسیه مقصد:", key="sop_c")
        if st.button("✍️ Generate Motivation Letter / نگارش انگیزه‌نامه", key="sop_btn"):
            if f_in.strip() != "" and c_in.strip() != "":
                with st.spinner("Writing your Motivation Letter..."):
                    sop = ask_ai(f"Write a strong 400-word scholarship Motivation Letter in English for a student applying for {f_in} in {c_in}, highlighting resilience, self-learning, and community impact.")
                    if sop != "": st.success(sop)

# --- Tab 3: Unlimited English Academy ---
with tab3:
    st.subheader("📚 Unlimited English Academy | آکادمی جامع انگلیسی")
    eng_tab = st.selectbox("Choose Learning Module / انتخاب بخش آموزشی:", [
        "1. Dynamic Vocabulary Builder (بانک لغات نامحدود)",
        "2. Custom Topic Lesson Generator (درس‌ساز موضوعی)",
        "3. Complete English Grammar (گرامر کامل)",
        "4. Real-Life Conversations (مکالمات روزمره و مصاحبه)",
        "5. Interactive Quiz & AI Test Generator (آزمون تعاملی)"
    ], key="eng_select")

    if eng_tab.startswith("1."):
        v_topic = st.selectbox("Vocabulary Category / موضوع لغات:", [
            "Academic & Scholarship Words (لغات دانشگاهی و بورسیه)",
            "Technology & Coding (تکنولوژی و برنامه‌نویسی)",
            "Daily Life & Travel (زندگی روزمره و سفر)",
            "Business & Leadership (مدیریت و رهبری)",
            "Motivational & Success (انگیزشی و موفقیت)"
        ], key="v_top")
        if st.button("🔄 Load 10 New Words / دریافت ۱۰ لغت جدید", key="new_words_btn"):
            with st.spinner("Generating 10 fresh vocabulary words..."):
