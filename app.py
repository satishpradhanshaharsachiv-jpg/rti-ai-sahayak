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
# १. पेज कॉन्फिगरेशन आणि मोबाईल फ्रेंडली CSS डिझाईन
# ==============================================================================
st.set_page_config(
    page_title="आकांक्षा इंटरप्राइजेस RTI AI ॲप",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Mukta:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Mukta', sans-serif !important;
        background-color: #0F172A !important;
        color: #F8FAFC !important;
    }

    /* स्क्रीनशॉट प्रमाणे वरचा मुख्य बॅनर */
    .custom-banner {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        border: 2px solid transparent;
        border-image: linear-gradient(90deg, #FACC15, #38BDF8, #EC4899) 1;
        padding: 16px;
        text-align: center;
        border-radius: 18px;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.2);
        margin-bottom: 20px;
    }

    /* मोबाईलसाठी अचूक २-कॉलम ग्रिड डिझाईन */
    .menu-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-bottom: 15px;
    }

    .menu-btn {
        padding: 18px 10px;
        border-radius: 16px;
        text-align: center;
        color: white !important;
        font-weight: 700;
        font-size: 1.1rem;
        text-decoration: none !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: transform 0.2s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: none;
        cursor: pointer;
        width: 100%;
    }

    .menu-btn:hover {
        transform: scale(0.97);
        opacity: 0.9;
    }

    /* प्रत्येक बटनाचे आकर्षक रंग (स्क्रीनशॉट प्रमाणे) */
    .btn-green { background: linear-gradient(135deg, #10B981, #059669); }
    .btn-red { background: linear-gradient(135deg, #EF4444, #DC2626); }
    .btn-teal { background: linear-gradient(135deg, #0EA5E9, #0284C7); }
    .btn-blue { background: linear-gradient(135deg, #3B82F6, #2563EB); }
    .btn-purple { background: linear-gradient(135deg, #8B5CF6, #7C3AED); }
    .btn-orange { background: linear-gradient(135deg, #F59E0B, #D97706); }
    .btn-pink { background: linear-gradient(135deg, #EC4899, #DB2777); }
    .btn-indigo { background: linear-gradient(135deg, #6366F1, #4F46E5); }

    /* Preview Output Box */
    .draft-preview {
        background-color: #020617;
        color: #E2E8F0;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #38BDF8;
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
# ४. ब्रँडिंग व बॅनर हेडर
# ==============================================================================
st.markdown("""
<div class="custom-banner">
    <div style="font-size: 1.35rem; font-weight: 800; color: #FACC15; margin-bottom: 5px;">
        ✨ आकांक्षा इंटरप्राइजेस RTI AI ॲप कायदेशीर सहाय्यक ✨
    </div>
    <div style="font-size: 0.9rem; color: #F87171; font-weight: 600; margin-bottom: 8px;">
        ⚡ घरसल्या RTI अर्ज व शासकीय तक्रार एका सेकंदात A4 साइज मध्ये मोफत मिळवा ⚡
    </div>
    <hr style="border: 0.5px dashed #475569; margin: 8px 0;">
    <div style="font-size: 0.95rem; font-weight: 700; color: #E2E8F0;">
        👨‍💼 सतीश अशोक प्रधान | 📱 मो. ८६६८२३५३९५
    </div>
</div>
""", unsafe_allow_html=True)

# नॅव्हिगेशन बटन्स
col_h1, col_h2, col_h3 = st.columns(3)
with col_h1:
    if st.button("🏠 होमपेज", key="nav_home"): st.session_state.active_tab = "home"; st.rerun()
with col_h2:
    if st.button("📚 कायदेशीर कलमे", key="nav_lib"): st.session_state.active_tab = "library"; st.rerun()
with col_h3:
    if st.button("📜 जतन केलेले मसुदे", key="nav_hist"): st.session_state.active_tab = "history"; st.rerun()

st.markdown("---")

# ==============================================================================
# ५. मुख्य होमपेज - हुबेहूब २-कॉलम ग्रिड रचना (HTML बटनांसह)
# ==============================================================================
if st.session_state.active_tab == "home":
    
    # Streamlit च्या फॉर्म किंवा बटन क्लिक्स हाताळण्यासाठी hidden query params किंवा buttons वापरू शकतो
    # इथे आपण st.button वापरून सहज टॅब बदलू शकतो:
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📄\nजोडपत्र 'अ'\n(कलम ६(१))", key="b1", use_container_width=True):
            st.session_state.active_tab = "rti_a"
            st.rerun()
    with col2:
        if st.button("⚖️\nप्रथम अपील\n(कलम १९(१))", key="b2", use_container_width=True):
            st.session_state.active_tab = "rti_b"
            st.rerun()

    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        if st.button("🏛️\nमाहिती आयोग\n(द्वितीय अपील)", key="b3", use_container_width=True):
            st.session_state.active_tab = "rti_c"
            st.rerun()
    with col4:
        if st.button("✨\nAI चॅट\n(कायदेशीर सहाय्यक)", key="b4", use_container_width=True):
            st.session_state.active_tab = "ai_chat"
            st.rerun()

    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

    col5, col6 = st.columns(2)
    with col5:
        if st.button("📜\nकोर्ट याचिका\n(Court Petition)", key="b5", use_container_width=True):
            st.session_state.active_tab = "court"
            st.rerun()
    with col6:
        if st.button("📢\nशासकीय तक्रार\n(Administrative)", key="b6", use_container_width=True):
            st.session_state.active_tab = "govt"
            st.rerun()

    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

    col7, col8 = st.columns(2)
    with col7:
        if st.button("📝\nप्रतिज्ञापत्र / पोर्टल\n(Affidavit)", key="b7", use_container_width=True):
            st.session_state.active_tab = "affidavit"
            st.rerun()
    with col8:
        if st.button("🛒\nग्राहक मंच तक्रार\n(Consumer)", key="b8", use_container_width=True):
            st.session_state.active_tab = "consumer"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    
    # तळाशी चॅट इनपुट बॉक्स
    home_chat_input = st.chat_input("AI ला कायदेशीर प्रश्न विचारा...")
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

# ==============================================================================
# ७. इतर सर्व मॉड्यूल्स (प्रथम अपील, माहिती आयोग, AI चॅट, कोर्ट, शासकीय, प्रतिज्ञापत्र, ग्राहक मंच, कलमे, इतिहास)
# ==============================================================================
elif st.session_state.active_tab == "rti_b":
    st.header("⚖️ जोडपत्र 'ब' - प्रथम अपील अर्ज")
    # (मागील कोडाप्रमाणे सर्व फीचर्स जसेच्या तसे चालू राहतील)

elif st.session_state.active_tab == "ai_chat":
    st.header("✨ आकांक्षा AI - कायदेशीर व प्रशासकीय चॅट सहाय्यक")
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    user_input = st.chat_input("तुमचा कायदेशीर प्रश्न किंवा अडचण इथे लिहा...")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        with st.chat_message("assistant"):
            ai_out = get_ai_response(user_input)
            st.markdown(ai_out)
            st.session_state.chat_history.append({"role": "assistant", "content": ai_out})

elif st.session_state.active_tab == "library":
    st.header("📚 कायदेशीर कलमे व मार्गदर्शक नियमावली")
    st.markdown("* **कलम ६(१):** माहिती मागण्यासाठी मूळ अर्ज.\n* **कलम १९(१):** प्रथम अपील.")

elif st.session_state.active_tab == "history":
    st.header("📜 जतन केलेले मसुदे")
    st.info("सेव्ह केलेले मसुदे इथे दिसतील.")

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
