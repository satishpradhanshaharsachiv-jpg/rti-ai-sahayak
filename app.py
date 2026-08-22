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
# MOBILE APP CSS
# =========================================================

st.markdown("""
<style>

* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
}

.stApp {
    background: #f5f7fb;
}

/* मुख्य कंटेनर */
.block-container {
    max-width: 900px !important;
    padding-top: 12px !important;
    padding-left: 12px !important;
    padding-right: 12px !important;
    padding-bottom: 35px !important;
}

/* Streamlit वरची पट्टी */
header[data-testid="stHeader"] {
    height: 35px !important;
    background: transparent !important;
}

/* =========================================================
   HEADER
   ========================================================= */

.app-header {
    background: #ffffff;
    border-radius: 24px;
    padding: 20px 12px 16px 12px;
    text-align: center;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
    margin-bottom: 22px;
}

.app-title {
    font-size: 30px;
    font-weight: 900;
    color: #1d2739;
    margin-bottom: 8px;
}

.app-title span {
    color: #0aa678;
}

.app-tag {
    display: inline-block;
    background: #fff3c4;
    color: #b86b00;
    border: 2px dashed #e9ad25;
    border-radius: 25px;
    padding: 8px 17px;
    font-size: 14px;
    font-weight: 800;
    margin-bottom: 10px;
}

.app-info {
    color: #555;
    font-size: 13px;
    line-height: 1.7;
}

/* =========================================================
   SECTION TITLE
   ========================================================= */

.service-title {
    font-size: 25px;
    font-weight: 900;
    color: #202838;
    margin: 8px 0 15px 5px;
}

/* =========================================================
   3 x 3 GRID
   ========================================================= */

div[data-testid="column"] {
    padding: 6px !important;
}

/* सर्व बटणे */
div.stButton > button {

    width: 100% !important;

    min-height: 185px !important;
    height: 185px !important;

    border: none !important;
    border-radius: 25px !important;

    color: #ffffff !important;

    font-size: 18px !important;
    font-weight: 900 !important;

    white-space: pre-line !important;

    box-shadow:
        0 7px 18px rgba(0,0,0,0.16) !important;

    transition:
        transform 0.15s ease,
        box-shadow 0.15s ease !important;

    padding: 12px !important;
}

/* Touch effect */
div.stButton > button:hover {
    transform: translateY(-4px) !important;
    box-shadow:
        0 11px 25px rgba(0,0,0,0.22) !important;
}

div.stButton > button:active {
    transform: scale(0.96) !important;
}

/* =========================================================
   ROW 1 COLORS
   ========================================================= */

div[data-testid="stHorizontalBlock"]:nth-of-type(1)
div[data-testid="column"]:nth-child(1)
div.stButton > button {

    background: linear-gradient(
        145deg,
        #8bea70,
        #52c878
    ) !important;
}

div[data-testid="stHorizontalBlock"]:nth-of-type(1)
div[data-testid="column"]:nth-child(2)
div.stButton > button {

    background: linear-gradient(
        145deg,
        #ffc45c,
        #ff9f1c
    ) !important;
}

div[data-testid="stHorizontalBlock"]:nth-of-type(1)
div[data-testid="column"]:nth-child(3)
div.stButton > button {

    background: linear-gradient(
        145deg,
        #9ca9ff,
        #6378e8
    ) !important;
}

/* =========================================================
   ROW 2 COLORS
   ========================================================= */

div[data-testid="stHorizontalBlock"]:nth-of-type(2)
div[data-testid="column"]:nth-child(1)
div.stButton > button {

    background: linear-gradient(
        145deg,
        #c79cff,
        #8b4de8
    ) !important;
}

div[data-testid="stHorizontalBlock"]:nth-of-type(2)
div[data-testid="column"]:nth-child(2)
div.stButton > button {

    background: linear-gradient(
        145deg,
        #ff9ea9,
        #f16b7b
    ) !important;
}

div[data-testid="stHorizontalBlock"]:nth-of-type(2)
div[data-testid="column"]:nth-child(3)
div.stButton > button {

    background: linear-gradient(
        145deg,
        #ffb98e,
        #ff915e
    ) !important;
}

/* =========================================================
   ROW 3 COLORS
   ========================================================= */

div[data-testid="stHorizontalBlock"]:nth-of-type(3)
div[data-testid="column"]:nth-child(1)
div.stButton > button {

    background: linear-gradient(
        145deg,
        #8be2e4,
        #41b9bd
    ) !important;
}

div[data-testid="stHorizontalBlock"]:nth-of-type(3)
div[data-testid="column"]:nth-child(2)
div.stButton > button {

    background: linear-gradient(
        145deg,
        #8fb8ff,
        #5f8ee8
    ) !important;
}

div[data-testid="stHorizontalBlock"]:nth-of-type(3)
div[data-testid="column"]:nth-child(3)
div.stButton > button {

    background: linear-gradient(
        145deg,
        #b7a6ff,
        #806ce5
    ) !important;
}

/* =========================================================
   FORM DESIGN
   ========================================================= */

.stTextInput input,
.stTextArea textarea {

    border-radius: 14px !important;

    border: 1px solid #d9dfe9 !important;

    font-size: 16px !important;

    background: #ffffff !important;
}

/* Generate button */
.generate-btn button {

    min-height: 55px !important;

    border-radius: 15px !important;

    font-size: 17px !important;

    font-weight: 800 !important;
}

/* =========================================================
   DOCUMENT BOX
   ========================================================= */

.document-box {

    background: #ffffff;

    border-radius: 18px;

    padding: 22px;

    margin-top: 18px;

    box-shadow:
        0 5px 20px rgba(0,0,0,0.10);

    color: #111827;

    font-size: 15px;

    line-height: 1.9;
}

/* =========================================================
   INFO BOX
   ========================================================= */

.info-box {

    background: #eef5ff;

    border-left: 5px solid #4c8bf5;

    border-radius: 15px;

    padding: 15px;

    margin: 15px 0;

    color: #26344a;

    font-size: 14px;

}

/* =========================================================
   MOBILE
   ========================================================= */

@media screen and (max-width: 600px) {

    .block-container {

        padding-left: 6px !important;

        padding-right: 6px !important;

        padding-top: 8px !important;

    }

    .app-header {

        border-radius: 20px;

        padding: 15px 8px;

    }

    .app-title {

        font-size: 23px;

    }

    .app-tag {

        font-size: 12px;

        padding: 7px 12px;

    }

    .app-info {

        font-size: 11px;

    }

    .service-title {

        font-size: 22px;

        margin-left: 4px;

    }

    div[data-testid="column"] {

        padding: 4px !important;

    }

    div.stButton > button {

        min-height: 150px !important;

        height: 150px !important;

        border-radius: 20px !important;

        font-size: 15px !important;

        padding: 8px !important;

    }

}

/* अतिशय छोट्या स्क्रीनसाठी */
@media screen and (max-width: 380px) {

    div.stButton > button {

        min-height: 130px !important;

        height: 130px !important;

        font-size: 13px !important;

        border-radius: 17px !important;

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
<div class="app-header">

    <div class="app-title">
        ⚖️ <span>RTI AI</span> महा-सहाय्यक
    </div>

    <div class="app-tag">
        ⚡ घरबसल्या एका मिनिटात अर्ज तयार करा
    </div>

    <div class="app-info">
        👤 सतीश अशोक प्रधान
        &nbsp; | &nbsp;
        📱 ८६६८२३५३९५
        <br>
        📍 छत्रपती संभाजीनगर
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# LOGIN
# =========================================================

if not st.session_state.is_logged_in:

    st.markdown(
        '<div class="service-title">🔐 सुरक्षित मोबाईल प्रवेश</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-box">
        📱 तुमचा १० अंकी मोबाईल नंबर टाका आणि ॲप सुरू करा.
    </div>
    """, unsafe_allow_html=True)

    mobile = st.text_input(
        "मोबाईल नंबर",
        placeholder="१० अंकी मोबाईल नंबर",
        max_chars=10
    )

    if st.button(
        "🚀 ॲप सुरू करा",
        use_container_width=True
    ):

        if len(mobile) == 10 and mobile.isdigit():

            st.session_state.is_logged_in = True
            st.session_state.user_mobile = mobile
            st.session_state.active_module = "home"

            st.rerun()

        else:

            st.error(
                "कृपया अचूक १० अंकी मोबाईल नंबर टाका."
            )

    st.stop()


