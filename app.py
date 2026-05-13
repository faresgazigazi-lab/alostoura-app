import streamlit as st

st.set_page_config(page_title="تطبيق الأسطورة", layout="centered")

st.title("🚀 تطبيق الأسطورة AI")
st.subheader("مرحباً بك يا فارس في عالمك الخاص")

col1, col2 = st.columns(2)
with col1:
    if st.button("🎥 إنشاء فيديو AI"): 
        st.success("جاري تحضير استوديو الفيديوهات...")
    if st.button("🖼️ توليد صور سحرية"): 
        st.success("افتح الكاميرا أو ارفع صورة...")
with col2:
    if st.button("📝 كتابة أكواد ونصوص"): 
        st.success("المبرمج الصغير جاهز للعمل...")
    if st.button("🎞️ صناعة أفلام كرتون"): 
        st.success("جاري تجهيز استوديو الرسوم المتحركة...")

st.info("تم التطوير بواسطة: Faresgazi Global")
