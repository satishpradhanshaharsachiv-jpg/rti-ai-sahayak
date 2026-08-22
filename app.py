import streamlit as st
import datetime
import json
from pathlib import Path

# =========================================================
# RTI AI महा-सहाय्यक - MOBILE FIRST VERSION
# =========================================================

st.set_page_config(
    page_title="RTI AI महा-सहाय्यक",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# MOBILE CSS
# =========================================================

st.markdown("""
<style>
/* Streamlit mobile-first layout */
.stApp {
    background: #f5f7fb;
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

/* Header */
.mobile-header {
    background: #ffffff;
    border-radius: 20px;
    padding: 14px 10px;
    margin-bottom: 12px;
    text-align: center;
    box-shadow: 0 3px 14px rgba(0,0,0,.08);
}

.mobile-header h1 {
    margin: 0;
    font-size: 25px;
    color: #08a678;
    font-weight: 900;
}

.mobile-header .tag {
    display: inline-block;
    margin-top: 7px;
    padding: 6px 13px;
    border-radius: 22px;
    background: #fff4ce;
    border: 1px dashed #e0a800;
    color: #a86500;
    font-size: 12px;
    font-weight: 800;
}

.mobile-header .person {
    margin-top: 7px;
    color: #555;
    font-size: 11px;
}

/* Section heading */
.section-title {
    font-size: 22px;
    font-weight: 900;
    color: #202738;
    margin: 12px 2px 10px 2px;
}

/* EXACT 3 x 3 mobile grid */
div[data-testid="stHorizontalBlock"] {
    gap: 7px !important;
}

div[data-testid="column"] {
    padding: 0 !important;
    min-width: 0 !important;
}

/* App buttons */
div.stButton > button {
    width: 100% !important;
    min-height: 112px !important;
    height: 112px !important;
    border: none !important;
    border-radius: 22px !important;
    color: white !important;
    font-size: 15px !important;
    font-weight: 900 !important;
    line-height: 1.25 !important;
    white-space: pre-line !important;
    box-shadow: 0 5px 13px rgba(0,0,0,.18) !important;
    margin-bottom: 7px !important;
    transition: transform .12s ease !important;
}

div.stButton > button:active {
    transform: scale(.96) !important;
}

/* Home grid button colors based on position */
.home-r1 button { background: linear-gradient(135deg,#13b981,#079669) !important; }
.home-r2 button { background: linear-gradient(135deg,#ff9f43,#ff6b35) !important; }
.home-r3 button { background: linear-gradient(135deg,#4d7cff,#3457d5) !important; }
.home-r4 button { background: linear-gradient(135deg,#8e44ec,#6435c8) !important; }
.home-r5 button { background: linear-gradient(135deg,#ff647c,#e52e4d) !important; }
.home-r6 button { background: linear-gradient(135deg,#ff8a32,#e85d04) !important; }
.home-r7 button { background: linear-gradient(135deg,#23b5aa,#11998e) !important; }
.home-r8 button { background: linear-gradient(135deg,#4e8ff7,#2d67ce) !important; }
.home-r9 button { background: linear-gradient(135deg,#8067e8,#5b43c6) !important; }

/* We use nth button classes by wrapping each Streamlit button */
.home-r1 div.stButton > button { background: linear-gradient(135deg,#13b981,#079669) !important; }
.home-r2 div.stButton > button { background: linear-gradient(135deg,#ff9f43,#ff6b35) !important; }
.home-r3 div.stButton > button { background: linear-gradient(135deg,#4d7cff,#3457d5) !important; }

/* Form controls */
.stTextInput input,
.stTextArea textarea {
    border-radius: 12px !important;
    font-size: 16px !important;
}

.stTextArea textarea {
    min-height: 140px !important;
}

.a4-container {
    background: #ffffff;
    color: #111827;
    border-radius: 15px;
    padding: 18px;
    margin-top: 12px;
    line-height: 1.8;
    box-shadow: 0 3px 15px rgba(0,0,0,.10);
}

.info-box {
    background: #eef4ff;
    border-left: 5px solid #3b82f6;
    border-radius: 14px;
    padding: 13px;
    margin: 10px 0;
}

/* Bottom navigation visual */
.bottom-nav {
    position: fixed;
    left: 8px;
    right: 8px;
    bottom: 8px;
    background: rgba(255,255,255,.96);
    border-radius: 20px;
    padding: 9px;
    box-shadow: 0 -2px 15px rgba(0,0,0,.15);
    text-align: center;
    z-index: 999;
    color: #555;
    font-size: 11px;
}

/* Small phone screens */
@media (max-width: 420px) {
    .block-container {
        padding-left: 6px !important;
        padding-right: 6px !important;
    }

    .mobile-header h1 {
        font-size: 21px;
    }

    .section-title {
        font-size: 20px;
    }

    div[data-testid="stHorizontalBlock"] {
        gap: 5px !important;
    }

    div.stButton > button {
        min-height: 103px !important;
        height: 103px !important;
        border-radius: 18px !important;
        font-size: 13px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE + ONE-TIME MOBILE LOGIN
# =========================================================

# मोबाइल नंबर एकदाच सेव्ह करण्यासाठी स्थानिक फाइल
# त्यामुळे Streamlit refresh / पुन्हा उघडल्यानंतर नंबर पुन्हा विचारला जाणार नाही.
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
    <div class="tag">⚡ घरबसल्या एका मिनिटात अर्ज तयार करा</div>
    <div class="person">
        👤 सतीश अशोक प्रधान | 📱 ८६६८२३५३९५ |
        छत्रपती संभाजीनगर
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# LOGIN
# =========================================================

if not st.session_state.is_logged_in:

    st.markdown(
        '<div class="section-title" style="text-align:center;">🔐 पहिल्यांदा मोबाईल प्रवेश</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-box">
        📱 तुमचा १० अंकी मोबाईल नंबर फक्त एकदाच टाका.
        पुढील वेळी ॲप थेट खुले होईल.
    </div>
    """, unsafe_allow_html=True)

    mobile = st.text_input(
        "मोबाईल नंबर",
        placeholder="१० अंकी मोबाईल नंबर",
        max_chars=10
    )

    if st.button("🚀 ॲप सुरू करा", use_container_width=True):
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
# HOME - 3 x 3
# =========================================================

if st.session_state.active_module == "home":

    st.markdown(
        '<div class="section-title">📱 कायदेशीर सेवा निवडा</div>',
        unsafe_allow_html=True
    )

    # ROW 1
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("📄\nजोडपत्र 'अ'", key="home_rti"):
            st.session_state.active_module = "rti"
            st.rerun()

    with c2:
        if st.button("⚖️\nप्रथम अपील", key="home_fa"):
            st.session_state.active_module = "first_appeal"
            st.rerun()

    with c3:
        if st.button("🏛️\nमाहिती आयोग", key="home_comm"):
            st.session_state.active_module = "commission"
            st.rerun()

    # ROW 2
    c4, c5, c6 = st.columns(3)

    with c4:
        if st.button("✨\nAI चॅट", key="home_ai"):
            st.session_state.active_module = "ai_chat"
            st.rerun()

    with c5:
        if st.button("📜\nकोर्ट याचिका", key="home_court"):
            st.session_state.active_module = "court"
            st.rerun()

    with c6:
        if st.button("📣\nशासकीय तक्रार", key="home_comp"):
            st.session_state.active_module = "complaint"
            st.rerun()

    # ROW 3
    c7, c8, c9 = st.columns(3)

    with c7:
        if st.button("✏️\nप्रतिज्ञापत्र", key="home_aff"):
            st.session_state.active_module = "affidavit"
            st.rerun()

    with c8:
        if st.button("🛒\nग्राहक मंच", key="home_cons"):
            st.session_state.active_module = "consumer"
            st.rerun()

    with c9:
        if st.button("📂\nदस्तऐवज / PDF", key="home_docs"):
            st.session_state.active_module = "documents"
            st.rerun()

    st.markdown("""
    <div class="info-box">
        💡 कोणतीही सेवा निवडा. संबंधित अर्जाचा प्राथमिक मसुदा तयार करता येईल.
    </div>

    <div class="bottom-nav">
        🏠 मुख्य पृष्ठ &nbsp;&nbsp;&nbsp; 📂 माझे अर्ज &nbsp;&nbsp;&nbsp;
        ⚙️ सेटिंग &nbsp;&nbsp;&nbsp; ❓ मदत
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# BACK TO HOME FOR ALL MODULES
# =========================================================

else:

    if st.button("🏠 मुख्य पृष्ठावर जा", use_container_width=True):
        st.session_state.active_module = "home"
        st.rerun()

# =========================================================
# RTI
# =========================================================

if st.session_state.active_module == "rti":

    st.markdown(
        '<div class="section-title">📄 जोडपत्र \'अ\' - माहिती अधिकार अर्ज</div>',
        unsafe_allow_html=True
    )

    dept = st.text_input("जन माहिती अधिकारी, विभाग व पत्ता")
    subject = st.text_input("माहितीचा विषय")
    details = st.text_area("माहितीचा तपशील", height=180)

    if st.button("📝 मसुदा तयार करा", use_container_width=True):

        draft = f"""
**माहिती अधिकाराचा अर्ज (जोडपत्र 'अ')**

प्रति,
जन माहिती अधिकारी,
{dept}

**विषय:** {subject}

**माहितीचा तपशील:**
{details}

**अर्जदार:** सतीश अशोक प्रधान
**ठिकाण:** छत्रपती संभाजीनगर
**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="a4-container">{draft}</div>',
            unsafe_allow_html=True
        )

# =========================================================
# FIRST APPEAL
# =========================================================

elif st.session_state.active_module == "first_appeal":

    st.markdown(
        '<div class="section-title">⚖️ प्रथम अपील अर्ज</div>',
        unsafe_allow_html=True
    )

    fa_dept = st.text_input("प्रथम अपिलीय अधिकारी व पत्ता")
    reason = st.text_area("अपिलाचे कारण", height=180)

    if st.button("📝 प्रथम अपील तयार करा", use_container_width=True):

        draft = f"""
**प्रथम अपील अर्ज**

प्रति,
{fa_dept}

**अपिलाचे कारण:**
{reason}

**अपीलार्थी:** सतीश अशोक प्रधान
**ठिकाण:** छत्रपती संभाजीनगर
**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="a4-container">{draft}</div>',
            unsafe_allow_html=True
        )

# =========================================================
# COMMISSION
# =========================================================

elif st.session_state.active_module == "commission":

    st.markdown(
        '<div class="section-title">🏛️ माहिती आयोग</div>',
        unsafe_allow_html=True
    )

    comm_details = st.text_area(
        "तक्रार / द्वितीय अपील तपशील",
        height=220
    )

    if st.button("📝 आयोग अर्ज तयार करा", use_container_width=True):

        draft = f"""
**द्वितीय अपील / तक्रार**

प्रति,
मा. राज्य माहिती आयोग

**तपशील:**
{comm_details}

**अर्जदार:** सतीश अशोक प्रधान
**ठिकाण:** छत्रपती संभाजीनगर
**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="a4-container">{draft}</div>',
            unsafe_allow_html=True
        )

