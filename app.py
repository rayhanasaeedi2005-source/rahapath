with tab4:
    st.subheader("📅 Smart Study Planner")
    st.info("⏱️ **قانون تمرکز پومودورو:** ۲۵ دقیقه مطالعه عمیق + ۵ دقیقه استراحت.")

    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    new_task = st.text_input("هدف درسی امروز را بنویسید (مثلاً: خواندن ۱۰ لغت جدید):")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ افزودن هدف", key="task_btn") and new_task.strip() != "":
            st.session_state.tasks.append(new_task.strip())
            st.success("اضافه شد!")
    with col2:
        if st.button("🗑️ پاک کردن لیست", key="clear_btn"):
            st.session_state.tasks = []
            st.info("لیست پاک شد!")

    st.write("**پیشرفت امروز شما:**")
    if len(st.session_state.tasks) == 0:
        st.write("هنوز هدفی اضافه نکرده‌اید. اولین هدف درسی امروزتان را بالا بنویسید!")
    if len(st.session_state.tasks) > 0:
        completed = 0
        for idx, t in enumerate(st.session_state.tasks):
            if st.checkbox(t, key=f"task_{idx}"):
                completed = completed + 1
        progress = completed / len(st.session_state.tasks)
        st.progress(progress)
        st.write(f"**انجام شده:** {completed} از {len(st.session_state.tasks)} هدف ({int(progress * 100)}%)")

with tab5:
    st.subheader("🧮 Smart Problem Solver")
    tool = st.selectbox("ابزار مورد نظر را انتخاب کنید:", [
        "1. Grade Calculator (محاسبه فیصدی نمرات)",
        "2. Scientific Calculator (ماشین‌حساب علمی)",
        "3. Unit Converter (تبدیل واحدها)"
    ])

    if tool.startswith("1."):
        scores_input = st.text_input("نمرات را با کاما جدا کنید (مثلاً: 85, 90, 95):")
        if st.button("محاسبه فیصدی", key="calc_btn") and scores_input.strip() != "":
            try:
                scores = [float(x.strip()) for x in scores_input.split(",")]
                avg = sum(scores) / len(scores)
                st.metric("فیصدی کل (Average)", f"{avg:.2f}%")
                if avg >= 85:
                    st.success("درجه: A (ممتاز! عالی بود) 🌟")
                if avg >= 70 and avg < 85:
                    st.success("درجه: B (بسیار خوب) 🎉")
                if avg >= 55 and avg < 70:
                    st.info("درجه: C (کامیاب) 👍")
                if avg < 55:
                    st.warning("نیاز به تلاش بیشتر دارید. ادامه دهید! 💪")
            except Exception:
                st.error("لطفاً اعداد معتبر وارد کنید (مثال: 80, 90, 85).")

    if tool.startswith("2."):
        num1 = st.number_input("عدد اول:", value=0.0)
        op = st.selectbox("عملیات:", [
            "+ (جمع)",
            "- (تفریق)",
            "* (ضرب)",
            "/ (تقسیم)",
            "^ (توان)",
            "sqrt (جذر مربع عدد اول)"
        ])
        num2 = st.number_input("عدد دوم:", value=0.0)
        if st.button("محاسبه", key="math_btn"):
            if op.startswith("+"):
                st.success(f"نتیجه: {num1 + num2}")
            if op.startswith("-"):
                st.success(f"نتیجه: {num1 - num2}")
            if op.startswith("*"):
                st.success(f"نتیجه: {num1 * num2}")
            if op.startswith("/") and num2 != 0:
                st.success(f"نتیجه: {num1 / num2}")
            if op.startswith("/") and num2 == 0:
                st.error("تقسیم بر صفر ممکن نیست!")
            if op.startswith("^"):
                st.success(f"نتیجه: {num1 ** num2}")
            if op.startswith("sqrt"):
                if num1 >= 0:
                    st.success(f"نتیجه: {math.sqrt(num1):.4f}")
                if num1 < 0:
                    st.error("جذر عدد منفی تعریف نشده است!")

    if tool.startswith("3."):
        conv_type = st.radio("نوع تبدیل:", [
            "1. Celsius to Fahrenheit (سانتی‌گراد به فارنهایت)",
            "2. Kilometers to Miles (کیلومتر به مایل)",
            "3. Hours to Minutes (ساعت به دقیقه)"
        ])
        val = st.number_input("مقدار را وارد کنید:", value=1.0)
        if st.button("تبدیل کن", key="conv_btn"):
            if conv_type.startswith("1."):
                st.success(f"{val} °C = {(val * 9/5) + 32:.2f} °F")
            if conv_type.startswith("2."):
                st.success(f"{val} km = {val * 0.621371:.2f} miles")
            if conv_type.startswith("3."):
                st.success(f"{val} ساعت = {val * 60:.0f} دقیقه")

st.markdown("---")
st.caption("Built with ❤️ by Rayhana | RahaPath Educational Platform (2026)")
