import streamlit as st
import google.generativeai as genai
import datetime
import json
import io
import urllib.parse
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# ==============================================================================
# १. पेज कॉन्फिगरेशन आणि स्क्रीनशॉट प्रमाणे कस्टम CSS (Gradient Cards & Layout)
# ==============================================================================
st.set_page_config(
    page_title="आकांक्षा AI कायदेशीर व प्रशासकीय महा-सहाय्यक",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Mukta:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Mukta', sans-serif !important;
        background-color: #F8FAFC !important;
        color: #1E293B !important;
    }

    /* मुख्य शीर्षक डिझाईन */
    .main-title {
        font-size: 1.6rem !important;
        font-weight: 800;
        text-align: center;
        color: #0F172A;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #64748B;
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 20px;
    }

    /* स्क्रीनशॉट प्रमाणे कलरफुल ग्रिड बटनांचे डिझाईन */
    .stButton > button {
        width: 100% !important;
        height: 95px !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        border-radius: 18px !important;
        border: none !important;
        color: #FFFFFF !important;
        box-shadow: 0 6px 15px rgba(0,0,0,0.15) !important;
        transition: transform 0.2s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .stButton > button:hover {
        transform: scale(0.98);
    }

    /* विविध ग्रेडियंट्स (स्क्रीनशॉट प्रमाणे) */
    div.row-widget.stButton:nth-child(1) button { background: linear-gradient(135deg, #10B981, #059669) !important; }
    
    /* प्रीव्ह्यू बॉक्स */
    .draft-preview {
        background-color: #F1F5F9;
        color: #0F172A;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #3B82F6;
        font-size: 1rem;
        line-height: 1.7;
        white-space: pre-wrap;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# २. सेशन्स आणि स्टेट मॅनेजमेंट
# ==============================================================================
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "home"
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'draft_history' not in st.session_state:
    st.session_state.draft_history = []
if 'generated_draft' not in st.session_state:
    st.session_state.generated_draft = ""

# ==============================================================================
# ३. हेल्पर फंक्शन्स (AI & Doc Generators)
# ==============================================================================
def get_ai_response(prompt):
    api_key = st.secrets.get("GEMINI_API_KEY", None)
    if not api_key:
        return "कृपया Streamlit Secrets मध्ये 'GEMINI_API_KEY' जोडा."
    
    genai.configure(api_key=api_key)
    models = ['gemini-2.5-flash', 'gemini-2.0-flash', 'gemini-1.5-flash', 'gemini-1.5-pro']
    
    for model_name in models:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            if response and response.text:
                return response.text
        except Exception:
            continue
    return "माफ करा, सर्व AI मॉडेल्स सध्या व्यस्त आहेत."

def generate_docx(text):
    doc = Document()
    doc.add_heading('आकांक्षा AI कायदेशीर मसुदा', level=1)
    for line in text.split('\n'):
        doc.add_paragraph(line)
    bio = io.BytesIO()
    doc.save(bio)
    bio.seek(0)
    return bio

def generate_pdf(text):
    bio = io.BytesIO()
    doc = SimpleDocTemplate(bio, pagesize=letter)
    styles = getSampleStyleSheet()
    style = ParagraphStyle('Normal', fontName='Helvetica', fontSize=10, leading=14)
    story = [Paragraph("<b>आकांक्षा AI कायदेशीर मसुदा</b>", styles['Heading1']), Spacer(1, 12)]
    for paragraph in text.split('\n\n'):
        story.append(Paragraph(paragraph.replace('\n', '<br/>'), style))
        story.append(Spacer(1, 8))
    doc.build(story)
    bio.seek(0)
    return bio

def get_share_links(text):
    encoded_text = urllib.parse.quote(text[:1000] + "...\n\n(पूर्ण मसुदा आकांक्षा AI द्वारे तयार केला आहे.)")
    return f"https://api.whatsapp.com/send?text={encoded_text}", f"mailto:?subject=कायदेशीर मसुदा&body={encoded_text}"

# ==============================================================================
# ४. हेडर व नॅव्हिगेशन
# ==============================================================================
st.markdown('<div class="main-title">⚖️ आकांक्षा AI महा-सहाय्यक</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">संकल्पना: सतीश अशोक प्रधान | छत्रपती संभाजीनगर</div>', unsafe_allow_html=True)

col_h1, col_h2, col_h3 = st.columns(3)
with col_h1:
    if st.button("🏠 होम", key="nav_home"): st.session_state.active_tab = "home"; st.rerun()
with col_h2:
    if st.button("📚 कलमे", key="nav_lib"): st.session_state.active_tab = "library"; st.rerun()
with col_h3:
    if st.button("📜 इतिहास", key="nav_hist"): st.session_state.active_tab = "history"; st.rerun()

st.markdown("---")

# ==============================================================================
# ५. मुख्य होमपेज - स्क्रीनशॉट प्रमाणे २ ग्रिड कॉलम्स रचना
# ==============================================================================
if st.session_state.active_tab == "home":
    
    # 1 ली जोडी (जोडपत्र 'अ' आणि प्रथम अपील)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📄\nजोडपत्र 'अ'", key="b1"): st.session_state.active_tab = "rti_a"; st.rerun()
    with c2:
        if st.button("⚖️\nप्रथम अपील", key="b2"): st.session_state.active_tab = "rti_b"; st.rerun()

    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

    # 2 री जोडी (माहिती आयोग / द्वितीय अपील आणि AI चॅट)
    c3, c4 = st.columns(2)
    with c3:
        if st.button("🏛️\nमाहिती आयोग", key="b3"): st.session_state.active_tab = "rti_c"; st.rerun()
    with c4:
        if st.button("✨\nAI चॅट", key="b4"): st.session_state.active_tab = "ai_chat"; st.rerun()

    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

    # 3 री जोडी (कोर्ट याचिका आणि शासकीय तक्रार)
    c5, c6 = st.columns(2)
    with c5:
        if st.button("📜\nकोर्ट याचिका", key="b5"): st.session_state.active_tab = "court"; st.rerun()
    with c6:
        if st.button("📢\nशासकीय तक्रार", key="b6"): st.session_state.active_tab = "govt"; st.rerun()

    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

    # 4 थी जोडी (आरटीआय ऑनलाइन आणि ग्राहक मंच)
    c7, c8 = st.columns(2)
    with c7:
        if st.button("🌐\nआरटीआय पोर्टल सहाय्य", key="b7"): st.session_state.active_tab = "affidavit"; st.rerun()
    with c8:
        if st.button("🛒\nग्राहक मंच", key="b8"): st.session_state.active_tab = "consumer"; st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    
    # स्क्रीनशॉट प्रमाणे खाली थेट चॅट इनपुट बॉक्स
    home_chat_input = st.chat_input("AI ला कायदेशीर प्रश्न विचारா...")
    if home_chat_input:
        st.session_state.active_tab = "ai_chat"
        st.session_state.chat_history.append({"role": "user", "content": home_chat_input})
        st.rerun()

# ==============================================================================
# ६. जोडपत्र 'अ' (कलम ६(१))
# ==============================================================================
elif st.session_state.active_tab == "rti_a":
    st.header("📄 जोडपत्र 'अ' - माहिती अधिकार अर्ज (कलम ६(१))")
    with st.form("form_rti_a"):
        applicant_name = st.text_input("अर्जदाराचे पूर्ण नाव:", value="सतीश अशोक प्रधान")
        pio_office = st.text_input("जन माहिती अधिकारी / कार्यालय:", value="जन माहिती अधिकारी, जिल्हाधिकारी कार्यालय, छत्रपती संभाजीनगर")
        subject = st.text_input("माहितीचा विषय:", value="प्रशासकीय कामाचा निधी व खर्च तपशील")
        details = st.text_area("माहितीचे मुद्देवार वर्णन:", value="१. उपरोक्त कालावधीत मंजूर झालेल्या सर्व निधीची सत्यप्रत.")
        submit_a = st.form_submit_button("🚀 मसुदा तयार करा")

    if submit_a:
        draft = f"परिशिष्ट / जोडपत्र 'अ'\nप्रति, {pio_office}\nअर्जदार: {applicant_name}\nविषय: {subject}\nतपशील: {details}"
        st.session_state.generated_draft = draft

# (इतर सर्व मॉड्यूल्स जसेच्या तसे पुढे जोडू शकता...)

# ==============================================================================
# मसुदा प्रीव्ह्यू आणि डाऊनलोड सेक्शन
# ==============================================================================
if st.session_state.generated_draft and st.session_state.active_tab not in ["home", "library", "history", "ai_chat"]:
    st.markdown("---")
    st.subheader("📋 तयार झालेला मसुदा:")
    st.markdown(f'<div class="draft-preview">{st.session_state.generated_draft}</div>', unsafe_allow_html=True)
    
    col_txt, col_docx, col_pdf = st.columns(3)
    with col_txt:
        st.download_button("📄 TXT डाऊनलोड", data=st.session_state.generated_draft, file_name="draft.txt")
    with col_docx:
        st.download_button("📝 Word डाऊनलोड", data=generate_docx(st.session_state.generated_draft), file_name="draft.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    with col_pdf:
        st.download_button("🔴 PDF डाऊनलोड", data=generate_pdf(st.session_state.generated_draft), file_name="draft.pdf", mime="application/pdf")
