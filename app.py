import streamlit as st
import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="RTI AI महा-सहाय्यक",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# MOBILE-FIRST CSS
# =========================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: "Noto Sans Devanagari", "Noto Sans", sans-serif;
}

/* पूर्ण ॲप */
.stApp {
    background: #f5f7fb;
}

/* Desktop width कमी */
.block-container {
    max-width: 720px !important;
    padding-top: 10px !important;
    padding-left: 12px !important;
    padding-right: 12px !important;
    padding-bottom: 30px !important;
}

/* वरचा Streamlit header कमी */
header[data-testid="stHeader"] {
    background: transparent !important;
    height: 35px !important;
}

/* Header */
.mobile-header {
    background: white;
    border-radius: 20px;
    padding: 15px 10px 12px 10px;
    margin-bottom: 10px;
    text-align: center;
    box-shadow: 0 3px 15px rgba(0,0,0,0.08);
}

.mobile-header-title {
    font-size: 25px;
    font-weight: 900;
    color: #08a678;
    margin: 0;
}

.mobile-header-sub {
    font-size: 12px;
    color: #666;
    margin-top: 4px;
}

.tag {
    display: inline-block;
    margin-top: 8px;
    padding: 7px 15px;
    border-radius: 25px;
    background: #fff3cd;
    border: 1px dashed #e0a800;
    color: #b06b00;
    font-size: 13px;
    font-weight: 800;
}

/* =========================================================
   MOBILE APP BUTTONS
   ========================================================= */

div[data-testid="column"] {
    padding: 4px !important;
}

div.stButton > button {
    width: 100% !important;
    min-height: 105px !important;
    height: 105px !important;

    border: none !important;
    border-radius: 23px !important;

    color: white !important;
    font-size: 16px !important;
    font-weight: 900 !important;

    box-shadow: 0 5px 12px rgba(0,0,0,0.18) !important;

    white-space: pre-line !important;

    transition: transform 0.15s ease,
                box-shadow 0.15s ease !important;
}

div.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 18px rgba(0,0,0,0.25) !important;
}

div.stButton > button:active {
    transform: scale(0.96) !important;
}

/* प्रत्येक बटणासाठी रंग */

