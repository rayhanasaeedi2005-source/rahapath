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
    <p>Empowering Afghan Students through AI & Education</p>
    <p>مسیر رهایی، خودآموزی و پیشرفت آموزشی</p>
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
    question = st.text_area("سوال درسی یا عمومی خود را به فارسی یا انگلیسی بنویسید:", height=90)
    if st.button("✨ Ask AI", key="ai_btn"):
        if question.strip() == "":
            st.warning("لطفاً اول یک سوال بنویسید!")
        if question.strip() != "":
            with st.spinner("در حال نوشتن پاسخ..."):
                answered = False
                api_key = st.secrets.get("OPENROUTER_API_KEY", "").strip()
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://streamlit.app",
                    "X-Title": "RahaPath"
                }
                models = ["openrouter/free", "meta-llama/llama-3.3-70b-instruct:free", "google/gemma-3-27b-it:free"]
                for m in models:
                    if answered:
                        break
                    try:
                        data = {
                            "model": m,
                            "messages": [
                                {"role": "system", "content": "You are RahaPath AI, a helpful educational assistant for Afghan students. Answer clearly and thoroughly in the same language the user asks."},
                                {"role": "user", "content": question}
                            ]
                        }
                        res = requests.post("https://openrouter.ai", headers=headers, json=data, timeout=20)
                        if res.status_code == 200:
                            for item in res.json().get("choices", []):
                                text = item.get("message", {}).get("content", "").strip()
                                if text != "":
                                    st.success(text)
                                    answered = True
                                    break
                    except Exception:
                        continue
                if not answered:
                    st.warning("سرور شلوغ است، لطفاً ۵ ثانیه بعد دوباره دکمه Ask AI را بزنید.")

with tab2:
    st.subheader("🌍 Scholarship Finder & Guide")
    sch = st.radio("بخش مورد نظر:", ["1. لیست بورسیه‌ها", "2. چک‌لیست مدارک", "3. راهنمای انگیزه‌نامه"])
    if sch.startswith("1."):
        lvl = st.selectbox("مقطع تحصیلی:", ["Bachelor (لیسانس)", "Master (ماستری)", "Online Free Universities"])
        if lvl == "Bachelor (لیسانس)":
            st.success("**1. Türkiye Burslari (ترکیه):** شهریه کامل، خوابگاه و کمک‌هزینه | [turkiyeburslari.gov.tr](https://turkiyeburslari.gov.tr)")
            st.success("**2. DAAD (آلمان):** کمک‌هزینه ماهانه و بیمه | [daad.de](https://daad.de)")
            st.success("**3. Romanian Scholarship (رومانی):** تحصیل و خوابگاه رایگان | [studyinromania.gov.ro](https://studyinromania.gov.ro)")
        if lvl == "Master (ماستری)":
            st.success("**1. Chevening (انگلستان):** پوشش کامل هزینه‌ها | [chevening.org](https://chevening.org)")
            st.success("**2. Erasmus Mundus (اروپا):** تحصیل در چند کشور اروپایی | [eacea.ec.europa.eu](https://europa.eu)")
            st.success("**3. Fulbright (آمریکا):** بورسیه کامل ماستری | [fulbrightonline.org](https://fulbrightonline.org)")
        if lvl == "Online Free Universities":
            st.info("**1. University of the People:** دانشگاه آنلاین رایگان آمریکایی | [uopeople.edu](https://uopeople.edu)")
            st.info("**2. Coursera Financial Aid:** کورس‌های رایگان دانشگاه‌های برتر | [coursera.org](https://coursera.org)")
    if sch.startswith("2."):
        st.checkbox("1. پاسپورت معتبر یا تذکره الکترونیکی")
        st.checkbox("2. شهادت‌نامه و نمرات سه‌ساله با ترجمه انگلیسی")
        st.checkbox("3. انگیزه‌نامه قوی (Motivation Letter)")
        st.checkbox("4. دو توصیه‌نامه از استادان")
        st.checkbox("5. مدرک زبان انگلیسی (Duolingo / IELTS)")
    if sch.startswith("3."):
        st.success("**پاراگراف ۱:** معرفی خود و علاقه به رشته.\n\n**پاراگراف ۲:** دستاوردهای درسی و مهارت‌های خودآموز.\n\n**پاراگراف ۳:** دلیل انتخاب دانشگاه و کشور مقصد.\n\n**پاراگراف ۴:** اهداف آینده و کمک به جامعه.")

