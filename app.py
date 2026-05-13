import streamlit as st

# إعدادات الواجهة الاحترافية (Dark Theme)
st.set_page_config(page_title="تطبيق الأسطورة AI", layout="wide")

# تصميم لوجو خاص بـ فارس (FAREGAZI) بالـ CSS بدل اللوجو بتاعي
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    /* تصميم اللوجو الخاص بك */
    .my-logo {
        font-family: 'Arial Black', sans-serif;
        font-size: 40px;
        font-weight: bold;
        background: linear-gradient(45deg, #FFD700, #FF4500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        border: 2px solid #FFD700;
        padding: 10px;
        text-align: center;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background-color: #1E1E1E;
        color: gold;
        border: 1px solid #FFD700;
    }
    </style>
    <div class="my-logo">Faresgazi AI 🚀</div>
    """, unsafe_allow_html=True)

# --- القائمة الجانبية (Sidebar) ---
with st.sidebar:
    st.markdown("<h2 style='color: gold;'>🛠️ أدوات الأسطورة</h2>", unsafe_allow_html=True)
    st.button("🎥 إنشاء أفلام")
    st.button("🎨 صناعة كرتون")
    st.button("✍️ نصوص وأكواد")
    st.button("🔄 تحريك الصور")
    
    st.markdown("---")
    st.markdown("<h2 style='color: gold;'>📲 تفعيل الأجهزة</h2>", unsafe_allow_html=True)
    
    # زر الكاميرا الحقيقي
    st.camera_input("📸 افتح الكاميرا الآن")
    
    # زر الميكروفون
    if st.button("🎙️ تسجيل صوتي"):
        st.audio_input("سجل أمرك الصوتي يا فارس")

# --- منطقة الدردشة (شبه واجهتي بالظبط) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("تحدث مع الأسطورة..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        response = f"أهلاً يا فارس! أنا ذكاء الأسطورة الخاص بك. طلبت مني: '{prompt}'"
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

st.sidebar.markdown("---")
st.sidebar.caption("By: FAREGAZI GLOBAL")