# =========================================================
# HOME SCREEN
# =========================================================

if st.session_state.active_module == "home":

    st.markdown("""
    <div class="service-title">
        📱 कायदेशीर सेवा निवडा
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # ROW 1
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "📄\nजोडपत्र 'अ'\n\nमाहिती अधिकार अर्ज",
            key="rti_button"
        ):

            st.session_state.active_module = "rti"
            st.rerun()

    with col2:

        if st.button(
            "⚖️\nप्रथम अपील\n\nकलम १९ अंतर्गत",
            key="appeal_button"
        ):

            st.session_state.active_module = "first_appeal"
            st.rerun()

    with col3:

        if st.button(
            "🏛️\nमाहिती आयोग\n\nराज्य माहिती आयोग",
            key="commission_button"
        ):

            st.session_state.active_module = "commission"
            st.rerun()


    # =====================================================
    # ROW 2
    # =====================================================

    col4, col5, col6 = st.columns(3)

    with col4:

        if st.button(
            "✨\nAI चॅट\n\nAI कायदेशीर सल्ला",
            key="ai_button"
        ):

            st.session_state.active_module = "ai_chat"
            st.rerun()

    with col5:

        if st.button(
            "📜\nकोर्ट याचिका\n\nयाचिका मसुदा तयार करा",
            key="court_button"
        ):

            st.session_state.active_module = "court"
            st.rerun()

    with col6:

        if st.button(
            "📢\nशासकीय तक्रार\n\nशासकीय तक्रार अर्ज",
            key="complaint_button"
        ):

            st.session_state.active_module = "complaint"
            st.rerun()


    # =====================================================
    # ROW 3
    # =====================================================

    col7, col8, col9 = st.columns(3)

    with col7:

        if st.button(
            "📜\nप्रतिज्ञापत्र\n\nप्रतिज्ञापत्र तयार करा",
            key="affidavit_button"
        ):

            st.session_state.active_module = "affidavit"
            st.rerun()

    with col8:

        if st.button(
            "🛒\nग्राहक मंच\n\nग्राहक तक्रार अर्ज",
            key="consumer_button"
        ):

            st.session_state.active_module = "consumer"
            st.rerun()

    with col9:

        if st.button(
            "📂\nदस्तऐवज / PDF\n\nदस्तऐवज वाचक",
            key="documents_button"
        ):

            st.session_state.active_module = "documents"
            st.rerun()


    st.markdown("""
    <div class="info-box">
        🛡️ <b>सुरक्षित प्रवेश</b><br>
        तुमचा डेटा फक्त तुमच्या मदतीसाठी वापरला जातो.
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# BACK BUTTON
# =========================================================

else:

    if st.button(
        "🏠  मुख्य पृष्ठावर जा",
        use_container_width=True
    ):

        st.session_state.active_module = "home"

        st.rerun()


# =========================================================
# RTI APPLICATION
# =========================================================

if st.session_state.active_module == "rti":

    st.markdown(
        '<div class="service-title">📄 जोडपत्र \'अ\'</div>',
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
        height=200,
        placeholder="मागायची माहिती लिहा..."
    )

    if st.button(
        "📝 अर्जाचा मसुदा तयार करा",
        use_container_width=True
    ):

        draft = f"""
### माहिती अधिकाराचा अर्ज

**प्रति,**  
जन माहिती अधिकारी,  
{dept}

**विषय:** {subject}

**माहितीचा तपशील:**  
{details}

**अर्जदार:**  
सतीश अशोक प्रधान

**ठिकाण:** छत्रपती संभाजीनगर

**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="document-box">{draft}</div>',
            unsafe_allow_html=True
        )


# =========================================================
# FIRST APPEAL
# =========================================================

elif st.session_state.active_module == "first_appeal":

    st.markdown(
        '<div class="service-title">⚖️ प्रथम अपील</div>',
        unsafe_allow_html=True
    )

    officer = st.text_input(
        "प्रथम अपिलीय अधिकारी व पत्ता"
    )

    reason = st.text_area(
        "अपिलाचे कारण",
        height=220
    )

    if st.button(
        "📝 प्रथम अपील तयार करा",
        use_container_width=True
    ):

        draft = f"""
### प्रथम अपील अर्ज

**प्रति:**  
{officer}

**अपिलाचे कारण:**  
{reason}

**अपीलार्थी:**  
सतीश अशोक प्रधान

**ठिकाण:** छत्रपती संभाजीनगर

**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="document-box">{draft}</div>',
            unsafe_allow_html=True
        )