div[data-testid="column"]:nth-child(1)
div.stButton > button {
    background: linear-gradient(135deg,#00b894,#00a878) !important;
}

div[data-testid="column"]:nth-child(2)
div.stButton > button {
    background: linear-gradient(135deg,#ff5f6d,#ff9966) !important;
}

div[data-testid="column"]:nth-child(3)
div.stButton > button {
    background: linear-gradient(135deg,#19243d,#273657) !important;
}

/* दुसरी row */
div[data-testid="stHorizontalBlock"]:nth-of-type(2)
div[data-testid="column"]:nth-child(1)
div.stButton > button {
    background: linear-gradient(135deg,#6424c8,#873de8) !important;
}

div[data-testid="stHorizontalBlock"]:nth-of-type(2)
div[data-testid="column"]:nth-child(2)
div.stButton > button {
    background: linear-gradient(135deg,#ef233c,#d90429) !important;
}

div[data-testid="stHorizontalBlock"]:nth-of-type(2)
div[data-testid="column"]:nth-child(3)
div.stButton > button {
    background: linear-gradient(135deg,#ff7a00,#e85d04) !important;
}

/* तिसरी row */
div[data-testid="stHorizontalBlock"]:nth-of-type(3)
div[data-testid="column"]:nth-child(1)
div.stButton > button {
    background: linear-gradient(135deg,#0099cc,#0077b6) !important;
}

div[data-testid="stHorizontalBlock"]:nth-of-type(3)
div[data-testid="column"]:nth-child(2)
div.stButton > button {
    background: linear-gradient(135deg,#16a085,#138d75) !important;
}

div[data-testid="stHorizontalBlock"]:nth-of-type(3)
div[data-testid="column"]:nth-child(3)
div.stButton > button {
    background: linear-gradient(135deg,#6c5ce7,#4834d4) !important;
}

/* Section title */
.section-title {
    font-size: 24px;
    font-weight: 900;
    color: #202738;
    margin-top: 18px;
    margin-bottom: 10px;
}

/* सूचना बॉक्स */
.info-box {
    background: #eef4ff;
    border-left: 5px solid #3b82f6;
    border-radius: 15px;
    padding: 14px;
    font-size: 15px;
    margin-bottom: 15px;
}

/* Form */
.stTextInput input,
.stTextArea textarea {
    border-radius: 12px !important;
    border: 1px solid #d7dce5 !important;
    font-size: 16px !important;
}

/* Generate button */
.generate-button button {
    border-radius: 14px !important;
}

/* Document */
.a4-container {
    background: white;
    color: #111827;
    border-radius: 15px;
    padding: 20px;
    margin-top: 15px;
    line-height: 1.8;
    box-shadow: 0 3px 15px rgba(0,0,0,0.10);
}

/* Mobile */
@media (max-width: 600px) {

    .block-container {
        padding-left: 8px !important;
        padding-right: 8px !important;
    }

    .mobile-header-title {
        font-size: 22px;
    }

    div.stButton > button {
        min-height: 105px !important;
        height: 105px !important;
        font-size: 14px !important;
        border-radius: 20px !important;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if "active_module" not in st.session_state:
    st.session_state.active_module = "home"

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="mobile-header">

    <div class="mobile-header-title">
        ⚖️ RTI AI महा-सहाय्यक
    </div>

    <div class="tag">
        ⚡ घरबसल्या एका मिनिटात अर्ज तयार करा
    </div>

    <div class="mobile-header-sub">
        👤 सतीश अशोक प्रधान | 📱 ८६६८२३५३९५
        <br>
        छत्रपती संभाजीनगर
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# LOGIN
# =========================================================

if not st.session_state.is_logged_in:

    st.markdown("""
    <div class="section-title" style="text-align:center;">
        🔐 सुरक्षित मोबाईल प्रवेश
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        📱 तुमचा १० अंकी मोबाईल नंबर टाकून ॲप सुरू करा.
    </div>
    """, unsafe_allow_html=True)

    mobile = st.text_input(
        "मोबाईल नंबर",
        placeholder="१० अंकी मोबाईल नंबर",
        max_chars=10
    )

    if st.button("🚀 ॲप सुरू करा", use_container_width=True):

        if len(mobile) == 10 and mobile.isdigit():

            st.session_state.is_logged_in = True
            st.session_state.user_mobile = mobile
            st.session_state.active_module = "home"

            st.rerun()

        else:
            st.error("कृपया अचूक १० अंकी मोबाईल नंबर टाका.")

    st.stop()


# =========================================================
# HOME MENU
# =========================================================

if st.session_state.active_module == "home":

    st.markdown("""
    <div class="section-title">
        📱 कायदेशीर सेवा निवडा
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # ROW 1
    # =========================

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

    # =========================
    # ROW 2
    # =========================

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

    # =========================
    # ROW 3
    # =========================

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

    st.markdown("---")

    st.markdown("""
    <div class="info-box">
        💡 <b>टीप:</b> वरील कोणतेही बटन निवडा आणि संबंधित अर्ज किंवा कायदेशीर कागदपत्र तयार करा.
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# BACK BUTTON
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

    dept = st.text_input(
        "जन माहिती अधिकारी, विभाग व पत्ता",
        placeholder="उदा. जिल्हाधिकारी कार्यालय..."
    )

    subject = st.text_input(
        "माहितीचा विषय",
        placeholder="विषय लिहा..."
    )

    details = st.text_area(
        "माहितीचा तपशील",
        placeholder="मागायची माहिती येथे लिहा...",
        height=180
    )

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

    fa_dept = st.text_input(
        "प्रथम अपिलीय अधिकारी व पत्ता"
    )

    reason = st.text_area(
        "अपिलाचे कारण",
        height=180
    )

    if st.button("📝 प्रथम अपील तयार करा", use_container_width=True):

        draft = f"""
**प्रथम अपील अर्ज**

प्रति,  
{fa_dept}

**अपिलाचे कारण:**  
{reason}

**अपीलार्थी:**  
सतीश अशोक प्रधान  
छत्रपती संभाजीनगर

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
        "आयोगासाठी तक्रार / द्वितीय अपील तपशील",
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
        ✨ RTI, प्रथम अपील, तक्रार किंवा कायदेशीर प्रक्रियेबद्दल प्रश्न विचारा.
        <br>
        📎 पुढे कागदपत्र / फोटो जोडण्याची सुविधा देखील जोडता येईल.
    </div>
    """, unsafe_allow_html=True)

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input(
        "तुमचा प्रश्न येथे लिहा..."
    )

    if prompt:

        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        # सध्या basic response
        if (
            "आरटीआय" in prompt
            or "RTI" in prompt.upper()
            or "माहिती" in prompt
        ):

            response = """
माहिती अधिकारासंबंधी प्रश्नासाठी प्रथम जोडपत्र 'अ' वापरून अर्ज तयार करता येईल.
तुमचा प्रश्न अधिक स्पष्ट दिल्यास संबंधित अर्जाचा मसुदा तयार करता येईल.
"""

        elif "अपील" in prompt:

            response = """
माहिती न मिळाल्यास किंवा अपूर्ण माहिती मिळाल्यास प्रथम अपील प्रक्रियेचा विचार करता येतो.
तुमच्याकडे असलेला RTI अर्ज आणि उत्तर दिल्यास त्यावर आधारित मसुदा तयार करता येईल.
"""

        elif "तक्रार" in prompt:

            response = """
तक्रारीसाठी संबंधित कार्यालय, विषय, घटना आणि मागणी स्पष्टपणे लिहा.
त्यावर आधारित शासकीय तक्रार अर्ज तयार करता येईल.
"""

        else:

            response = f"""
सतीशजी, तुमचा प्रश्न:

**{prompt}**

या विषयासाठी संबंधित विभाग निवडा किंवा अधिक तपशील द्या.
"""

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })


# =========================================================
# COURT PETITION
# =========================================================

elif st.session_state.active_module == "court":

    st.markdown(
        '<div class="section-title">📜 कोर्ट याचिका मसुदा</div>',
        unsafe_allow_html=True
    )

    facts = st.text_area(
        "प्रकरणाची हकीकत",
        height=250
    )

    relief = st.text_area(
        "मागणी / दिलासा",
        height=150
    )

    if st.button("📝 याचिका मसुदा तयार करा", use_container_width=True):

        draft = f"""
**कोर्ट याचिका — प्राथमिक मसुदा**

**प्रकरणाची हकीकत:**  
{facts}

**मागणी / दिलासा:**  
{relief}

**याचिकाकर्ता:**  
सतीश अशोक प्रधान

**ठिकाण:** छत्रपती संभाजीनगर  
**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}

*टीप: हा प्राथमिक मसुदा आहे. दाखल करण्यापूर्वी संबंधित कायदेशीर तज्ज्ञाकडून तपासणी करावी.*
"""

        st.markdown(
            f'<div class="a4-container">{draft}</div>',
            unsafe_allow_html=True
        )


# =========================================================
# GOVERNMENT COMPLAINT
# =========================================================

elif st.session_state.active_module == "complaint":

    st.markdown(
        '<div class="section-title">📣 शासकीय तक्रार अर्ज</div>',
        unsafe_allow_html=True
    )

    authority = st.text_input(
        "तक्रार कोणाकडे करायची आहे?"
    )

    subject = st.text_input(
        "तक्रारीचा विषय"
    )

    comp = st.text_area(
        "तक्रारीचा संपूर्ण तपशील",
        height=250
    )

    demand = st.text_area(
        "आपली मागणी",
        height=150
    )

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

**तक्रारदार:**  
सतीश अशोक प्रधान  
छत्रपती संभाजीनगर

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

    aff = st.text_area(
        "प्रतिज्ञापत्रातील घोषणा / मुद्दे",
        height=250
    )

    if st.button("📝 प्रतिज्ञापत्र तयार करा", use_container_width=True):

        draft = f"""
**प्रतिज्ञापत्र**

मी, सतीश अशोक प्रधान, छत्रपती संभाजीनगर,
खालीलप्रमाणे घोषित करतो:

{aff}

वरील माहिती माझ्या माहितीनुसार सत्य आहे.

**घोषणाकर्ता:**  
सतीश अशोक प्रधान

**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="a4-container">{draft}</div>',
            unsafe_allow_html=True
        )


# =========================================================
# CONSUMER FORUM
# =========================================================

elif st.session_state.active_module == "consumer":

    st.markdown(
        '<div class="section-title">🛒 ग्राहक मंच तक्रार</div>',
        unsafe_allow_html=True
    )

    company = st.text_input(
        "विरोधातील व्यक्ती / कंपनी / सेवा प्रदाता"
    )

    cons = st.text_area(
        "फसवणूक / सेवेत त्रुटी / तक्रारीचा तपशील",
        height=230
    )

    compensation = st.text_input(
        "मागितलेली भरपाई"
    )

    if st.button("📝 ग्राहक मंच अर्ज तयार करा", use_container_width=True):

        draft = f"""
**ग्राहक तक्रार अर्ज — प्राथमिक मसुदा**

**विरोधातील पक्ष:**  
{company}

**तक्रारीचा तपशील:**  
{cons}

**मागितलेली भरपाई:**  
{compensation}

**तक्रारदार:**  
सतीश अशोक प्रधान

**ठिकाण:** छत्रपती संभाजीनगर  
**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="a4-container">{draft}</div>',
            unsafe_allow_html=True
        )


# =========================================================
# DOCUMENTS / PDF
# =========================================================

elif st.session_state.active_module == "documents":

    st.markdown(
        '<div class="section-title">📂 दस्तऐवज / PDF</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-box">
        📄 या विभागात पुढे तयार केलेले अर्ज,
        PDF, फोटो आणि इतर कागदपत्रे व्यवस्थापित करता येतील.
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "📎 कागदपत्र निवडा",
        type=["pdf", "jpg", "jpeg", "png", "docx"],
        accept_multiple_files=True
    )

    if uploaded:

        st.success(
            f"{len(uploaded)} कागदपत्रे निवडली आहेत."
        )

        for file in uploaded:

            st.write(
                f"📄 {file.name}"
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<br>
<div style="
text-align:center;
font-size:11px;
color:#777;
padding:15px;
">
⚖️ RTI AI महा-सहाय्यक
<br>
सतीश अशोक प्रधान | छत्रपती संभाजीनगर
</div>
""", unsafe_allow_html=True)
