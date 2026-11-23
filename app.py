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

def ask_openrouter(prompt_text, sys_role="You are RahaPath AI, a helpful educational assistant for Afghan students. Answer clearly, accurately, and thoroughly in the same language the user asks."):
    api_key = st.secrets.get("OPENROUTER_API_KEY", "").strip()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://streamlit.app",
        "X-Title": "RahaPath"
    }
    models = [
        "openrouter/free",
        "meta-llama/llama-3.3-70b-instruct:free",
        "google/gemma-3-27b-it:free",
        "mistralai/mistral-small-3.1-24b-instruct:free"
    ]
    for m in models:
        try:
            data = {
                "model": m,
                "messages": [
                    {"role": "system", "content": sys_role},
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
    mode = st.selectbox("حالت دستیار (Select Mode):", [
        "1. پرسش و پاسخ عمومی و درسی (General & Study Q&A)",
        "2. ترجمه و اصلاح گرامر متن انگلیسی (Translator & Grammar Fixer)",
        "3. توضیح ساده موضوعات سخت علمی (Explain Like I'm 15)"
    ])
    question = st.text_area("متن یا سوال خود را بنویسید (به فارسی یا انگلیسی):", height=100)
    if st.button("✨ دریافت پاسخ (Ask AI)", key="ai_btn"):
        if question.strip() == "":
            st.warning("لطفاً اول سوال یا متن خود را بنویسید!")
        if question.strip() != "":
            with st.spinner("در حال پردازش پاسخ..."):
                final_prompt = question
                if mode.startswith("2."):
                    final_prompt = f"Translate this between Persian and English, and if it is English, correct any grammar mistakes and explain them clearly: {question}"
                if mode.startswith("3."):
                    final_prompt = f"Explain this concept in very simple, clear, step-by-step terms with examples in the same language: {question}"
                ans = ask_openrouter(final_prompt)
                if ans != "":
                    st.success(ans)
                if ans == "":
                    st.warning("سرورهای رایگان شلوغ هستند، لطفاً ۵ ثانیه صبر کنید و دوباره بزنید.")

with tab2:
    st.subheader("🌍 Global Scholarships & Apply Hub")
    sch = st.radio("بخش مورد نظر:", [
        "1. بانک جامع بورسیه‌ها (Scholarship Database)",
        "2. چک‌لیست کامل مدارک (10-Step Checklist)",
        "3. نگارش هوشمند انگیزه‌نامه (AI Motivation Letter)"
    ])
    if sch.startswith("1."):
        lvl = st.selectbox("مقطع یا نوع بورسیه:", [
            "1. Bachelor (لیسانس - آسیا و اروپا)",
            "2. Master & PhD (ماستری و دکترا)",
            "3. Free Online Degrees & Certificates (تحصیل آنلاین رایگان)"
        ])
        if lvl.startswith("1."):
            st.success("**1. Türkiye Burslari (ترکیه):** شهریه کامل، خوابگاه، کمک‌هزینه ماهانه، بیمه و پرواز | [turkiyeburslari.gov.tr](https://turkiyeburslari.gov.tr)")
            st.success("**2. Stipendium Hungaricum (مجارستان):** تحصیل رایگان، خوابگاه و کمک‌هزینه زندگی در اروپا | [stipendiumhungaricum.hu](https://stipendiumhungaricum.hu)")
            st.success("**3. MEXT Scholarship (جاپان):** بورسیه کامل دولت جاپان برای مقطع لیسانس | [studyinjapan.go.jp](https://studyinjapan.go.jp)")
            st.success("**4. GKS - Global Korea Scholarship (کوریای جنوبی):** پوشش کامل شهریه، زبان کوریایی و زندگی | [studyinkorea.go.kr](https://studyinkorea.go.kr)")
            st.success("**5. Romanian Government Scholarship (رومانی):** تحصیل رایگان و کمک‌هزینه ماهانه | [studyinromania.gov.ro](https://studyinromania.gov.ro)")
        if lvl.startswith("2."):
            st.success("**1. Chevening Scholarship (انگلستان):** پوشش کامل شهریه، پرواز و هزینه زندگی | [chevening.org](https://chevening.org)")
            st.success("**2. Erasmus Mundus (اتحادیه اروپا):** تحصیل مشترک در ۲ تا ۳ کشور اروپایی با بورسیه کامل | [eacea.ec.europa.eu](https://europa.eu)")
            st.success("**3. DAAD Scholarships (آلمان):** بورسیه‌های متنوع ماستری و تحقیقاتی | [daad.de](https://daad.de)")
            st.success("**4. Fulbright Program (آمریکا):** بورسیه کامل مقطع ماستری در دانشگاه‌های آمریکا | [foreign.fulbrightonline.org](https://fulbrightonline.org)")
            st.success("**5. Australia Awards (استرالیا):** بورسیه کامل توسعه و ماستری | [dfat.gov.au](https://dfat.gov.au)")
        if lvl.startswith("3."):
            st.info("**1. University of the People (UoPeople):** دانشگاه آنلاین آمریکایی بدون شهریه در کمپیوتر ساینس و مدیریت | [uopeople.edu](https://uopeople.edu)")
            st.info("**2. Coursera Financial Aid:** دریافت رایگان گواهینامه‌های Google, Meta و دانشگاه‌های برتر | [coursera.org](https://coursera.org)")
            st.info("**3. edX Financial Assistance:** تخفیف تا ۹۰٪ یا کورس‌های رایگان از Harvard و MIT | [edx.org](https://edx.org)")
            st.info("**4. Saylor Academy:** کورس‌های دانشگاهی کاملاً رایگان با گواهینامه | [saylor.org](https://saylor.org)")

    if sch.startswith("2."):
        st.write("**چک‌لیست ۱۰ مرحله‌ای آماده‌سازی مدارک بورسیه:**")
        st.checkbox("1. پاسپورت معتبر یا تذکره الکترونیکی")
        st.checkbox("2. شهادت‌نامه مکتب و نمرات سه‌ساله با مهر وزارت خارجه")
        st.checkbox("3. ترجمه رسمی انگلیسی تمام مدارک تحصیلی")
        st.checkbox("4. دیپلم و ترانسکریپت لیسانس (برای متقاضیان ماستری)")
        st.checkbox("5. انگیزه‌نامه اختصاصی (Motivation Letter / SOP)")
        st.checkbox("6. دو توصیه‌نامه رسمی از استادان (Recommendation Letters)")
        st.checkbox("7. رزومه تحصیلی استاندارد (Academic CV)")
        st.checkbox("8. مدرک زبان انگلیسی (Duolingo English Test / IELTS / TOEFL)")
        st.checkbox("9. گواهی فعالیت‌های داوطلبانه، اجتماعی یا پروژه‌ها (مثل ساخت RahaPath!)")
        st.checkbox("10. اسکن باکیفیت و ذخیره در Google Drive")

    if sch.startswith("3."):
        st.write("**مولد هوشمند انگیزه‌نامه (AI Motivation Letter):**")
        field = st.text_input("رشته تحصیلی مورد نظر (مثلاً: Computer Science):")
        country = st.text_input("کشور یا بورسیه مقصد (مثلاً: Turkey Burslari):")
        if st.button("✍️ نوشتن نمونه انگیزه‌نامه", key="sop_btn"):
            if field.strip() == "" or country.strip() == "":
                st.warning("لطفاً رشته و کشور مقصد را وارد کنید.")
            if field.strip() != "" and country.strip() != "":
                with st.spinner("در حال نوشتن انگیزه‌نامه حرفه‌ای..."):
                    sop_prompt = f"Write a strong, inspiring 400-word scholarship Motivation Letter in English for an Afghan student applying for {field} in {country}. Highlight resilience, self-learning, and future contribution."
                    sop_res = ask_openrouter(sop_prompt)
                    if sop_res != "":
                        st.success(sop_res)
                    if sop_res == "":
                        st.warning("سرور شلوغ است، چند ثانیه بعد دوباره تلاش کنید.")

with tab3:
    st.subheader("📚 Comprehensive English Academy")
    eng = st.radio("بخش مورد نظر را انتخاب کنید:", [
        "1. بانک لغات سطح‌بندی‌شده (24+ Vocabulary)",
        "2. تولید نامحدود درس و لغت جدید (AI Unlimited Lessons)",
        "3. گرامر جامع زمان‌ها (Complete Grammar)",
        "4. مکالمات کاربردی (Real Conversations)",
        "5. آزمون ۸ سوالی + تولید آزمون جدید (Quiz)"
    ])

    if eng.startswith("1."):
        lvl_v = st.selectbox("سطح لغات را انتخاب کنید:", [
            "Level 1: Beginner (مبتدی - ۸ لغت)",
            "Level 2: Intermediate (متوسط - ۸ لغت)",
            "Level 3: Advanced & Academic (پیشرفته و دانشگاهی - ۸ لغت)"
        ])
        if lvl_v.startswith("Level 1"):
            st.markdown("| Word | معنی فارسی | Example |\n| :--- | :--- | :--- |\n| **Improve** | پیشرفت کردن | *I want to improve my English.* |\n| **Future** | آینده | *Education builds a bright future.* |\n| **Goal** | هدف | *My main goal is to study computer science.* |\n| **Practice** | تمرین کردن | *Practice makes you better every day.* |\n| **Support** | حمایت کردن | *We support each other in learning.* |\n| **Confident** | با اعتماد به نفس | *Speak English and feel confident.* |\n| **Skill** | مهارت | *Coding is a valuable modern skill.* |\n| **Success** | موفقیت | *Hard work leads to real success.* |")
        if lvl_v.startswith("Level 2"):
