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
# MOBILE APP CSS (NO HORIZONTAL SCROLL & BEAUTIFUL BUTTONS)
# =========================================================

st.markdown("""
<style>
/* मोबाईल व्ह्यू लॉक करणे - डावीकडे/उजवीकडे सरकणे बंद */
html, body, .stApp {
    background-color: #0f172a !important;
    color: #ffffff !important;
    overflow-x: hidden !important;
}

/* जास्तीची जागा आणि साईडबार लपवणे */
[data-testid="stSidebar"], header[data-testid="stHeader"], footer {
    display: none !important;
}

.block-container {
    max-width: 100% !important;
    padding: 8px 6px 80px 6px !important;
}

/* हेडर बॉक्स */
.mobile-header {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 14px;
    padding: 10px;
    text-align: center;
    border: 1px solid #ffd700;
    margin-bottom: 12px;
}

.mobile-header h1 {
    margin: 0;
    font-size: 18px;
    color: #ffd700;
    font-weight: 800;
}

.mobile-header .tag {
    display: inline-block;
    margin-top: 4px;
    padding: 2px 8px;
    border-radius: 10px;
    background: #ff9800;
    color: #ffffff;
    font-size: 10px;
    font-weight: bold;
}

.mobile-header .person {
    margin-top: 5px;
    color: #cbd5e1;
    font-size: 10px;
}

/* ४ कॉलम मोबाईल ग्रिडसाठी जागा आणि लेआउट */
div[data-testid="stHorizontalBlock"] {
    gap: 4px !important;
    display: flex !important;
    flex-wrap: nowrap !important;
}

div[data-testid="column"] {
    min-width: 0 !important;
    flex: 1 1 0% !important;
    padding: 0 !important;
}

/* चमचमीत रंगीत बटन्स (Text Visible & Colorful) */
div.stButton > button {
    width: 100% !important;
    min-height: 70px !important;
    height: 70px !important;
    border-radius: 12px !important;
    font-size: 11px !important;
    font-weight: 800 !important;
    line-height: 1.2 !important;
    white-space: pre-line !important;
    color: #ffffff !important;
    border: none !important;
    box-shadow: 0 3px 6px rgba(0,0,0,0.3) !important;
    margin-bottom: 4px !important;
    padding: 2px !important;
}

/* प्रत्येक ओळीतील बटनांचे रंगेबेरंगी ग्रेडियंट्स */
div[data-testid="column"]:nth-child(1) div.stButton > button { background: linear-gradient(135deg, #10b981, #059669) !important; }
div[data-testid="column"]:nth-child(2) div.stButton > button { background: linear-gradient(135deg, #ef4444, #dc2626) !important; }
div[data-testid="column"]:nth-child(3) div.stButton > button { background: linear-gradient(135deg, #8b5cf6, #7c3aed) !important; }
div[data-testid="column"]:nth-child(4) div.stButton > button { background: linear-gradient(135deg, #f59e0b, #d97706) !important; }

/* A4 मसुदा बॉक्स */
.a4-container {
    background: #ffffff;
    color: #0f172a;
    border-radius: 12px;
    padding: 14px;
    margin-top: 10px;
    line-height: 1.6;
    border: 2px dashed #ffd700;
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
# LOGIN SCREEN
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
# HOME SCREEN (4x3 PURE STREAMLIT MOBILE GRID)
# =========================================================

if st.session_state.active_module == "home":

    # Row 1
    r1_c1, r1_c2, r1_c3, r1_c4 = st.columns(4)
    with r1_c1:
        if st.button("📄\nजोडपत्र 'अ'", key="b1"):
            st.session_state.active_module = "rti"
            st.rerun()
    with r1_c2:
        if st.button("⚖️\nप्रथम अपील", key="b2"):
            st.session_state.active_module = "first_appeal"
            st.rerun()
    with r1_c3:
        if st.button("🏛️\nमाहिती आयोग", key="b3"):
            st.session_state.active_module = "commission"
            st.rerun()
    with r1_c4:
        if st.button("✨\nAI चॅट", key="b4"):
            st.session_state.active_module = "ai_chat"
            st.rerun()

    # Row 2
    r2_c1, r2_c2, r2_c3, r2_c4 = st.columns(4)
    with r2_c1:
        if st.button("📜\nकोर्ट याचिका", key="b5"):
            st.session_state.active_module = "court"
            st.rerun()
    with r2_c2:
        if st.button("📣\nशासकीय तक्रार", key="b6"):
            st.session_state.active_module = "complaint"
            st.rerun()
    with r2_c3:
        if st.button("✏️\nप्रतिज्ञापत्र", key="b7"):
            st.session_state.active_module = "affidavit"
            st.rerun()
    with r2_c4:
        if st.button("🛒\nग्राहक मंच", key="b8"):
            st.session_state.active_module = "consumer"
            st.rerun()

    # Row 3
    r3_c1, r3_c2, r3_c3, r3_c4 = st.columns(4)
    with r3_c1:
        if st.button("📑\nग्रामपंचायत", key="b9"):
            st.session_state.active_module = "grampanchayat"
            st.rerun()
    with r3_c2:
        if st.button("🏢\nमहापालिका", key="b10"):
            st.session_state.active_module = "corporation"
            st.rerun()
    with r3_c3:
        if st.button("🚔\nपोलीस तक्रार", key="b11"):
            st.session_state.active_module = "police"
            st.rerun()
    with r3_c4:
        if st.button("📂\nPDF/फाइल्स", key="b12"):
            st.session_state.active_module = "documents"
            st.rerun()

# =========================================================
# MODULE PAGES
# =========================================================

else:
    if st.button("🏠 मुख्य पृष्ठावर जा", use_container_width=True):
        st.session_state.active_module = "home"
        st.rerun()

    if st.session_state.active_module == "rti":
        st.subheader("📄 जोडपत्र 'अ' - माहिती अधिकार अर्ज")
        dept = st.text_input("विभाग व पत्ता:")
        subject = st.text_input("विषय:")
        details = st.text_area("माहितीचा तपशील:")
        if st.button("मसुदा तयार करा", use_container_width=True):
            draft = f"**माहिती अधिकाराचा अर्ज (जोडपत्र 'अ')**\n\n**प्रति,** जन माहिती अधिकारी, {dept}\n\n**विषय:** {subject}\n\n**तपशील:** {details}\n\n**अर्जदार:** सतीश अशोक प्रधान | दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}"
            st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

    elif st.session_state.active_module == "first_appeal":
        st.subheader("⚖️ प्रथम अपील अर्ज")
        fa_dept = st.text_input("प्रथम अपिलीय अधिकारी:")
        reason = st.text_area("अपिलाचे कारण:")
        if st.button("अपील तयार करा", use_container_width=True):
            draft = f"**प्रथम अपील अर्ज**\n\n**प्रति,** {fa_dept}\n\n**कारण:** {reason}\n\n**अपीलार्थी:** सतीश अशोक प्रधान"
            st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

    elif st.session_state.active_module == "police":
        st.subheader("🚔 पोलीस ठाणे तक्रार")
        station = st.text_input("पोलीस ठाणे:")
        p_comp = st.text_area("तक्रार मजकूर:")
        if st.button("तक्रार तयार करा", use_container_width=True):
            draft = f"**पोलीस तक्रार अर्ज**\n\n**प्रति,** ठाणे अंमलदार, {station}\n\n**मजकूर:** {p_comp}\n\n**तक्रारदार:** सतीश अशोक प्रधान"
            st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

    else:
        st.subheader(f"📑 {st.session_state.active_module.upper()} सेवा")
        gen_text = st.text_area("तपशील टाका:")
        if st.button("अर्ज तयार करा", use_container_width=True):
            draft = f"**अर्ज मसुदा**\n\n**तपशील:** {gen_text}\n\n**अर्जदार:** सतीश अशोक प्रधान"
            st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)
