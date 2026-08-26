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
# १. पेज कॉन्फिगरेशन आणि कस्टम CSS (Branding, Dark Theme & Dynamic CSS)
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

    /* स्क्रीनशॉट प्रमाणे ग्रिड बटनांचे डिझाईन आणि कलर्स */
    .stButton > button {
        width: 100% !important;
        height: 90px !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        border-radius: 16px !important;
        border: none !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
        transition: transform 0.2s ease;
    }

    .stButton > button:hover {
        transform: scale(0.98);
    }

    /* स्क्रीनशॉट प्रमाणे वरचा मुख्य बॅनर (Gradient Border Box) */
    .custom-banner {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        border: 2px solid transparent;
        border-image: linear-gradient(90deg, #FACC15, #38BDF8, #EC4899) 1;
        padding: 18px;
        text-align: center;
        border-radius: 18px;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.2);
        margin-bottom: 20px;
    }

    /* Custom Form Containers */
    .form-container {
        background-color: #1E293B;
        padding: 25px;
        border-radius: 16px;
        border: 1px solid #334155;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
        margin-top: 15px;
    }

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
# २. सेशन्स आणि स्टेट मॅनेजमेंट (State Initialization)
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
# ३. हेल्पर फंक्शन्स (AI Integration & Document Generators)
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
            
    return "माफ करा, सर्व AI मॉडेल्स सध्या व्यस्त आहेत. कृपया थोड्या वेळाने प्रयत्न करा."

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
    
    story = []
    story.append(Paragraph("<b>आकांक्षा AI कायदेशीर मसुदा</b>", styles['Heading1']))
    story.append(Spacer(1, 12))
    
    for paragraph in text.split('\n\n'):
        clean_p = paragraph.replace('\n', '<br/>')
        story.append(Paragraph(clean_p, style))
        story.append(Spacer(1, 8))
        
    doc.build(story)
    bio.seek(0)
    return bio

def get_share_links(text):
    encoded_text = urllib.parse.quote(text[:1000] + "...\n\n(पूर्ण मसुदा आकांक्षा AI द्वारे तयार केला आहे.)")
    whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_text}"
    mailto_url = f"mailto:?subject=कायदेशीर मसुदा - आकांक्षा AI&body={encoded_text}"
    return whatsapp_url, mailto_url

# ==============================================================================
# ४. ब्रँडिंग व स्क्रीनशॉट प्रमाणे हुबेहूब बॅनर हेडर
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

# Top Action Navigation Bar
col_home, col_lib, col_hist = st.columns(3)
with col_home:
    if st.button("🏠 होमपेज", key="nav_home"):
        st.session_state.active_tab = "home"
        st.rerun()
with col_lib:
    if st.button("📚 कायदेशीर कलमे", key="nav_lib"):
        st.session_state.active_tab = "library"
        st.rerun()
with col_hist:
    if st.button("📜 जतन केलेले मसुदे", key="nav_hist"):
        st.session_state.active_tab = "history"
        st.rerun()

st.markdown("---")