# =========================================================
# AI CHAT
# =========================================================

elif st.session_state.active_module == "ai_chat":

    st.markdown(
        '<div class="section-title">✨ AI कायदेशीर सल्लागार</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-box">
        ✨ RTI, अपील, तक्रार किंवा कायदेशीर प्रक्रियेबद्दल प्रश्न विचारा.
    </div>
    """, unsafe_allow_html=True)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("तुमचा प्रश्न येथे लिहा...")

    if prompt:

        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        if "आरटीआय" in prompt or "RTI" in prompt.upper() or "माहिती" in prompt:
            response = (
                "माहिती अधिकारासंबंधी प्रश्नासाठी जोडपत्र 'अ' "
                "वापरून अर्जाचा मसुदा तयार करता येईल."
            )
        elif "अपील" in prompt:
            response = (
                "तुमच्या प्रकरणाची माहिती दिल्यास प्रथम अपीलाचा "
                "प्राथमिक मसुदा तयार करता येईल."
            )
        elif "तक्रार" in prompt:
            response = (
                "तक्रारीचे कार्यालय, विषय, घटना आणि मागणी दिल्यास "
                "शासकीय तक्रार अर्ज तयार करता येईल."
            )
        else:
            response = (
                f"सतीशजी, तुमचा प्रश्न: **{prompt}**\n\n"
                "कृपया थोडा अधिक तपशील द्या."
            )

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

# =========================================================
# COURT
# =========================================================

elif st.session_state.active_module == "court":

    st.markdown(
        '<div class="section-title">📜 कोर्ट याचिका मसुदा</div>',
        unsafe_allow_html=True
    )

    facts = st.text_area("प्रकरणाची हकीकत", height=240)
    relief = st.text_area("मागणी / दिलासा", height=140)

    if st.button("📝 याचिका मसुदा तयार करा", use_container_width=True):

        draft = f"""
**कोर्ट याचिका — प्राथमिक मसुदा**

**प्रकरणाची हकीकत:**
{facts}

**मागणी / दिलासा:**
{relief}

**याचिकाकर्ता:** सतीश अशोक प्रधान
**ठिकाण:** छत्रपती संभाजीनगर
**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}

