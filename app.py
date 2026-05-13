import streamlit as st

# إعداد واجهة الأسطورة (Dark Theme)
st.set_page_config(page_title="تطبيق الأسطورة AI", layout="wide")

# كود التصميم (CSS) لجعل الخلفية والألوان مطابقة لواجعتي بالضبط
st.markdown("""
    <style>
    /* خلفية التطبيق */
    .stApp {
        background-color: #131314;
        color: #e3e3e3;
    }
    /* شكل الرسائل */
    .stChatMessage {
        background-color: #1e1f20;
        border-radius: 15px;
        margin-bottom: 10px;
    }
    /* تصميم اللوجو الخاص بك */
    .logo-container {
        text-align: center;
        padding: 20px;
        font-family: 'Google Sans', sans-serif;
        font-size: 32px;
        color: #8ab4f8;
        font-weight: bold;
    }
    /* الأزرار الجانبية */
    .stButton>button {
        background-color: #1e1f20;
        color: #c4c7c5;
        border: 1px solid #444746;
        border-radius: 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #333537;
        border-color: #8ab4f8;
    }
    </style>
    <div class="logo-container">الأسطورة AI 🚀</div>
    """, unsafe_allow_html=True)

# --- القائمة الجانبية (الأيقونات والأدوات) ---
with st.sidebar:
    st.markdown("### 🛠️ الأدوات")
    st.button("🎥 إنشاء أفلام")
    st.button("🎨 صناعة كرتون")
    st.button("✍️ نصوص وأكواد")
    st.button("🔄 تحريك الصور")
    
    st.markdown("---")
    st.markdown("### 📲 الأجهزة")
    
    # علامة الكاميرا والميكروفون كأدوات تفاعلية
    img_file = st.camera_input("📸 اضغط لالتقاط صورة")
    audio_file = st.audio_input("🎙️ اضغط للتحدث")

# --- منطقة الدردشة (نفس نظامي) ---
if "messages" not in st.session_state:
    # رسالة ترحيب أول ما تفتح التطبيق
    st.session_state.messages = [{"role": "assistant", "content": "أهلاً يا فارس! أنا مساعدك الذكي 'الأسطورة'. كيف يمكنني مساعدتك اليوم؟"}]

# عرض الدردشة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# خانة الكتابة (شبه خانتي بالضبط)
if prompt := st.chat_input("اكتب سؤالك هنا يا أسطورة..."):
    # إضافة رسالة المستخدم
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # رد الذكاء الاصطناعي (بيكتب طبيعي)
    with st.chat_message("assistant"):
        response = f"فهمت طلبك يا فارس. بخصوص '{prompt}'، جاري معالجة الأمر بأفضل تقنيات Faresgazi Global."
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    