# ==============================================================================
# ५. मुख्य होमपेज - स्क्रीनशॉट प्रमाणे २-कॉलम ग्रिड रचना व खाली चॅट बॉक्स
# ==============================================================================
if st.session_state.active_tab == "home":
    
    # 1 ली जोडी: जोडपत्र 'अ' आणि प्रथम अपील
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📄\nजोडपत्र 'अ'\n(RTI कलम ६(१))", key="btn_rti_a"):
            st.session_state.active_tab = "rti_a"
            st.rerun()
    with col2:
        if st.button("⚖️\nप्रथम अपील\n(कलम १९(१))", key="btn_rti_b"):
            st.session_state.active_tab = "rti_b"
            st.rerun()

    st.markdown("<div style='margin-top: 12px;'></div>", unsafe_allow_html=True)

    # 2 री जोडी: माहिती आयोग आणि AI चॅट
    col3, col4 = st.columns(2)
    with col3:
        if st.button("🏛️\nमाहिती आयोग\n(द्वितीय अपील १९(३))", key="btn_rti_c"):
            st.session_state.active_tab = "rti_c"
            st.rerun()
    with col4:
        if st.button("✨\nAI चॅट\n(कायदेशीर सहाय्यक)", key="btn_ai_chat"):
            st.session_state.active_tab = "ai_chat"
            st.rerun()

    st.markdown("<div style='margin-top: 12px;'></div>", unsafe_allow_html=True)

    # 3 री जोडी: कोर्ट याचिका आणि शासकीय तक्रार
    col5, col6 = st.columns(2)
    with col5:
        if st.button("📜\nकोर्ट याचिका\n(Court Petition)", key="btn_court"):
            st.session_state.active_tab = "court"
            st.rerun()
    with col6:
        if st.button("📢\nशासकीय तक्रार\n(Administrative App)", key="btn_govt"):
            st.session_state.active_tab = "govt"
            st.rerun()

    st.markdown("<div style='margin-top: 12px;'></div>", unsafe_allow_html=True)

    # 4 थी जोडी: प्रतिज्ञापत्र / पोर्टल सहाय्य आणि ग्राहक मंच
    col7, col8 = st.columns(2)
    with col7:
        if st.button("📝\nप्रतिज्ञापत्र / पोर्टल\n(Affidavit Draft)", key="btn_affidavit"):
            st.session_state.active_tab = "affidavit"
            st.rerun()
    with col8:
        if st.button("🛒\nग्राहक मंच तक्रार\n(Consumer Forum)", key="btn_consumer"):
            st.session_state.active_tab = "consumer"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # स्क्रीनशॉट प्रमाणे अगदी खाली चॅट इनपुट बॉक्स
    home_chat_input = st.chat_input("AI ला कायदेशीर प्रश्न विचारा...")
    if home_chat_input:
        st.session_state.active_tab = "ai_chat"
        st.session_state.chat_history.append({"role": "user", "content": home_chat_input})
        st.rerun()

# ==============================================================================
# ६. विभाग १: जोडपत्र 'अ' (माहिती अधिकार मूळ अर्ज - कलम ६(१))
# ==============================================================================
elif st.session_state.active_tab == "rti_a":
    st.header("📄 जोडपत्र 'अ' - माहिती अधिकार अर्ज (कलम ६(१))")
    
    with st.form("form_rti_a"):
        col1, col2 = st.columns(2)
        with col1:
            applicant_name = st.text_input("अर्जदाराचे पूर्ण नाव:", value="सतीश अशोक प्रधान")
            applicant_address = st.text_area("पूर्ण पत्ता व मोबाईल:", value="छत्रपती संभाजीनगर, मो. ८६६८२३५३९५")
            pio_office = st.text_input("जन माहिती अधिकारी / कार्यालयाचे नाव:", value="जन माहिती अधिकारी, जिल्हाधिकारी कार्यालय, छत्रपती संभाजीनगर")
        with col2:
            subject = st.text_input("माहितीचा विषय:", value="प्रशासकीय कामाचा निधी व खर्च तपशील")
            time_period = st.text_input("माहितीचा कालावधी:", value="०१ जानेवारी २०२५ ते ३१ डिसेंबर २०२५")
            delivery_mode = st.radio("माहिती मिळण्याचा मार्ग:", ["व्यक्तिशः (Self)", "टपालाद्वारे (Speed Post)", "जी-मेल (Gmail/Email)"])
            
            email_id = ""
            if delivery_mode == "जी-मेल (Gmail/Email)":
                email_id = st.text_input("ई-मेल आयडी नोंदवा:", value="ashapradhan981@gmail.com")

        bpl_status = st.checkbox("अर्जदार दारिद्र्यरेषेखालील (BPL) आहे का?", value=False)
        details = st.text_area("हव्या असलेल्या माहितीचे मुद्देवार वर्णन:", value="१. उपरोक्त कालावधीत मंजूर झालेल्या सर्व निधीची सत्यप्रत.\n२. संबंधित कामांची निविदा प्रक्रिया आणि वर्क ऑर्डरच्या प्रती.")

        submit_a = st.form_submit_button("🚀 जोडपत्र 'अ' मसुदा तयार करा")

    if submit_a:
        mode_str = delivery_mode
        if delivery_mode == "जी-मेल (Gmail/Email)":
            mode_str = f"ई-मेल द्वारे ({email_id})"

        fee_str = "माहिती अधिकार कायद्यानुसार १०/- रुपयाचा कोर्ट फी स्टॅम्प जोडला आहे."
        if bpl_status:
            fee_str = "अर्जदार दारिद्र्यरेषेखालील (BPL) असल्याने शुल्क माफ आहे. (BPL कार्ड प्रत जोडली आहे)."

        draft = f"""
परिशिष्ट / जोडपत्र 'अ'
(माहितीचा अधिकार अधिनियम, २००५ च्या कलम ६(१) अन्वये अर्ज)

प्रति,
{pio_office}

१. अर्जदाराचे नाव : {applicant_name}
२. पूर्ण पत्ता व संपर्क : {applicant_address}
३. माहितीचा विषय : {subject}
४. आवश्यक असलेल्या माहितीचा कालावधी : {time_period}
५. हव्या असलेल्या माहितीचे वर्णन :
{details}

६. माहिती पुरवण्याचा मार्ग : {mode_str}
७. अर्जाचे शुल्क : {fee_str}

स्थान: छत्रपती संभाजीनगर
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}

अर्जदाराची स्वाक्षरी: ___________________
({applicant_name})
"""
        st.session_state.generated_draft = draft
        st.session_state.draft_history.append({"title": f"RTI-A: {subject}", "date": str(datetime.date.today()), "content": draft})

