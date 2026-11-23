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
    <h1>🎓 RahaPath v4.0</h1>
    <p>Empowering Afghan Students through AI & Education</p>
    <p>پلتفرم جامع خودآموزی، زبان انگلیسی، بورسیه‌ها و هوش مصنوعی</p>
</div>
""", unsafe_allow_html=True)

def ask_openrouter(prompt_text):
    api_key = st.secrets.get("OPENROUTER_API_KEY", "").strip()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://streamlit.app",
        "X-Title": "RahaPath"
    }
    models = ["openrouter/free", "meta-llama/llama-3.3-70b-instruct:free", "google/gemma-3-27b-it:free"]
    for m in models:
        try:
            data = {
                "model": m,
                "messages": [
                    {"role": "system", "content": "You are RahaPath AI, a helpful educational assistant for Afghan students. Answer clearly and thoroughly in the same language the user asks."},
                    {"role": "user", "content": prompt_text}
                ]
            }
            res = requests.post("https://openrouter.ai", headers=headers, json=data, timeout=25)
            if res.status_code == 200:
                for item in res.json().get("choices", []):
                    text = item.get("message", {}).get("content", "").strip()
                    if text != "":
                        return text
        except Exception:
            continue
    return ""

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🤖 AI Assistant",
    "🌍 Scholarships",
    "📚 English",
    "📅 Planner",
    "🧮 Solver"
])

with tab1:
    st.subheader("🤖 AI Study Assistant")
    mode = st.selectbox("حالت دستیار:", [
        "1. پرسش و پاسخ عمومی و درسی",
        "2. ترجمه و اصلاح گرامر انگلیسی",
        "3. توضیح ساده موضوعات علمی"
    ])
    question = st.text_area("سوال یا متن خود را بنویسید:", height=90)
    if st.button("✨ دریافت پاسخ (Ask AI)", key="ai_btn"):
        if question.strip() == "": st.warning("لطفاً اول سوال خود را بنویسید!")
        if question.strip() != "":
            with st.spinner("در حال پردازش پاسخ..."):
                p = question
                if mode.startswith("2."): p = f"Translate between Persian and English and fix grammar mistakes: {question}"
                if mode.startswith("3."): p = f"Explain simply step-by-step with examples: {question}"
                ans = ask_openrouter(p)
                if ans != "": st.success(ans)
                if ans == "": st.warning("سرورهای رایگان شلوغ هستند، لطفاً ۵ ثانیه بعد دوباره بزنید.")

with tab2:
    st.subheader("🌍 Global Scholarships & Apply Hub")
    sch = st.radio("بخش مورد نظر:", [
        "1. بانک جامع بورسیه‌ها",
        "2. چک‌لیست ۱۰ مرحله‌ای مدارک",
        "3. نگارش هوشمند انگیزه‌نامه (AI)"
    ])
    if sch.startswith("1."):
        lvl = st.selectbox("مقطع تحصیلی:", ["1. Bachelor (لیسانس)", "2. Master (ماستری)", "3. Online Free Universities"])
        if lvl.startswith("1."):
            st.success("**1. Türkiye Burslari (ترکیه):** شهریه، خوابگاه و کمک‌هزینه | [turkiyeburslari.gov.tr](https://turkiyeburslari.gov.tr)")
            st.success("**2. Stipendium Hungaricum (مجارستان):** تحصیل و خوابگاه رایگان | [stipendiumhungaricum.hu](https://stipendiumhungaricum.hu)")
            st.success("**3. MEXT (جاپان):** بورسیه کامل دولت جاپان | [studyinjapan.go.jp](https://studyinjapan.go.jp)")
            st.success("**4. GKS (کوریای جنوبی):** پوشش کامل شهریه و زندگی | [studyinkorea.go.kr](https://studyinkorea.go.kr)")
            st.success("**5. Romanian Scholarship (رومانی):** تحصیل رایگان در اروپا | [studyinromania.gov.ro](https://studyinromania.gov.ro)")
        if lvl.startswith("2."):
            st.success("**1. Chevening (انگلستان):** پوشش کامل ماستری | [chevening.org](https://chevening.org)")
            st.success("**2. Erasmus Mundus (اروپا):** تحصیل در چند کشور اروپایی | [eacea.ec.europa.eu](https://europa.eu)")
            st.success("**3. DAAD (آلمان):** بورسیه‌های ماستری و تحقیقاتی | [daad.de](https://daad.de)")
            st.success("**4. Fulbright (آمریکا):** بورسیه کامل ماستری در آمریکا | [fulbrightonline.org](https://fulbrightonline.org)")
            st.success("**5. Australia Awards (استرالیا):** بورسیه کامل ماستری | [dfat.gov.au](https://dfat.gov.au)")
        if lvl.startswith("3."):
            st.info("**1. University of the People:** دانشگاه آنلاین رایگان آمریکایی | [uopeople.edu](https://uopeople.edu)")
            st.info("**2. Coursera Financial Aid:** کورس‌های رایگان Google و Meta | [coursera.org](https://coursera.org)")
            st.info("**3. edX Financial Aid:** کورس‌های Harvard و MIT | [edx.org](https://edx.org)")
            st.info("**4. Saylor Academy:** کورس‌های دانشگاهی رایگان | [saylor.org](https://saylor.org)")
    if sch.startswith("2."):
        st.checkbox("1. پاسپورت معتبر یا تذکره الکترونیکی")
        st.checkbox("2. شهادت‌نامه و نمرات سه‌ساله با مهر وزارت خارجه")
        st.checkbox("3. ترجمه رسمی انگلیسی مدارک تحصیلی")
        st.checkbox("4. دیپلم و ترانسکریپت لیسانس (برای ماستری)")
        st.checkbox("5. انگیزه‌نامه اختصاصی (Motivation Letter)")
        st.checkbox("6. دو توصیه‌نامه از استادان")
        st.checkbox("7. رزومه تحصیلی استاندارد (Academic CV)")
        st.checkbox("8. مدرک زبان (Duolingo / IELTS / TOEFL)")
        st.checkbox("9. گواهی فعالیت‌های داوطلبانه و پروژه‌ها")
        st.checkbox("10. اسکن باکیفیت و ذخیره در Google Drive")
    if sch.startswith("3."):
        field = st.text_input("رشته تحصیلی (مثلاً: Computer Science):")
        country = st.text_input("کشور یا بورسیه (مثلاً: Turkey Burslari):")
        if st.button("✍️ نوشتن نمونه انگیزه‌نامه", key="sop_btn"):
            if field.strip() != "" and country.strip() != "":
                with st.spinner("در حال نوشتن انگیزه‌نامه..."):
                    sop = ask_openrouter(f"Write a strong 400-word scholarship Motivation Letter in English for an Afghan student applying for {field} in {country}.")
                    if sop != "": st.success(sop)
                    if sop == "": st.warning("سرور شلوغ است، چند ثانیه بعد دوباره بزنید.")

with tab3:
    st.subheader("📚 Comprehensive English Academy")
    eng = st.radio("بخش مورد نظر:", [
        "1. بانک لغات سطح‌بندی‌شده (24 لغت)",
        "2. تولید نامحدود درس جدید (AI Lessons)",
        "3. گرامر جامع زمان‌ها (Grammar)",
        "4. مکالمات کاربردی (Conversations)",
        "5. آزمون ۸ سوالی + تولید آزمون جدید"
    ])
    if eng.startswith("1."):
        lv = st.selectbox("سطح لغات:", ["Level 1: Beginner", "Level 2: Intermediate", "Level 3: Advanced"])
        if lv == "Level 1: Beginner":
            st.markdown("| Word | معنی | Example |\n| :--- | :--- | :--- |\n| **Improve** | پیشرفت کردن | *I want to improve my English.* |\n| **Future** | آینده | *Education builds a bright future.* |\n| **Goal** | هدف | *My goal is computer science.* |\n| **Practice** | تمرین کردن | *Practice makes you better.* |\n| **Support** | حمایت کردن | *We support each other.* |\n| **Confident** | با اعتماد به نفس | *Speak English and feel confident.* |\n| **Skill** | مهارت | *Coding is a modern skill.* |\n| **Success** | موفقیت | *Hard work leads to success.* |")
        if lv == "Level 2: Intermediate":
            st.markdown("| Word | معنی | Example |\n| :--- | :--- | :--- |\n| **Resilient** | مقاوم، تاب‌آور | *Afghan students are resilient.* |\n| **Opportunity** | فرصت | *Scholarships create opportunities.* |\n| **Achieve** | به دست آوردن | *You can achieve your dreams.* |\n| **Determine** | مصمم بودن | *She is determined to succeed.* |\n| **Perseverance** | پشتکار | *Perseverance overcomes obstacles.* |\n| **Fluently** | روان و سلیس | *She speaks English fluently.* |\n| **Independent** | مستقل | *Self-learning makes you independent.* |\n| **Overcome** | غلبه کردن | *We can overcome any difficulty.* |")
        if lv == "Level 3: Advanced":
            st.markdown("| Word | معنی | Example |\n| :--- | :--- | :--- |\n| **Endeavor** | تلاش جدی | *Academic endeavor needs discipline.* |\n| **Proficiency** | تسلط بالا | *English proficiency is essential.* |\n| **Empower** | توانمند ساختن | *Technology empowers learners.* |\n| **Dedication** | فداکاری و تعهد | *Her dedication is inspiring.* |\n| **Aspiration** | آرزوی بزرگ | *My aspiration is to innovate.* |\n| **Comprehend** | درک کردن | *Read carefully to comprehend.* |\n| **Collaborate** | همکاری کردن | *Students collaborate globally.* |\n| **Breakthrough** | پیشرفت بزرگ | *AI is a major breakthrough.* |")
    if eng.startswith("2."):
        tc = st.selectbox("موضوع درس جدید:", [
            "Job & Scholarship Interview",
            "Technology & Artificial Intelligence",
            "University & Academic Life",
            "Travel & Airport",
            "Business & Entrepreneurship"
        ])
        if st.button("📚 ساخت درس جدید نامحدود", key="gen_eng"):
            with st.spinner("در حال ساخت درس جدید..."):
                lr = ask_openrouter(f"Create a rich English lesson about '{tc}' for Persian speakers with 10 vocabulary words (with Persian meanings and examples) and a 6-line dialogue with Persian translation.")
                if lr != "": st.success(lr)