with tab3:
    st.subheader("📚 English Learning Hub")
    eng = st.radio("بخش مورد نظر:", ["1. لغات مهم", "2. مکالمه روزمره", "3. گرامر کاربردی", "4. آزمون ۵ سوالی"])
    if eng.startswith("1."):
        st.markdown("| Word | معنی | Example |\n| :--- | :--- | :--- |\n| **Resilient** | مقاوم، تاب‌آور | *Afghan students are resilient.* |\n| **Opportunity** | فرصت | *Education creates opportunities.* |\n| **Achieve** | موفق شدن | *You can achieve your dreams.* |\n| **Perseverance** | پشتکار | *Success needs perseverance.* |\n| **Fluently** | روان و سلیس | *I speak English fluently.* |")
    if eng.startswith("2."):
        st.info("**Introducing Yourself:** *Hello! My name is Rayhana, and I love technology.*\n(سلام! نام من ریحانه است و به تکنولوژی علاقه دارم.)")
        st.info("**Goals:** *I am studying hard to win a scholarship.*\n(من سخت درس می‌خوانم تا بورسیه بگیرم.)")
        st.info("**Motivation:** *Never give up! Every small step matters.*\n(هرگز تسلیم نشو! هر قدم کوچک مهم است.)")
    if eng.startswith("3."):
        st.success("**Simple Present (حال ساده):**\n- **I / You / We / They** + فعل ساده (*We **study** every day.*)\n- **He / She / It** + فعل + **s/es** (*She **codes** every night.*)")
    if eng.startswith("4."):
        q1 = st.radio("1. Synonym of 'Resilient'?", ["Weak", "Strong", "Tired"], key="q1")
        q2 = st.radio("2. Meaning of 'Perseverance'?", ["پشتکار", "مانع", "اشتباه"], key="q2")
        q3 = st.radio("3. 'She ____ Python daily.'", ["learn", "learns", "learning"], key="q3")
        q4 = st.radio("4. 'We ____ give up.'", ["doesn't", "don't", "isn't"], key="q4")
        q5 = st.radio("5. Meaning of 'Fluently'?", ["آهسته", "روان و سلیس", "ساکت"], key="q5")
        if st.button("✅ ثبت آزمون", key="quiz_btn"):
            score = sum([q1 == "Strong", q2 == "پشتکار", q3 == "learns", q4 == "don't", q5 == "روان و سلیس"])
            st.metric("نمره شما", f"{score} / 5")
            if score == 5:
                st.success("🎉 عالی! ۵ از ۵!")
            if score < 5:
                st.info("👍 خوب بود! درس‌ها را مرور کنید و دوباره امتحان دهید.")

with tab4:
    st.subheader("📅 Smart Study Planner")
    st.info("⏱️ **قانون پومودورو:** ۲۵ دقیقه مطالعه عمیق + ۵ دقیقه استراحت")
    if "tasks" not in st.session_state:
        st.session_state.tasks = []
    new_task = st.text_input("هدف درسی امروز را بنویسید:")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("➕ افزودن", key="add_t") and new_task.strip() != "":
            st.session_state.tasks.append(new_task.strip())
    with c2:
        if st.button("🗑️ پاک کردن", key="clr_t"):
            st.session_state.tasks = []
    if len(st.session_state.tasks) > 0:
        done = sum([st.checkbox(t, key=f"t_{i}") for i, t in enumerate(st.session_state.tasks)])
        st.progress(done / len(st.session_state.tasks))
        st.write(f"انجام شده: {done} از {len(st.session_state.tasks)}")

with tab5:
    st.subheader("🧮 Smart Problem Solver")
    tool = st.selectbox("انتخاب ابزار:", ["1. محاسبه فیصدی نمرات", "2. ماشین‌حساب علمی", "3. تبدیل واحدها"])
    if tool.startswith("1."):
        s_in = st.text_input("نمرات را با کاما جدا کنید (مثلاً: 85, 90, 95):")
        if st.button("محاسبه فیصدی", key="c_btn") and s_in.strip() != "":
            try:
                sc = [float(x.strip()) for x in s_in.split(",")]
                avg = sum(sc) / len(sc)
                st.metric("فیصدی کل", f"{avg:.2f}%")
                if avg >= 55:
                    st.success("وضعیت: کامیاب! آفرین 🎉")
                if avg < 55:
                    st.warning("نیاز به تلاش بیشتر 💪")
            except Exception:
                st.error("لطفاً اعداد را با کاما وارد کنید.")
    if tool.startswith("2."):
        n1 = st.number_input("عدد اول:", value=0.0)
        op = st.selectbox("عملیات:", ["+", "-", "*", "/", "^ (توان)", "sqrt (جذر)"])
        n2 = st.number_input("عدد دوم:", value=0.0)
        if st.button("محاسبه", key="m_btn"):
            if op == "+": st.success(f"نتیجه: {n1 + n2}")
            if op == "-": st.success(f"نتیجه: {n1 - n2}")
            if op == "*": st.success(f"نتیجه: {n1 * n2}")
            if op == "/" and n2 != 0: st.success(f"نتیجه: {n1 / n2}")
            if op == "/" and n2 == 0: st.error("تقسیم بر صفر ممکن نیست!")
            if op.startswith("^"): st.success(f"نتیجه: {n1 ** n2}")
            if op.startswith("sqrt"): st.success(f"نتیجه: {math.sqrt(n1):.4f}" if n1 >= 0 else "عدد منفی مجاز نیست!")
    if tool.startswith("3."):
        ct = st.radio("تبدیل:", ["1. سانتی‌گراد به فارنهایت", "2. کیلومتر به مایل", "3. ساعت به دقیقه"])
        v = st.number_input("مقدار:", value=1.0)