# ==============================================================================
# ७. विभाग २: जोडपत्र 'ब' (प्रथम अपील - कलम १९(१))
# ==============================================================================
elif st.session_state.active_tab == "rti_b":
    st.header("⚖️ जोडपत्र 'ब' - प्रथम अपील अर्ज (कलम १९(१))")
    
    with st.form("form_rti_b"):
        col1, col2 = st.columns(2)
        with col1:
            app_name = st.text_input("अपीलकर्त्याचे नाव:", value="सतीश अशोक प्रधान")
            app_address = st.text_area("पत्ता व संपर्क:", value="छत्रपती संभाजीनगर, मो. ८६६८२३५३९५")
            first_authority = st.text_input("प्रथम अपीलीय अधिकारी पदनाम व कार्यालय:", value="प्रथम अपीलीय अधिकारी तथा उपजिल्हाधिकारी, छत्रपती संभाजीनगर")
        with col2:
            pio_details = st.text_input("जन माहिती अधिकारी तपशील:", value="जन माहिती अधिकारी, तहसील कार्यालय")
            original_app_date = st.date_input("मूळ अर्जाची (६(१)) तारीख:")
            reason = st.selectbox("अपीलाचे मुख्य कारण:", [
                "मुदतीत माहिती न मिळणे (कलम ७(१) चे उल्लंघन)",
                "अपूर्ण व दिशाभूल करणारी माहिती मिळणे",
                "बेकायदेशीरपणे माहिती देण्यास नकार देणे",
                "अवाजवी शुल्काची मागणी करणे"
            ])

        appeal_grounds = st.text_area("अपीलाचे सविस्तर आधार / युक्तीवाद:", value="जन माहिती अधिकाऱ्यांनी विहित मुदतीत माहिती पुरवली नाही. त्यामुळे कलम ७(६) नुसार आता संपूर्ण माहिती विनामूल्य मिळण्यास मी पात्र आहे.")
        
        submit_b = st.form_submit_button("🚀 प्रथम अपील मसुदा तयार करा")

    if submit_b:
        draft = f"""
जोडपत्र 'ब'
(माहितीचा अधिकार अधिनियम, २००५ च्या कलम १९(१) अन्वये प्रथम अपील)

प्रति,
{first_authority}

१. अपीलकर्त्याचे नाव व पत्ता : {app_name}, {app_address}
२. जन माहिती अधिकाऱ्याचा तपशील : {pio_details}
३. मूळ अर्ज ६(१) सादर केल्याचा दिनांक : {original_app_date.strftime('%d/%m/%Y')}
४. अपीलाचे कारण : {reason}

५. अपीलाचे आधार व वस्तुस्थिती :
{appeal_grounds}

६. मागितलेली दाद / प्रार्थना :
अ) जन माहिती अधिकाऱ्यांना तात्काळ व विनामूल्य संपूर्ण अचूक माहिती पुरवण्याचे निर्देश द्यावेत.
ब) विहित मुदतीचे उल्लंघन केल्याप्रकरणी जन माहिती अधिकाऱ्यावर प्रशासकीय नियमांनुसार कारवाईची शिफारस करावी.

स्थान: छत्रपती संभाजीनगर
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}

अपीलकर्त्याची स्वाक्षरी: ___________________
({app_name})
"""
        st.session_state.generated_draft = draft
        st.session_state.draft_history.append({"title": f"RTI-First Appeal", "date": str(datetime.date.today()), "content": draft})