*हा प्राथमिक मसुदा आहे. दाखल करण्यापूर्वी संबंधित कायदेशीर तज्ज्ञाकडून तपासणी करावी.*
"""

        st.markdown(
            f'<div class="a4-container">{draft}</div>',
            unsafe_allow_html=True
        )

# =========================================================
# COMPLAINT
# =========================================================

elif st.session_state.active_module == "complaint":

    st.markdown(
        '<div class="section-title">📣 शासकीय तक्रार अर्ज</div>',
        unsafe_allow_html=True
    )

    authority = st.text_input("तक्रार कोणाकडे करायची आहे?")
    subject = st.text_input("तक्रारीचा विषय")
    comp = st.text_area("तक्रारीचा संपूर्ण तपशील", height=220)
    demand = st.text_area("आपली मागणी", height=140)

    if st.button("📝 तक्रार तयार करा", use_container_width=True):

        draft = f"""
**शासकीय तक्रार अर्ज**

प्रति,
{authority}

**विषय:** {subject}

**तक्रारीचा तपशील:**
{comp}

**मागणी:**
{demand}

**तक्रारदार:** सतीश अशोक प्रधान
**ठिकाण:** छत्रपती संभाजीनगर
**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="a4-container">{draft}</div>',
            unsafe_allow_html=True
        )

