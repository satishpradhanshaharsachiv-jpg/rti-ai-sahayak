import streamlit as st
import datetime
import json
from pathlib import Path

# =========================================================
# RTI AI महा-सहाय्यक - ULTIMATE MOBILE VERSION
# =========================================================

st.set_page_config(
    page_title="RTI AI महा-सहाय्यक",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# MOBILE + GOLDEN GLOSSY CSS
# =========================================================

st.markdown("""
<style>
/* Streamlit mobile-first layout */
.stApp {
    background: linear-gradient(180deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
    color: #ffffff;
}

.block-container {
    max-width: 720px !important;
    padding: 8px 8px 85px 8px !important;
}

/* Hide unnecessary desktop/sidebar elements */
[data-testid="stSidebar"] {
    display: none;
}

header[data-testid="stHeader"] {
    height: 34px !important;
    background: transparent !important;
}

/* Header Box */
.mobile-header {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 18px;
    padding: 12px 10px;
    margin-bottom: 12px;
    text-align: center;
    border: 1.5px solid #ffd700;
    box-shadow: 0 4px 15px rgba(255, 215, 0, 0.25);
}

.mobile-header h1 {
    margin: 0;
    font-size: 22px;
    color: #ffd700;
    font-weight: 900;
    text-shadow: 0 0 8px rgba(255,215,0,0.6);
}

.mobile-header .tag {
    display: inline-block;
    margin-top: 5px;
    padding: 4px 10px;
    border-radius: 18px;
    background: linear-gradient(90deg, #ff8c00, #e52e71);
    color: #ffffff;
    font-size: 11px;
    font-weight: 800;
}

.mobile-header .person {
    margin-top: 6px;
    color: #ffd700;
    font-size: 10px;
}

/* Section Title */
.section-title {
    font-size: 18px;
    font-weight: 900;
    color: #ffd700;
    margin: 10px 2px 8px 2px;
}

/* Grid Layout Gap */
div[data-testid="stHorizontalBlock"] {
    gap: 6px !important;
}

div[data-testid="column"] {
    padding: 0 !important;
    min-width: 0 !important;
}

/* Glossy Golden Buttons */
div.stButton > button {
    width: 100% !important;
    min-height: 80px !important;
    height: 80px !important;
    border-radius: 14px !important;
    font-size: 12px !important;
    font-weight: 900 !important;
    line-height: 1.2 !important;
    white-space: pre-line !important;
    color: #ffffff !important;
    border: 1.5px solid #ffd700 !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.5), inset 0 1px 1px rgba(255,255,255,0.4) !important;
    margin-bottom: 6px !important;
    transition: transform .12s ease !important;
}

div.stButton > button:active {
    transform: scale(.95) !important;
}

/* Form Controls */
.stTextInput input, .stTextArea textarea {
    border-radius: 10px !important;
    font-size: 15px !important;
}

/* Output A4 Draft Box */
.a4-container {
    background: #ffffff;
    color: #111827;
    border-radius: 12px;
    padding: 16px;
    margin-top: 12px;
    line-height: 1.7;
    border: 2px dashed #ffd700;
    box-shadow: 0 4px 15px rgba(255,215,0,0.2);
}

.info-box {
    background: rgba(255, 255, 255, 0.1);
    border-left: 4px solid #ffd700;
    border-radius: 10px;
    padding: 10px;
    margin: 10px 0;
    font-size: 12px;
}

/* Bottom Nav Visual */
.bottom-nav {
    position: fixed;
    left: 8px;
    right: 8px;
    bottom: 8px;
    background: rgba(15, 32, 39, 0.95);
    border: 1px solid #ffd700;
    border-radius: 16px;
    padding: 8px;
    box-shadow: 0 -2px 12px rgba(0,0,0,0.5);
    text-align: center;
    z-index: 999;
    color: #ffd700;
    font-size: 11px;
}

/* Small Screens Styling */
@media (max-width: 420px) {
    div.stButton > button {
        min-height: 72px !important;
        height: 72px !important;
        font-size: 10.5px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# ONE-TIME MOBILE LOGIN SYSTEM
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

if "user_mobile" not in st.session_state:
    st.session_state.user_mobile = saved_mobile

if "active_module" not in st.session_state:
    st.session_state.active_module = "home"

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="mobile-header">
    <h1>⚖️ RTI AI महा-सहाय्यक</h1>
    <div class="tag">⚡ एका मिनिटात सर्व कायदेशीर मसुदे</div>
    <div class="person">
        👤 सतीश अशोक प्रधान | 📱 ८६६८२३५३९५ | छत्रपती संभाजीनगर
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# LOGIN SCREEN
# =========================================================

if not st.session_state.is_logged_in:

    st.markdown('<div class="section-title" style="text-align:center;">🔐 सुरक्षित मोबाईल प्रवेश</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        📱 तुमचा १० अंकी मोबाईल नंबर टाका. हा फक्त एकदाच विचारेल.
    </div>
    """, unsafe_allow_html=True)

    mobile = st.text_input("मोबाईल नंबर", placeholder="8668235395", max_chars=10)

    if st.button("🚀 ॲप सुरू करा", use_container_width=True, key="login_btn"):
        if len(mobile) == 10 and mobile.isdigit():
            save_mobile(mobile)
            st.session_state.is_logged_in = True
            st.session_state.user_mobile = mobile
            st.session_state.active_module = "home"
            st.rerun()
        else:
            st.error("कृपया अचूक १० अंकी मोबाईल नंबर टाका.")

    st.stop()

# =========================================================
# HOME SCREEN — 4 x 3 GRID (12 BUTTONS)
# =========================================================

if st.session_state.active_module == "home":

    st.markdown('<div class="section-title">📱 सेवा निवडा:</div>', unsafe_allow_html=True)

    # ROW 1
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("📄\nजोडपत्र 'अ'", key="b1"):
            st.session_state.active_module = "rti"
            st.rerun()
    with c2:
        if st.button("⚖️\nप्रथम अपील", key="b2"):
            st.session_state.active_module = "first_appeal"
            st.rerun()
    with c3:
        if st.button("🏛️\nमाहिती आयोग", key="b3"):
            st.session_state.active_module = "commission"
            st.rerun()
    with c4:
        if st.button("✨\nAI चॅट", key="b4"):
            st.session_state.active_module = "ai_chat"
            st.rerun()

    # ROW 2
    c5, c6, c7, c8 = st.columns(4)
    with c5:
        if st.button("📜\nकोर्ट याचिका", key="b5"):
            st.session_state.active_module = "court"
            st.rerun()
    with c6:
        if st.button("📣\nशासकीय तक्रार", key="b6"):
            st.session_state.active_module = "complaint"
            st.rerun()
    with c7:
        if st.button("✏️\nप्रतिज्ञापत्र", key="b7"):
            st.session_state.active_module = "affidavit"
            st.rerun()
    with c8:
        if strlit_b8 := st.button("🛒\nग्राहक मंच", key="b8"):
            st.session_state.active_module = "consumer"
            st.rerun()

    # ROW 3
    c9, c10, c11, c12 = st.columns(4)
    with c9:
        if st.button("📑\nग्रामपंचायत", key="b9"):
            st.session_state.active_module = "grampanchayat"
            st.rerun()
    with c10:
        if st.button("🏢\nमहापालिका", key="b10"):
            st.session_state.active_module = "corporation"
            st.rerun()
    with c11:
        if st.button("🚔\nपोलीस तक्रार", key="b11"):
            st.session_state.active_module = "police"
            st.rerun()
    with c12:
        if st.button("📂\nPDF/फाइल्स", key="b12"):
            st.session_state.active_module = "documents"
            st.rerun()

    st.markdown("""
    <div class="bottom-nav">
        🏠 मुख्य पृष्ठ &nbsp;&nbsp;|&nbsp;&nbsp; 📂 माझे अर्ज &nbsp;&nbsp;|&nbsp;&nbsp; ⚙️ सेटिंग
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# COMMON NAVIGATION FOR ALL MODULES
# =========================================================

else:
    if st.button("🏠 मुख्य पृष्ठावर जा", use_container_width=True, key="back_home"):
        st.session_state.active_module = "home"
        st.rerun()

# =========================================================
# MODULES LOGIC
# =========================================================

if st.session_state.active_module == "rti":
    st.markdown('<div class="section-title">📄 जोडपत्र \'अ\' - माहिती अधिकार अर्ज</div>', unsafe_allow_html=True)
    dept = st.text_input("जन माहिती अधिकारी, विभाग व पत्ता")
    subject = st.text_input("माहितीचा विषय")
    details = st.text_area("माहितीचा तपशील", height=150)
    if st.button("📝 मसुदा तयार करा", use_container_width=True, key="m_rti"):
        draft = f"**माहिती अधिकाराचा अर्ज (जोडपत्र 'अ')**\n\n**प्रति,**\nजन माहिती अधिकारी,\n{dept}\n\n**विषय:** {subject}\n\n**माहितीचा तपशील:**\n{details}\n\n**अर्जदार:** सतीश अशोक प्रधान\n**ठिकाण:** छत्रपती संभाजीनगर\n**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}"
        st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

elif st.session_state.active_module == "first_appeal":
    st.markdown('<div class="section-title">⚖️ प्रथम अपील अर्ज</div>', unsafe_allow_html=True)
    fa_dept = st.text_input("प्रथम अपिलीय अधिकारी व पत्ता")
    reason = st.text_area("अपिलाचे कारण", height=150)
    if st.button("📝 प्रथम अपील तयार करा", use_container_width=True, key="m_fa"):
        draft = f"**प्रथम अपील अर्ज**\n\n**प्रति,**\n{fa_dept}\n\n**अपिलाचे कारण:**\n{reason}\n\n**अपीलार्थी:** सतीश अशोक प्रधान\n**ठिकाण:** छत्रपती संभाजीनगर\n**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}"
        st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

elif st.session_state.active_module == "commission":
    st.markdown('<div class="section-title">🏛️ माहिती आयोग</div>', unsafe_allow_html=True)
    comm_details = st.text_area("तक्रार / द्वितीय अपील तपशील", height=180)
    if st.button("📝 आयोग अर्ज तयार करा", use_container_width=True, key="m_comm"):
        draft = f"**द्वितीय अपील / तक्रार**\n\n**प्रति,**\nमा. राज्य माहिती आयोग\n\n**तपशील:**\n{comm_details}\n\n**अर्जदार:** सतीश अशोक प्रधान\n**ठिकाण:** छत्रपती संभाजीनगर\n**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}"
        st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

elif st.session_state.active_module == "ai_chat":
    st.markdown('<div class="section-title">✨ AI कायदेशीर सल्लागार</div>', unsafe_allow_html=True)
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if prompt := st.chat_input("तुमचा प्रश्न येथे लिहा..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        res = f"सतीशजी, तुमच्या '{prompt}' या प्रश्नासंदर्भात योग्य मसुदा निवडण्यासाठी मुख्य मेन्यूचा वापर करा."
        with st.chat_message("assistant"):
            st.markdown(res)
        st.session_state.messages.append({"role": "assistant", "content": res})

elif st.session_state.active_module == "court":
    st.markdown('<div class="section-title">📜 कोर्ट याचिका मसुदा</div>', unsafe_allow_html=True)
    facts = st.text_area("प्रकरणाची हकीकत", height=180)
    if st.button("📝 याचिका मसुदा तयार करा", use_container_width=True, key="m_court"):
        draft = f"**कोर्ट याचिका — मसुदा**\n\n**हकीकत:**\n{facts}\n\n**याचिकाकर्ता:** सतीश अशोक प्रधान\n**ठिकाण:** छत्रपती संभाजीनगर"
        st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

elif st.session_state.active_module == "complaint":
    st.markdown('<div class="section-title">📣 शासकीय तक्रार अर्ज</div>', unsafe_allow_html=True)
    authority = st.text_input("तक्रार कोणाकडे करायची आहे?")
    comp = st.text_area("तक्रारीचा तपशील", height=180)
    if st.button("📝 तक्रार तयार करा", use_container_width=True, key="m_comp"):
        draft = f"**शासकीय तक्रार अर्ज**\n\n**प्रति,** {authority}\n\n**तपशील:**\n{comp}\n\n**तक्रारदार:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर"
        st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

elif st.session_state.active_module == "affidavit":
    st.markdown('<div class="section-title">✏️ प्रतिज्ञापत्र</div>', unsafe_allow_html=True)
    aff = st.text_area("प्रतिज्ञापत्रातील मुद्दे", height=180)
    if st.button("📝 प्रतिज्ञापत्र तयार करा", use_container_width=True, key="m_aff"):
        draft = f"**प्रतिज्ञापत्र**\n\nमी सतीश अशोक प्रधान, खालीलप्रमाणे घोषित करतो:\n{aff}\n\n**घोषणाकर्ता:** सतीश अशोक प्रधान"
        st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

elif st.session_state.active_module == "consumer":
    st.markdown('<div class="section-title">🛒 ग्राहक मंच तक्रार</div>', unsafe_allow_html=True)
    company = st.text_input("विरोधकांचे नाव")
    cons = st.text_area("तक्रार तपशील", height=180)
    if st.button("📝 ग्राहक मंच अर्ज तयार करा", use_container_width=True, key="m_cons"):
        draft = f"**ग्राहक मंच अर्ज**\n\n**विरोधक:** {company}\n\n**तपशील:**\n{cons}\n\n**तक्रारदार:** सतीश अशोक प्रधान"
        st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

elif st.session_state.active_module == "police":
    st.markdown('<div class="section-title">🚔 पोलीस ठाणे तक्रार</div>', unsafe_allow_html=True)
    station = st.text_input("पोलीस ठाणे")
    p_comp = st.text_area("तक्रार मजकूर", height=180)
    if st.button("📝 पोलीस तक्रार तयार करा", use_container_width=True, key="m_pol"):
        draft = f"**पोलीस ठाणे तक्रार अर्ज**\n\n**प्रति,** ठाणे अंमलदार, {station}\n\n**मजकूर:**\n{p_comp}\n\n**तक्रारदार:** सतीश अशोक प्रधान"
        st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

elif st.session_state.active_module == "documents":
    st.markdown('<div class="section-title">📂 दस्तऐवज / PDF</div>', unsafe_allow_html=True)
    uploaded = st.file_uploader("📎 कागदपत्र निवडा", accept_multiple_files=True)
    if uploaded:
        st.success(f"{len(uploaded)} फायली निवडल्या आहेत.")

else:
    st.markdown(f'<div class="section-title">📑 {st.session_state.active_module.upper()} मसुदा</div>', unsafe_allow_html=True)
    gen_text = st.text_area("तपशील प्रविष्ट करा:", height=180)
    if st.button("📝 अर्ज तयार करा", use_container_width=True, key="m_gen"):
        draft = f"**अर्ज / मसुदा**\n\n**तपशील:**\n{gen_text}\n\n**अर्जदार:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर"
        st.markdown(f'<div class="a4-container">{draft}</div>', unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div style="text-align:center; font-size:10px; color:#ffd700; padding:12px;">
⚖️ RTI AI महा-सहाय्यक <br>
सतीश अशोक प्रधान | छत्रपती संभाजीनगर
</div>
""", unsafe_allow_html=True)