# ==============================================================================
# ८. विभाग ३: जोडपत्र 'क' (द्वितीय अपील - कलम १९(३))
# ==============================================================================
elif st.session_state.active_tab == "rti_c":
    st.header("🏛️ जोडपत्र 'क' - द्वितीय अपील (माहिती आयोग कलम १९(३))")
    
    with st.form("form_rti_c"):
        col1, col2 = st.columns(2)
        with col1:
            bench = st.selectbox("राज्य माहिती आयोग खंडपीठ:", ["राज्य माहिती आयोग, खंडपीठ छत्रपती संभाजीनगर", "राज्य माहिती आयोग, मुंबई", "राज्य माहिती आयोग, पुणे Bench"])
            app_name = st.text_input("अपीलकर्त्याचे नाव:", value="सतीश अशोक प्रधान")
            app_contact = st.text_area("पत्ता व फोन:", value="छत्रपती संभाजीनगर, मो. ८६६८२३५३९५")
        with col2:
            pio_name = st.text_input("जन माहिती अधिकारी कार्यालय:", value="जन माहिती अधिकारी, भूमी अभिलेख विभाग")
            faa_name = st.text_input("प्रथम अपीलीय अधिकारी कार्यालय:", value="प्रथम अपीलीय अधिकारी, उपसंचालक भूमी अभिलेख")
            faa_order_date = st.text_input("प्रथम अपीलाच्या निर्णयाची तारीख/अंशतः उत्तर:", value="निर्णय दिलेला नाही / अपीलाची सुनावणी घेतली नाही")

        penalty_demand = st.checkbox("कलम २० अन्वये दोषी अधिकाऱ्यावर २५,००० रु. दंडात्मक कारवाईची मागणी करावी का?", value=True)
        facts = st.text_area("द्वितीय अपीलाची सविस्तर वस्तुस्थिती:", value="प्रथम अपीलीय अधिकाऱ्यांनी आदेश देऊनही जन माहिती अधिकाऱ्यांनी माहिती पुरवली नाही. माहिती अधिकाराच्या मूळ उद्देषाला हरताळ फासला जात आहे.")

        submit_c = st.form_submit_button("🚀 द्वितीय अपील मसुदा तयार करा")

    if submit_c:
        penalty_clause = ""
        if penalty_demand:
            penalty_clause = "माहिती कायदा कलम २०(१) अन्वये संबंधित दोषी अधिकाऱ्यावर दरदिवशी २५० रु. प्रमाणे कमाल २५,०००/- रु. दंडात्मक कारवाई करण्यात यावी व कलम २०(२) नुसार विभागीय चौकशीचे आदेश द्यावेत."

        draft = f"""
माहितीचा अधिकार अधिनियम, २००५ च्या कलम १९(३) अन्वये द्वितीय अपील अर्ज

समक्ष:
माननीय राज्य माहिती आयुक्त,
{bench}

अपीलकर्ता : {app_name}, {app_contact}
विरुद्ध
प्रतिवादी क्र. १ : जन माहिती अधिकारी, {pio_name}
प्रतिवादी क्र. २ : प्रथम अपीलीय अधिकारी, {faa_name}

विषय: द्वितीय अपील अर्ज स्वीकारून माहिती मिळणे व दोषी अधिकाऱ्यांवर दंडात्मक कारवाई होणेबाबत.

प्रथम अपील आदेश दिनांक : {faa_order_date}

अपिलाची सविस्तर वस्तुस्थिती:
{facts}

प्रार्थना / मागण्या:
१. प्रतिवादींना तत्काळ सत्यप्रत माहिती पुरवण्याचे आदेश व्हावेत.
२. {penalty_clause}

स्थान: छत्रपती संभाजीनगर
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}

अपीलकर्त्याची स्वाक्षरी: ___________________
({app_name})
"""
        st.session_state.generated_draft = draft
        st.session_state.draft_history.append({"title": "RTI-Second Appeal", "date": str(datetime.date.today()), "content": draft})

