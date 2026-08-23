import streamlit as st
import datetime
import json
from pathlib import Path

# =========================================================
# Streamlit Configuration
# =========================================================

st.set_page_config(
    page_title="RTI AI महा-सहाय्यक",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# MOBILE HTML-GRID & CUSTOM COLOR CSS
# =========================================================

st.markdown("""
<style>
/* मोबाईल व्ह्यू लॉक करणे - स्क्रोलिंग रोखण्यासाठी */
html, body, .stApp {
    background-color: #f4f6f9;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

/* जास्तीची जागा आणि साईडबार लपवणे */
[data-testid="stSidebar"], header[data-testid="stHeader"], footer {
    display: none !important;
}

.block-container {
    max-width: 100% !important;
    padding: 10px 10px 80px 10px !important;
}

/* हेडर डिझाइन */
.mobile-header {
    background: #ffffff;
    border-radius: 16px;
    padding: 12px;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    margin-bottom: 15px;
}

.mobile-header h1 {
    margin: 0;
    font-size: 20px;
    color: #00a86b;
    font-weight: 800;
}

.mobile-header .tag {
    display: inline-block;
    margin-top: 4px;
    padding: 3px 10px;
    border-radius: 12px;
    background: #fff3e0;
    color: #e65100;
    font-size: 11px;
    font-weight: bold;
    border: 1px dashed #ffa726;
}

.mobile-header .person {
    margin-top: 5px;
    color: #666;
    font-size: 10px;
}

/* ४x३ मोबाईल ग्रिड (HTML Layout) */
.grid-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    margin-bottom: 15px;
}

/* बटनांचे स्टायलिंग व चमचमीत रंग */
.app-btn {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 75px;
    border-radius: 16px;
    color: white !important;
    text-decoration: none !important;
    font-size: 11px;
    font-weight: bold;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    border: none;
    cursor: pointer;
    line-height: 1.2;
}

.app-btn span {
    font-size: 20px;
    margin-bottom: 3px;
}

/* प्रत्येक बटनाचे वेगळे चमचमीत रंगांचे ग्रेडियंट्स */
.btn-1  { background: linear-gradient(135deg, #11998e, #38ef7d); }
.btn-2  { background: linear-gradient(135deg, #FF416C, #FF4B2B); }
.btn-3  { background: linear-gradient(135deg, #8A2387, #E94057); }
.btn-4  { background: linear-gradient(135deg, #f7b731, #fa8231); }

.btn-5  { background: linear-gradient(135deg, #654ea3, #eaafc8); }
.btn-6  { background: linear-gradient(135deg, #00B4DB, #0083B0); }
.btn-7  { background: linear-gradient(135deg, #f12711, #f5af19); }
.btn-8  { background: linear-gradient(135deg, #56ab2f, #a8e063); }

.btn-9  { background: linear-gradient(135deg, #4776E6, #8E54E9); }
.btn-10 { background: linear-gradient(135deg, #614385, #516395); }
.btn-11 { background: linear-gradient(135deg, #11998e, #38ef7d); }
.btn-12 { background: linear-gradient(135deg, #fc4a1a, #f7b731); }

/* मसुदा A4 बॉक्स */
.a4-container {
    background: #ffffff;
    color: #111827;
    border-radius: 12px;
    padding: 15px;
    margin-top: 10px;
    line-height: 1.6;
    border: 2px dashed #00a86b;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# ONE-TIME LOGIN LOGIC
# =========================================================

USER_FILE = "rti_user.json"

def load_saved_mobile():
    try:
        user_path = Path(USER_FILE)
        if user_path.exists():
            data = json.loads(user_path.read_text(encoding="utf-8"))
            mobile = str(data.get("mobile", "")).strip()
            if len(mobile) == 10 and mobile.isdigit():
                return mobile
    except Exception:
        pass
    return ""

def save_mobile(mobile):
    Path(USER_FILE).write_text(
        json.dumps({"mobile": mobile}, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

saved_mobile = load_saved_mobile()

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = bool(saved_mobile)

if "active_module" not in st.session_state:
    st.session_state.active_module = "home"

# query_params द्वारे क्लिक हाताळणे
query_params = st.query_params
if "mod" in query_params:
    st.session_state.active_module = query_params["mod"]

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="mobile-header">
    <h1>⚖️ RTI AI महा-सहाय्यक</h1>
    <div class="tag">⚡ एका मिनिटात सर्व कायदेशीर मसुदे</div>
    <div class="person">👤 सतीश अशोक प्रधान | 📱 ८६६८२३५३९५ | छत्रपती संभाजीनगर</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# LOGIN
# =========================================================

if not st.session_state.is_logged_in:
    st.markdown("<h4 style='text-align:center;'>🔐 सुरक्षित मोबाईल प्रवेश</h4>", unsafe_allow_html=True)
    mobile = st.text_input("मोबाईल नंबर टाका:", placeholder="8668235395", max_chars=10)
    if st.button("🚀 ॲप सुरू करा", use_container_width=True):
        if len(mobile) == 10 and mobile.isdigit():
            save_mobile(mobile)
            st.session_state.is_logged_in = True
            st.rerun()
        else:
            st.error("कृपया अचूक १० अंकी मोबाईल नंबर टाका.")
    st.stop()

# =========================================================
# HOME SCREEN (HTML GRID - NO SIDE SCROLL, MULTICOLOR)
# =========================================================

if st.session_state.active_module == "home":

    st.markdown("""
    <div class="grid-container">
        <a href="?mod=rti" target="_self" class="app-btn btn-1"><span>📄</span>जोडपत्र 'अ'</a>
        <a href="?mod=first_appeal" target="_self" class="app-btn btn-2"><span>⚖️</span>प्रथम अपील</a>
        <a href="?mod=commission" target="_self" class="app-btn btn-3"><span>🏛️</span>माहिती आयोग</a>
        <a href="?mod=ai_chat" target="_self" class="app-btn btn-4"><span>✨</span>AI चॅट</a>
        
        <a href="?mod=court" target="_self" class="app-btn btn-5"><span>📜</span>कोर्ट याचिका</a>
        <a href="?mod=complaint" target="_self" class="app-btn btn-6"><span>📣</span>शासकीय तक्रार</a>
        <a href="?mod=affidavit" target="_self" class="app-btn btn-7"><span>✏️</span>प्रतिज्ञापत्र</a>
        <a href="?mod=consumer" target="_self" class="app-btn btn-8"><span>🛒</span>ग्राहक मंच</a>
        
        <a href="?mod=grampanchayat" target="_self" class="app-btn btn-9"><span>📑</span>ग्रामपंचायत</a>
        <a href="?mod=corporation" target="_self" class="app-btn btn-10"><span>🏢</span>महापालिका</a>
        <a href="?mod=police" target="_self" class="app-btn btn-11"><span>🚔</span>पोलीस तक्रार</a>
        <a href="?mod=documents" target="_self" class="app-btn btn-12"><span>📂</span>PDF/फाइल्स</a>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# MODULE PAGES
# =========================================================

else:
    if st.button("🏠 मुख्य पृष्ठावर जा", use_container_width=True):
        st.query_params.clear()
        st.session_state.active_module = "home"
        st.rerun()

    if st.session_state.active_module == "rti":
        st.subheader("📄 जोडपत्र 'अ' - माहिती अधिकार अर्ज")
        dept = st.text_input("विभाग व पत्ता:")
        subject = st.text_input("विषय:")
        details = st.text_area("माहितीचा तपशील:")
        if st.button("मसुदा तयार करा"):
            draft = f"**माहिती अधिकाराचा अर्ज (जोडपत्र 'अ')**\n\n**प्रति,** जन माहिती अधिकारी, {dept}\n\n**विषय:** {subject}\n\n**तपशील:** {details}\n\n**अर्जदार:** सतीश अशोक प्रधान | दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}"
            st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

    elif st.session_state.active_module == "first_appeal":
        st.subheader("⚖️ प्रथम अपील अर्ज")
        fa_dept = st.text_input("प्रथम अपिलीय अधिकारी:")
        reason = st.text_area("अपिलाचे कारण:")
        if st.button("अपील तयार करा"):
            draft = f"**प्रथम अपील अर्ज**\n\n**प्रति,** {fa_dept}\n\n**कारण:** {reason}\n\n**अपीलार्थी:** सतीश अशोक प्रधान"
            st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

    elif st.session_state.active_module == "police":
        st.subheader("🚔 पोलीस ठाणे तक्रार")
        station = st.text_input("पोलीस ठाणे:")
        p_comp = st.text_area("तक्रार मजकूर:")
        if st.button("तक्रार तयार करा"):
            draft = f"**पोलीस तक्रार अर्ज**\n\n**प्रति,** ठाणे अंमलदार, {station}\n\n**मजकूर:** {p_comp}\n\n**तक्रारदार:** सतीश अशोक प्रधान"
            st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

    else:
        st.subheader(f"📑 {st.session_state.active_module.upper()} सेवा")
        gen_text = st.text_area("तपशील टाका:")
        if st.button("अर्ज तयार करा"):
            draft = f"**अर्ज मसुदा**\n\n**तपशील:** {gen_text}\n\n**अर्जदार:** सतीश अशोक प्रधान"
            st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)
