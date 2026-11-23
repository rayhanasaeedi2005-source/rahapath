import streamlit as st
import math

def render_planner_and_solver(tab4, tab5, ask_ai_func):
    with tab4:
        st.subheader("📅 Study Planner | برنامه‌ریز درسی")
        st.info("⏱️ **Pomodoro:** 25 mins study + 5 mins break | ۲۵ دقیقه مطالعه + ۵ دقیقه استراحت")
        if "tasks" not in st.session_state:
            st.session_state.tasks = []
        nt = st.text_input("Study Goal / هدف درسی امروز:", key="nt4")
        if st.button("➕ Add Goal / افزودن", key="ba4") and nt.strip() != "":
            st.session_state.tasks.append(nt.strip())
        if st.button("🗑️ Clear All / پاک کردن", key="bc4"):
            st.session_state.tasks = []
        if len(st.session_state.tasks) > 0:
            done = sum([st.checkbox(t, key=f"tk_{i}") for i, t in enumerate(st.session_state.tasks)])
            st.progress(done / len(st.session_state.tasks))
            st.write(f"**Progress / پیشرفت:** {done} / {len(st.session_state.tasks)}")

    with tab5:
        st.subheader("🧮 Math & Smart Solver | ریاضی و حل‌کننده")
        tl = st.selectbox("Tool / ابزار:", ["1. AI Math Solver (حل مسائل ریاضی)", "2. Grade Calculator (محاسبه فیصدی)", "3. Scientific Calculator (ماشین‌حساب)", "4. Unit Converter (تبدیل واحد)"], key="tl5")
        if tl.startswith("1."):
            mq = st.text_area("Math/Physics Problem / سوال ریاضی:", height=80, key="mq5")
            if st.button("🧠 Solve / حل مسئله", key="bm5") and mq.strip() != "":
                ma = ask_ai_func(f"Solve this math or physics problem step-by-step clearly in the same language: {mq}")
                if ma != "": st.success(ma)
        if tl.startswith("2."):
            si = st.text_input("Scores / نمرات با کاما (85, 90, 95):", key="si5")
            if st.button("Calculate / محاسبه", key="bg5") and si.strip() != "":
                try:
                    sc = [float(x.strip()) for x in si.split(",")]
                    avg = sum(sc) / len(sc)
                    st.metric("Average / فیصدی", f"{avg:.2f}%")
                    st.success("Passed / کامیاب 🎉" if avg >= 55 else "Keep trying / تلاش بیشتر 💪")
                except Exception:
                    st.error("Enter valid numbers / اعداد معتبر وارد کنید.")
        if tl.startswith("3."):
            n1 = st.number_input("Number 1 / عدد اول:", value=0.0, key="n1_5")
            op = st.selectbox("Op / عملیات:", ["+", "-", "*", "/", "^", "sqrt"], key="op5")
            n2 = st.number_input("Number 2 / عدد دوم:", value=0.0, key="n2_5")
            if st.button("Calculate / محاسبه", key="bs5"):
                if op == "+": st.success(f"Result: {n1 + n2}")
                if op == "-": st.success(f"Result: {n1 - n2}")
                if op == "*": st.success(f"Result: {n1 * n2}")
                if op == "/" and n2 != 0: st.success(f"Result: {n1 / n2}")
                if op == "^": st.success(f"Result: {n1 ** n2}")
                if op == "sqrt": st.success(f"Result: {math.sqrt(n1):.4f}" if n1 >= 0 else "Invalid!")
        if tl.startswith("4."):
            ct = st.radio("Convert / تبدیل:", ["1. Celsius to Fahrenheit", "2. Km to Miles", "3. Hours to Minutes"], key="ct5")
            v = st.number_input("Value / مقدار:", value=1.0, key="v5")
            if st.button("Convert / تبدیل", key="bcv5"):
                if ct.startswith("1."): st.success(f"{(v * 9/5) + 32:.2f} °F")
                if ct.startswith("2."): st.success(f"{v * 0.621371:.2f} miles")
                if ct.startswith("3."): st.success(f"{v * 60:.0f} mins")