# ==============================================================================
# ९. विभाग ४: AI चॅट (आकांक्षा AI कायदेशीर सहाय्यक)
# ==============================================================================
elif st.session_state.active_tab == "ai_chat":
    st.header("✨ आकांक्षा AI - कायदेशीर व प्रशासकीय चॅट सहाय्यक")
    st.info("💡 टीप: कोणत्याही कायदेशीर, न्यायालयीन किंवा माहिती अधिकार कायद्याबद्दल प्रश्न विचारा. किंवा कागदपत्रांचा संदर्भ द्या.")

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("तुमचा कायदेशीर प्रश्न किंवा अडचण इथे लिहा...")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("आकांक्षा AI विचार करत आहे व कायदेशीर मसुदा शोधत आहे..."):
                system_context = f"तुम्ही 'आकांक्षा AI' कायदेशीर महा-सहाय्यक आहात. युझरचे नाव सतीश अशोक प्रधान आहे. भारतीय कायदे, RTI, BNS, IPC, आणि प्रशासकीय नियमांनुसार मराठीत अचूक मार्गदर्शन व मसुदा तयार करा. प्रश्न: {user_input}"
                ai_out = get_ai_response(system_context)
                st.markdown(ai_out)
                st.session_state.chat_history.append({"role": "assistant", "content": ai_out})

# ==============================================================================
# १०. विभाग ५: न्यायालयीन मसुदा (Court Petition / Legal Notice)
# ==============================================================================
elif st.session_state.active_tab == "court":
    st.header("📜 न्यायालयीन मसुदा (दिवाणी/फौजदारी/रिट याचिका)")
    
    with st.form("form_court"):
        court_name = st.text_input("न्यायालयाचे नाव:", value="मे. दिवाणी न्यायालय वरिष्ठ स्तर, छत्रपती संभाजीनगर")
        col1, col2 = st.columns(2)
        with col1:
            petitioner = st.text_input("याचिकाकर्ता/वादी:", value="सतीश अशोक प्रधान")
        with col2:
            respondent = st.text_input("प्रतिवादी/सामनेवाला:", value="संबंधित विभाग / खाजगी संस्था")
            
        case_type = st.selectbox("दाव्याचा / याचिकेचा प्रकार:", ["दिवाणी दावा (Civil Suit)", "फौजदारी तक्रार (Criminal Complaint)", "रिट याचिका (Writ Petition - High Court)", "कायदेशीर नोटीस (Legal Notice)"])
        facts = st.text_area("दाव्यातील प्रमुख घटना व वस्तुस्थिती:", value="प्रतिवादीने कराराचे उल्लंघन केले असून बेकायदेशीर कृत्य केले आहे.")
        prayers = st.text_area("न्यायालयाकडे मागितलेली दाद (Prayer):", value="प्रतिवादीस कायदेशीर प्रतिबंध करण्यात यावा व झालेल्या नुकसानीची भरपाई देण्यात यावी.")
        
        submit_court = st.form_submit_button("🚀 कोर्ट मसुदा तयार करा")

    if submit_court:
        draft = f"""
समक्ष : माननीय {court_name}

याचिका क्रमांक : _______ / २०२६

{petitioner}  ... वादी / याचिकाकर्ता
विरुद्ध
{respondent} ... प्रतिवादी / सामनेवाला

प्रकार: {case_type}

विषय: {case_type} अन्वये विनंती अर्ज.

वादीचा सविस्तर युक्तीवाद व वस्तुस्थिती:
{facts}

कायदेशीर मुद्दे व कलमे:
उपरोक्त कृत्य हे भारतीय कायद्यातील तरतुदींचे उल्लंघन करणारे असून वादीच्या मूलभूत हक्कांवर गदा आणणारे आहे.

प्रार्थना (Prayer):
अ) {prayers}
ब) या दाव्याचा संपूर्ण खर्च प्रतिवादीकडून वादीला देववण्यात यावा.
क) न्यायालय योग्य समजेल असा इतर दिलासा देण्यात यावा.

सत्यप्रतिज्ञा (Verification):
मी, {petitioner}, प्रतिज्ञापूर्वक लिहितो की, वरील मजकूर माझ्या माहिती व विश्वासाप्रमाणे सत्य व बरोबर आहे.

स्थान: छत्रपती संभाजीनगर
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}

वादीची स्वाक्षरी: ___________________
"""
        st.session_state.generated_draft = draft
        st.session_state.draft_history.append({"title": f"Court: {case_type}", "date": str(datetime.date.today()), "content": draft})

