import streamlit as st

st.set_page_config(page_title="تطبيق الأسطورة AI")
st.title("🚀 تطبيق الأسطورة AI")

# خانة الدردشة
user_input = st.text_input("اكتب رسالتك هنا يا فارس:")

if user_input:
    st.write(f"الأسطورة يقول: {user_input}")

# أزرار المهام
if st.button("🎥 إنشاء فيديو"):
    st.success("جاري البدء...")

if st.button("🖼️ توليد صور"):
    st.success("جاري التصميم...")

st.markdown("---")
st.caption("Developed by Faresgazi Global")

