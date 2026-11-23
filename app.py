import streamlit as st
import requests
import math

st.set_page_config(page_title="RahaPath - Empowering Education", page_icon="🎓", layout="centered")

st.markdown("""
<style>
    .main-banner {
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
        padding: 22px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 18px;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3);
    }
    .main-banner h1 {
        margin: 0;
        font-size: 2.1rem;
        color: white;
    }
    .main-banner p {
        margin: 6px 0 0 0;
        font-size: 1rem;
        opacity: 0.95;
    }
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        width: 100%;
    }
</style>
<div class="main-banner">
    <h1>🎓 RahaPath</h1>
    <p>Empowering Afghan Students through AI & Education</p>
    <p style="font-size: 0.9rem; margin-top: 4px;">مسیر رهایی، خودآموزی و پیشرفت آموزشی</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🤖 AI Assistant",
    "🌍 Scholarships",
    "📚 English",
    "📅 Planner",
    "🧮 Solver"
])

with tab1:
    st.subheader("🤖 AI Study Assistant")
    st.write("هر سوال درسی، انگلیسی، برنامه‌نویسی یا عمومی دارید به فارسی یا انگلیسی بپرسید:")
    question = st.text_area("سوال خود را بنویسید (Type your question here):", height=90)
    if st.button("✨ Ask AI (دریافت پاسخ)", key="ai_btn"):
        if question.strip() == "":
            st.warning("لطفاً اول یک سوال بنویسید! (Please type a question first)")
        if question.strip() != "":
            with st.spinner("در حال فکر کردن و نوشتن پاسخ... (Thinking...)"):
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
                                {"role": "system", "content": "You are RahaPath AI, a helpful and encouraging educational assistant for Afghan students. Answer clearly, accurately, and thoroughly in the same language the user asks."},
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
    st.subheader("🌍 Scholarship Finder & Guide")
    sch_section = st.radio("بخش مورد نظر را انتخاب کنید:", [
        "1. Scholarship List (لیست بورسیه‌ها)",
        "2. Document Checklist (چک‌لیست مدارک)",
        "3. Motivation Letter Guide (راهنمای انگیزه‌نامه)"
    ])

    if sch_section.startswith("1."):
        level = st.selectbox("مقطع تحصیلی (Select Study Level):", [
            "1. Bachelor (لیسانس)",
            "2. Master (ماستری)",
            "3. Online Free Universities (دانشگاه‌های آنلاین رایگان)"
        ])

        if level.startswith("1."):
            st.success("**1. Türkiye Burslari (بورسیه دولت ترکیه)**\n- **مزایا:** شهریه کامل، خوابگاه، کمک‌هزینه ماهانه، بیمه و بلیت پرواز.\n- **شرایط:** دیپلم مکتب با معدل بالای ۷۰٪.\n- **سایت رسمی:** [turkiyeburslari.gov.tr](https://turkiyeburslari.gov.tr)")
            st.success("**2. DAAD Scholarships (بورسیه آلمان)**\n- **مزایا:** کمک‌هزینه ماهانه و بیمه درمانی.\n- **سایت رسمی:** [daad.de](https://daad.de)")
            st.success("**3. Romanian Government Scholarship (بورسیه رومانی)**\n- **مزایا:** تحصیل رایگان، خوابگاه و کمک‌هزینه ماهانه.\n- **سایت رسمی:** [scholarships.studyinromania.gov.ro](https://studyinromania.gov.ro)")

        if level.startswith("2."):
            st.success("**1. Chevening Scholarship (بورسیه انگلستان)**\n- **مزایا:** پوشش کامل شهریه، هزینه زندگی و پرواز.\n- **شرایط:** مدرک لیسانس + ۲ سال سابقه کار یا فعالیت داوطلبانه.\n- **سایت رسمی:** [chevening.org](https://chevening.org)")
            st.success("**2. Erasmus Mundus (بورسیه اروپا)**\n- **مزایا:** تحصیل در ۲ تا ۳ کشور اروپایی با بورسیه کامل.\n- **سایت رسمی:** [eacea.ec.europa.eu](https://europa.eu)")
            st.success("**3. Fulbright Program (فولبرایت آمریکا)**\n- **مزایا:** بورسیه کامل مقطع ماستری در آمریکا.\n- **سایت رسمی:** [foreign.fulbrightonline.org](https://fulbrightonline.org)")

        if level.startswith("3."):
            st.info("**1. University of the People (UoPeople)**\n- دانشگاه آنلاین معتبر آمریکایی، کاملاً بدون شهریه در رشته‌های کمپیوتر ساینس و مدیریت.\n- **سایت رسمی:** [uopeople.edu](https://uopeople.edu)")
            st.info("**2. Coursera Financial Aid**\n- دریافت گواهینامه‌های رایگان از گوگل، متا و دانشگاه‌های برتر دنیا.\n- **سایت رسمی:** [coursera.org](https://coursera.org)")

    if sch_section.startswith("2."):
        st.write("**مدارک ضروری برای اپلای بورسیه را آماده و تیک بزنید:**")
        st.checkbox("1. پاسپورت معتبر یا تذکره الکترونیکی (Valid Passport / Tazkira)")
        st.checkbox("2. شهادت‌نامه و نمرات سه‌ساله با ترجمه انگلیسی (Diploma & Transcripts)")
        st.checkbox("3. انگیزه‌نامه قوی و اختصاصی (Motivation Letter / SOP)")
        st.checkbox("4. دو توصیه‌نامه از استادان یا معلمان (Two Recommendation Letters)")
        st.checkbox("5. مدرک زبان انگلیسی مانند Duolingo یا IELTS")
        st.checkbox("6. رزومه تحصیلی و فعالیت‌های داوطلبانه (Academic CV)")
        st.info("💡 تمام مدارک را با کیفیت بالا اسکن (PDF) کنید و در یک پوشه در Google Drive نگه دارید.")

    if sch_section.startswith("3."):
        st.write("یک انگیزه‌نامه استاندارد باید حدود **۵۰۰ تا ۷۰۰ کلمه** و شامل ۴ پاراگراف باشد:")
        st.success("**پاراگراف ۱ (معرفی):** خودتان را معرفی کنید، بگویید به چه رشته‌ای علاقه دارید و هدف اصلی شما چیست.")
        st.success("**پاراگراف ۲ (سوابق و پشتکار):** درباره دستاوردهای درسی و مهارت‌هایی که خودتان یاد گرفته‌اید (مثل انگلیسی یا کدنویسی) بنویسید.")
        st.success("**پاراگراف ۳ (چرا این بورسیه):** توضیح دهید چرا این کشور و رشته را انتخاب کرده‌اید.")
        st.success("**پاراگراف ۴ (اهداف آینده):** بگویید پس از فارغ‌التحصیلی چطور به جامعه و پیشرفت دیگران کمک خواهید کرد.")

with tab3:
    st.subheader("📚 English Learning Hub")
    eng_section = st.radio("بخش مورد نظر را انتخاب کنید:", [
        "1. Vocabulary (لغات مهم)",
        "2. Conversation (مکالمه روزمره)",
        "3. Grammar (گرامر کاربردی)",
        "4. Quiz (آزمون ۵ سوالی)"
    ])

    if eng_section.startswith("1."):
        st.markdown("| English Word | معنی فارسی | Example Sentence |\n| :--- | :--- | :--- |\n| **Resilient** | مقاوم، تاب‌آور | *Afghan students are strong and resilient.* |\n| **Opportunity** | فرصت | *Education creates new opportunities.* |\n| **Achieve** | به دست آوردن، موفق شدن | *You can achieve all your dreams.* |\n| **Determine** | مصمم بودن | *She is determined to learn coding.* |\n| **Knowledge** | دانش، علم | *Knowledge is power that no one can take.* |\n| **Perseverance** | پشتکار، استقامت | *Success comes through daily perseverance.* |\n| **Fluently** | روان و سلیس | *I want to speak English fluently.* |\n| **Independent** | مستقل | *Learning skills makes you independent.* |")

    if eng_section.startswith("2."):
        st.info("**1. معرفی خود (Introducing Yourself):**\n- *Hello! My name is Rayhana, and I am passionate about technology.*\n- سلام! نام من ریحانه است و به تکنولوژی علاقه‌مند هستم.")
        st.info("**2. صحبت درباره اهداف (Talking About Goals):**\n- *I am studying hard to win an international scholarship.*\n- من سخت درس می‌خوانم تا یک بورسیه بین‌المللی به دست بیاورم.")
        st.info("**3. درخواست کمک درسی (Asking for Help):**\n- *Could you please explain this topic in simple words?*\n- آیا می‌توانید لطفاً این موضوع را با کلمات ساده توضیح دهید؟")
        st.info("**4. انگیزه دادن به دوستان (Encouraging Friends):**\n- *Never give up! Every small step brings us closer to success.*\n- هرگز تسلیم نشو! هر قدم کوچک ما را به موفقیت نزدیک‌تر می‌کند.")

    if eng_section.startswith("3."):
        st.write("**Simple Present Tense (زمان حال ساده):** برای بیان عادت‌های روزمره و حقایق علمی استفاده می‌شود.")
        st.success("**فرمول مثبت:**\n- **I / You / We / They** + فعل ساده (*We **study** English every day.*)\n- **He / She / It** + فعل + **s / es** (*She **codes** every evening.*)")