# =========================================================
# AFFIDAVIT
# =========================================================

elif st.session_state.active_module == "affidavit":

    st.markdown(
        '<div class="section-title">✏️ प्रतिज्ञापत्र</div>',
        unsafe_allow_html=True
    )

    aff = st.text_area("प्रतिज्ञापत्रातील घोषणा / मुद्दे", height=240)

    if st.button("📝 प्रतिज्ञापत्र तयार करा", use_container_width=True):

        draft = f"""
**प्रतिज्ञापत्र**

मी, सतीश अशोक प्रधान, छत्रपती संभाजीनगर,
खालीलप्रमाणे घोषित करतो:

{aff}

वरील माहिती माझ्या माहितीनुसार सत्य आहे.

**घोषणाकर्ता:** सतीश अशोक प्रधान
**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="a4-container">{draft}</div>',
            unsafe_allow_html=True
        )

# =========================================================
# CONSUMER
# =========================================================

elif st.session_state.active_module == "consumer":

    st.markdown(
        '<div class="section-title">🛒 ग्राहक मंच तक्रार</div>',
        unsafe_allow_html=True
    )

    company = st.text_input("विरोधातील व्यक्ती / कंपनी / सेवा प्रदाता")
    cons = st.text_area(
        "फसवणूक / सेवेत त्रुटी / तक्रारीचा तपशील",
        height=220
    )
    compensation = st.text_input("मागितलेली भरपाई")

    if st.button("📝 ग्राहक मंच अर्ज तयार करा", use_container_width=True):

        draft = f"""
**ग्राहक तक्रार अर्ज — प्राथमिक मसुदा**

**विरोधातील पक्ष:** {company}

**तक्रारीचा तपशील:**
{cons}

**मागितलेली भरपाई:** {compensation}

**तक्रारदार:** सतीश अशोक प्रधान
**ठिकाण:** छत्रपती संभाजीनगर
**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="a4-container">{draft}</div>',
            unsafe_allow_html=True
        )

# =========================================================
# DOCUMENTS
# =========================================================

elif st.session_state.active_module == "documents":

    st.markdown(
        '<div class="section-title">📂 दस्तऐवज / PDF</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-box">
        📄 PDF, फोटो किंवा इतर कागदपत्रे निवडा.
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "📎 कागदपत्र निवडा",
        type=["pdf", "jpg", "jpeg", "png", "docx"],
        accept_multiple_files=True
    )

    if uploaded:
        st.success(f"{len(uploaded)} कागदपत्रे निवडली आहेत.")

        for file in uploaded:
            st.write(f"📄 {file.name}")

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div style="
text-align:center;
font-size:10px;
color:#777;
padding:12px;
">
⚖️ RTI AI महा-सहाय्यक
<br>
सतीश अशोक प्रधान | छत्रपती संभाजीनगर
</div>
""", unsafe_allow_html=True)