# =========================================================
# INFORMATION COMMISSION
# =========================================================

elif st.session_state.active_module == "commission":

    st.markdown(
        '<div class="service-title">🏛️ माहिती आयोग</div>',
        unsafe_allow_html=True
    )

    details = st.text_area(
        "द्वितीय अपील / तक्रारीचा तपशील",
        height=250
    )

    if st.button(
        "📝 आयोग अर्ज तयार करा",
        use_container_width=True
    ):

        draft = f"""
### द्वितीय अपील / तक्रार

**तपशील:**  
{details}

**अर्जदार:**  
सतीश अशोक प्रधान

**ठिकाण:** छत्रपती संभाजीनगर

**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="document-box">{draft}</div>',
            unsafe_allow_html=True
        )


# =========================================================
# AI CHAT
# =========================================================

elif st.session_state.active_module == "ai_chat":

    st.markdown(
        '<div class="service-title">✨ AI कायदेशीर सल्लागार</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-box">
        ✨ RTI, अपील, तक्रार, कोर्ट याचिका किंवा इतर कायदेशीर प्रश्न विचारा.
    </div>
    """, unsafe_allow_html=True)

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(
                message["content"]
            )

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

        if (
            "RTI" in prompt.upper()
            or "आरटीआय" in prompt
            or "माहिती अधिकार" in prompt
        ):

            answer = """
माहिती अधिकारासंबंधी तुमचा प्रश्न नोंदवला आहे.
जोडपत्र 'अ' विभागातून माहिती अधिकाराचा अर्ज तयार करता येईल.
"""

        elif "अपील" in prompt:

            answer = """
तुमच्या प्रकरणासाठी प्रथम अपील किंवा पुढील अपील प्रक्रियेचा विचार करता येईल.
तुमच्याकडे असलेला अर्ज आणि मिळालेले उत्तर दिल्यास त्यावर आधारित मसुदा तयार करता येईल.
"""

        elif "तक्रार" in prompt:

            answer = """
तक्रारीसाठी संबंधित अधिकारी, घटना, पुरावे आणि तुमची मागणी स्पष्टपणे द्या.
शासकीय तक्रार विभागातून मसुदा तयार करता येईल.
"""

        else:

            answer = f"""
सतीशजी,

तुमचा प्रश्न:

**{prompt}**

कृपया अधिक तपशील दिल्यास त्यानुसार योग्य अर्ज किंवा कायदेशीर मसुदा तयार करता येईल.
"""

        with st.chat_message("assistant"):

            st.markdown(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })


# =========================================================
# COURT PETITION
# =========================================================

elif st.session_state.active_module == "court":

    st.markdown(
        '<div class="service-title">📜 कोर्ट याचिका</div>',
        unsafe_allow_html=True
    )

    facts = st.text_area(
        "प्रकरणाची हकीकत",
        height=250
    )

    demand = st.text_area(
        "मागणी / दिलासा",
        height=180
    )

    if st.button(
        "📝 याचिका मसुदा तयार करा",
        use_container_width=True
    ):

        draft = f"""
### कोर्ट याचिका — प्राथमिक मसुदा

**प्रकरणाची हकीकत:**  
{facts}

**मागणी / दिलासा:**  
{demand}

**याचिकाकर्ता:**  
सतीश अशोक प्रधान

**ठिकाण:** छत्रपती संभाजीनगर

**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}

> हा प्राथमिक मसुदा आहे. दाखल करण्यापूर्वी संबंधित कायदेशीर तज्ज्ञाकडून तपासणी करावी.
"""

        st.markdown(
            f'<div class="document-box">{draft}</div>',
            unsafe_allow_html=True
        )


# =========================================================
# GOVERNMENT COMPLAINT
# =========================================================

elif st.session_state.active_module == "complaint":

    st.markdown(
        '<div class="service-title">📢 शासकीय तक्रार</div>',
        unsafe_allow_html=True
    )

    officer = st.text_input(
        "तक्रार कोणाकडे करायची?"
    )

    subject = st.text_input(
        "तक्रारीचा विषय"
    )

    complaint = st.text_area(
        "तक्रारीचा तपशील",
        height=230
    )

    demand = st.text_area(
        "आपली मागणी",
        height=150
    )

    if st.button(
        "📝 तक्रार तयार करा",
        use_container_width=True
    ):

        draft = f"""
### शासकीय तक्रार अर्ज

**प्रति:**  
{officer}

**विषय:**  
{subject}

**तक्रारीचा तपशील:**  
{complaint}

**मागणी:**  
{demand}

**तक्रारदार:**  
सतीश अशोक प्रधान

**ठिकाण:** छत्रपती संभाजीनगर

**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="document-box">{draft}</div>',
            unsafe_allow_html=True
        )


# =========================================================
# AFFIDAVIT
# =========================================================

elif st.session_state.active_module == "affidavit":

    st.markdown(
        '<div class="service-title">📜 प्रतिज्ञापत्र</div>',
        unsafe_allow_html=True
    )

    declaration = st.text_area(
        "प्रतिज्ञापत्रातील घोषणा / मुद्दे",
        height=250
    )

    if st.button(
        "📝 प्रतिज्ञापत्र तयार करा",
        use_container_width=True
    ):

        draft = f"""