# ==============================================================================
# ११. विभाग ६: शासकीय तक्रार अर्ज (Administrative Complaint)
# ==============================================================================
elif st.session_state.active_tab == "govt":
    st.header("📢 शासकीय तक्रार अर्ज (प्रशासकीय गैरकारभाराविरुद्ध)")
    
    with st.form("form_govt"):
        officer = st.text_input("तक्रार स्वीकारणारे वरिष्ठ अधिकारी:", value="मा. जिल्हाधिकारी साहेब, छत्रपती संभाजीनगर")
        applicant = st.text_input("तक्रारदाराचे नाव व संपर्क:", value="सतीश अशोक प्रधान, मो. ८६६८२३५३९५")
        dept = st.text_input("संबंधित शासकीय विभाग:", value="सार्वजनिक बांधकाम विभाग / महानगरपालिका")
        subject = st.text_input("तक्रारीचा मुख्य विषय:", value="शासकीय कामातील गैरव्यवहार आणि भ्रष्टाचार चौकशीबाबत")
        details = st.text_area("गैरकारभाराचा/प्रकरणाचा सविस्तर तपशील:", value="संबंधित अधिकाऱ्यांनी पदाचा गैरवापर करून नियमांचे उल्लंघन केले आहे व निकृष्ट दर्जाचे काम केले आहे.")
        demand = st.text_area("मागणी / प्रशासकीय कारवाईची विनंती:", value="दोषी अधिकाऱ्यांवर तात्काळ निलंबनाची कारवाई करून सखोल चौकशी समिती नेमण्यात यावी.")

        submit_govt = st.form_submit_button("🚀 शासकीय तक्रार अर्ज तयार करा")

    if submit_govt:
        draft = f"""
प्रशासकीय तक्रार अर्ज

प्रति,
{officer}

तक्रारदार : {applicant}
विभागाचे नाव : {dept}

विषय : {subject}

महेश्‍वर,

मी खालीलप्रमाणे तक्रार नोंदवत आहे:
१. {details}

२. वरील प्रकारामुळे सर्वसामान्य नागरिकांचे अतोनात नुकसान होत असून प्रशासकीय शिस्तीचा भंग होत आहे.

माझी मागणी:
{demand}

जर दिलेल्या मुदतीत योग्य कारवाई झाली नाही, तर तीव्र लोकशाही मार्गाने आंदोलन करण्यात येईल.

स्थान: छत्रपती संभाजीनगर
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}

आपला नम्र,

___________________
({applicant})
"""
        st.session_state.generated_draft = draft
        st.session_state.draft_history.append({"title": f"Govt Complaint: {subject}", "date": str(datetime.date.today()), "content": draft})

# ==============================================================================
# १२. विभाग ७: प्रतिज्ञापत्र (Affidavit Draft)
# ==============================================================================
elif st.session_state.active_tab == "affidavit":
    st.header("📝 प्रतिज्ञापत्र (Affidavit Draft)")
    
    with st.form("form_affidavit"):
        name = st.text_input("प्रतिज्ञापत्र करणाऱ्याचे पूर्ण नाव:", value="सतीश अशोक प्रधान")
        age = st.text_input("वय:", value="४०")
        address = st.text_area("पूर्ण पत्ता:", value="छत्रपती संभाजीनगर")
        purpose = st.text_input("प्रतिज्ञापत्राचे कारण / कशासाठी हवे आहे:", value="शासकीय योजनेच्या लाभासाठी व सत्यता पडताळणीसाठी")
        statements = st.text_area("सत्य विधाने (मुद्देवार):", value="१. मी असे प्रतिज्ञापूर्वक सांगतो की, वरील पत्त्यावर मी कायमस्वरूपी राहणारा आहे.\n२. माझ्याद्वारे दिलेली सर्व माहिती पूर्णपणे खरी व अचूक आहे.")

        submit_aff = st.form_submit_button("🚀 प्रतिज्ञापत्र मसुदा तयार करा")

    if submit_aff:
        draft = f"""
प्रतिज्ञापत्र (AFFIDAVIT)

मी, {name}, वय: {age} वर्षे, राहणार: {address}, प्रतिज्ञापत्राद्वारे खालीलप्रमाणे लिहून देतो की:

१. मी वरील नमूद पत्त्याचा कायमचा रहिवासी असून या प्रतिज्ञापत्रातील सर्व बाबींशी भलीभांती परिचित आहे.
२. हे प्रतिज्ञापत्र मी {purpose} या कारणासाठी सादर करत आहे.
३. माझे सत्य कथन खालीलप्रमाणे आहे:
{statements}

४. वरील सर्व माहिती माझ्या वैयक्तिक ज्ञानानुसार सत्य व बरोबर आहे. त्यात मी कोणतीही बाब लपवून ठेवलेली नाही.

सत्यता पडताळणी (Verification):
आज दिनांक {datetime.date.today().strftime('%d/%m/%Y')} रोजी छत्रपती संभाजीनगर येथे समक्ष उपस्थित राहून वरील मजकूर खरा असल्याबाबत प्रतिज्ञापूर्वक स्वाक्षरी केली.

प्रतिज्ञापत्र करणारा: ___________________
({name})
"""
        st.session_state.generated_draft = draft
        st.session_state.draft_history.append({"title": f"Affidavit: {purpose}", "date": str(datetime.date.today()), "content": draft})