### प्रतिज्ञापत्र

मी, **सतीश अशोक प्रधान**, छत्रपती संभाजीनगर,
खालीलप्रमाणे घोषित करतो:

{declaration}

वरील माहिती माझ्या माहितीनुसार सत्य आहे.

**घोषणाकर्ता:**  
सतीश अशोक प्रधान

**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="document-box">{draft}</div>',
            unsafe_allow_html=True
        )


# =========================================================
# CONSUMER FORUM
# =========================================================

elif st.session_state.active_module == "consumer":

    st.markdown(
        '<div class="service-title">🛒 ग्राहक मंच</div>',
        unsafe_allow_html=True
    )

    opposite_party = st.text_input(
        "विरोधातील व्यक्ती / कंपनी / सेवा प्रदाता"
    )

    complaint = st.text_area(
        "तक्रारीचा तपशील",
        height=230
    )

    compensation = st.text_input(
        "मागितलेली भरपाई"
    )

    if st.button(
        "📝 ग्राहक मंच अर्ज तयार करा",
        use_container_width=True
    ):

        draft = f"""
### ग्राहक मंच तक्रार — प्राथमिक मसुदा

**विरोधातील पक्ष:**  
{opposite_party}

**तक्रारीचा तपशील:**  
{complaint}

**मागितलेली भरपाई:**  
{compensation}

**तक्रारदार:**  
सतीश अशोक प्रधान

**ठिकाण:** छत्रपती संभाजीनगर

**दिनांक:** {datetime.date.today().strftime('%d/%m/%Y')}
"""

        st.markdown(
            f'<div class="document-box">{draft}</div>',
            unsafe_allow_html=True
        )


# =========================================================
# DOCUMENT / PDF
# =========================================================

elif st.session_state.active_module == "documents":

    st.markdown(
        '<div class="service-title">📂 दस्तऐवज / PDF</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-box">
        📄 PDF, फोटो किंवा इतर कागदपत्रे येथे निवडता येतील.
        पुढील टप्प्यात AI कडून त्यातील मजकूर वाचून अर्ज तयार करण्याची सुविधा जोडता येईल.
    </div>
    """, unsafe_allow_html=True)

    files = st.file_uploader(
        "📎 कागदपत्र निवडा",
        type=[
            "pdf",
            "jpg",
            "jpeg",
            "png",
            "docx"
        ],
        accept_multiple_files=True
    )

    if files:

        st.success(
            f"✅ {len(files)} कागदपत्रे निवडली."
        )

        for file in files:

            st.write(
                "📄 " + file.name
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<br>

<div style="
text-align:center;
color:#777;
font-size:11px;
padding:18px;
">

⚖️ RTI AI महा-सहाय्यक

<br>

सतीश अशोक प्रधान | छत्रपती संभाजीनगर

</div>

""", unsafe_allow_html=True)