# ==============================================================================
# १३. विभाग ८: ग्राहक मंच तक्रार (Consumer Forum)
# ==============================================================================
elif st.session_state.active_tab == "consumer":
    st.header("🛒 ग्राहक मंच तक्रार (Consumer Protection Act 2019)")
    
    with st.form("form_consumer"):
        complainant = st.text_input("तक्रारदाराचे नाव व पत्ता:", value="सतीश अशोक प्रधान, छत्रपती संभाजीनगर, मो. ८६६८२३५३९५")
        opposite_party = st.text_input("विरोधी कंपनी / विक्रेत्याचे नाव व पत्ता:", value="मे. फायनान्स कंपनी / मोबाईल शोरूम")
        product_service = st.text_input("खरेदी केलेली वस्तू / घेतलेली सेवा:", value="वाहन कर्ज सेवा / इलेक्ट्रॉनिक वस्तू")
        claim_amount = st.text_input("मागितलेली भरपाई रक्कम (रु.):", value="५०,०००/-")
        complaint_facts = st.text_area("सेवेतील त्रुटी व फसवणुकीचा सविस्तर तपशील:", value="विरोधी पक्षाने जाहिरातीत दिलेल्या आश्वासनानुसार सेवा दिली नाही व अनुचित व्यापार पद्धतीचा (Unfair Trade Practice) वापर केला.")

        submit_consumer = st.form_submit_button("🚀 ग्राहक मंच तक्रार तयार करा")

    if submit_consumer:
        draft = f"""
समक्ष : माननीय जिल्हा ग्राहक तक्रार निवारण आयोग, छत्रपती संभाजीनगर

तक्रार अर्ज क्र. ______ / २०२६
(ग्राहक संरक्षण कायदा, २०१९ अन्वये तक्रार)

{complainant} ... तक्रारदार
विरुद्ध
{opposite_party} ... विरोधी पक्ष

विषय: सेवेतील त्रुटी (Deficiency in Service) व अनुचित व्यापार पद्धतीविरुद्ध तक्रार.

तक्रारीची वस्तुस्थिती:
१. तक्रारदाराने विरोधी पक्षाकडून {product_service} सेवा/वस्तू घेतली होती.
२. {complaint_facts}

मागितलेली दाद व भरपाई:
अ) विरोधी पक्षाने सेवेतील त्रुटी दूर करून दिलेली सदोष सेवा सुधारावी.
ब) तक्रारदारास झालेल्या मानसिक व शारीरिक त्रासाबद्दल रु. {claim_amount} भरपाई म्हणून देववावेत.
क) तक्रार अर्जाचा खर्च रु. ५,०००/- विरोधी पक्षाकडून देववावा.

स्थान: छत्रपती संभाजीनगर
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}

तक्रारदाराची स्वाक्षरी: ___________________
({complainant.split(',')[0]})
"""
        st.session_state.generated_draft = draft
        st.session_state.draft_history.append({"title": "Consumer Complaint", "date": str(datetime.date.today()), "content": draft})

# ==============================================================================
# १४. अतिरिक्त विभाग: कायदेशीर कलमे (Legal Reference Library)
# ==============================================================================
elif st.session_state.active_tab == "library":
    st.header("📚 कायदेशीर कलमे व मार्गदर्शक नियमावली (Legal Library)")
    
    tab_rti, tab_cp, tab_bns = st.tabs(["माहिती अधिकार (RTI)", "ग्राहक संरक्षण", "BNS / IPC नियम"])
    
    with tab_rti:
        st.markdown("""
        * **कलम ६(१):** माहिती मागण्यासाठी मूळ अर्ज दाखल करणे.
        * **कलम ७(१):** ३० दिवसांच्या आत माहिती देणे बंधनकारक. (जीविताशी संबंधित असल्यास ४८ तास).
        * **कलम ७(६):** ३० दिवसांत माहिती न दिल्यास ती **विनामूल्य** देणे बंधनकारक.
        * **कलम १९(१):** प्रथम अपील (३० दिवसांच्या आत वरिष्ठांकडे).
        * **कलम १९(३):** द्वितीय अपील (राज्य माहिती आयोगाकडे ९० दिवसांत).
        * **कलम २०(१):** दोषी जन माहिती अधिकाऱ्यावर दरदिवशी २५० रु. (कमाल २५,००० रु.) दंड.
        """)
        
    with tab_cp:
        st.markdown("""
        * **ग्राहक संरक्षण कायदा २०१९:**
        * **जिल्हा आयोग:** ५० लाख रुपयांपर्यंतच्या दाव्यांसाठी.
        * **राज्य आयोग:** ५० लाख ते २ कोटी रुपयांपर्यंत.
        * **राष्ट्रीय आयोग:** २ कोटींपेक्षा जास्त दाव्यांसाठी.
        """)
        
    with tab_bns:
        st.markdown("""
        * **भारतीय न्याय संहिता (BNS):**
        * **बनावट दस्तऐवज (Forgery):** BNS कलम ३३६ / ३३८.
        * **फसवणूक (Cheating):** BNS कलम ३१८.
        * **प्रशासकीय गैरकारभार तक्रार:** CrPC १५६(३) / BNSS सुधारित नियम.
        """)

# ==============================================================================
# १५. अतिरिक्त विभाग: मसुदा इतिहास (Draft History)
# ==============================================================================
elif st.session_state.active_tab == "history":
    st.header("📜 सेव्ह केलेले मसुदे (Draft History)")
    if not st.session_state.draft_history:
        st.info("अद्याप कोणताही मसुदा सेव्ह केलेला नाही.")
    else:
        for idx, item in enumerate(st.session_state.draft_history):
            with st.expander(f"{idx+1}. {item['title']} - ({item['date']})"):
                st.code(item['content'], language='text')

# ==============================================================================
# १६. मसुदा डिस्प्ले आणि डाऊनलोड / शेअर ऑप्शन्स (Export Section)
# ==============================================================================
if st.session_state.generated_draft and st.session_state.active_tab not in ["home", "library", "history", "ai_chat"]:
    st.markdown("---")
    st.subheader("📋 तयार झालेला कायदेशीर मसुदा (Preview):")
    st.markdown(f'<div class="draft-preview">{st.session_state.generated_draft}</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📥 मसुदा डाऊनलोड व शेअर करा:")
    
    col_txt, col_docx, col_pdf, col_wa, col_mail = st.columns(5)
    
    with col_txt:
        st.download_button(
            label="📄 TXT डाऊनलोड",
            data=st.session_state.generated_draft,
            file_name="legal_draft.txt",
            mime="text/plain"
        )
        
    with col_docx:
        docx_file = generate_docx(st.session_state.generated_draft)
        st.download_button(
            label="📝 Word (DOCX)",
            data=docx_file,
            file_name="legal_draft.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
        
    with col_pdf:
        pdf_file = generate_pdf(st.session_state.generated_draft)
        st.download_button(
            label="🔴 PDF डाऊनलोड",
            data=pdf_file,
            file_name="legal_draft.pdf",
            mime="application/pdf"
        )
        
    wa_link, mail_link = get_share_links(st.session_state.generated_draft)
    with col_wa:
        st.markdown(f'<a href="{wa_link}" target="_blank"><button style="width:100%; background-color:#22C55E; color:white; border:none; padding:8px; border-radius:8px; font-weight:bold;">📲 WhatsApp शेअर</button></a>', unsafe_allow_html=True)
    with col_mail:
        st.markdown(f'<a href="{mail_link}" target="_blank"><button style="width:100%; background-color:#3B82F6; color:white; border:none; padding:8px; border-radius:8px; font-weight:bold;">✉️ Email पाठवा</button></a>', unsafe_allow_html=True)
