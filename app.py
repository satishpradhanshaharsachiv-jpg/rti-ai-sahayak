import streamlit as st
import google.generativeai as genai
import datetime
import io
import urllib.parse
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# ==========================================
# १. पेज सेटअप व ३D/ॲनिमेटेड CSS
# ==========================================
st.set_page_config(page_title="आकांक्षा AI कायदेशीर महा-सहाय्यक", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Mukta:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Mukta', sans-serif !important;
        background-color: #0F172A !important;
        color: #F8FAFC !important;
    }

    @keyframes bannerGlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes btnGlow1 { 
        0% { background-position: 0% 50%; } 
        50% { background-position: 100% 50%; } 
        100% { background-position: 0% 50%; } 
    }
    
    .custom-header-banner {
        background: linear-gradient(-45deg, #1e3c72, #2a5298, #0f2027, #203a43, #2c5364);
        background-size: 400% 400%;
        animation: bannerGlow 10s ease infinite;
        border: 2px solid #ffd700;
        border-radius: 20px;
        padding: 20px 15px;
        text-align: center;
        color: white;
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.4);
        margin-bottom: 25px;
    }
    
    .banner-title { font-size: 22px; font-weight: 800; color: #ffde59; margin-bottom: 8px; }
    .banner-subtitle { font-size: 14px; color: #ff9999; font-weight: 600; margin-bottom: 12px; }
    .banner-footer { border-top: 1px dashed rgba(255,255,255,0.3); padding-top: 10px; font-size: 15px; color: #e0e0e0; font-weight: 600; }

    .grid-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; max-width: 900px; margin: 0 auto 25px auto; }
    .grid-btn-3d {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        padding: 18px 10px; border-radius: 16px; color: white !important; font-weight: 700;
        text-decoration: none !important; text-align: center; font-size: 15px; background-size: 300% 300%;
        animation: btnGlow1 6s ease infinite; box-shadow: 0px 6px 0px rgba(0,0,0,0.3), 0px 8px 15px rgba(0,0,0,0.3);
        transition: all 0.2s ease; border: 1px solid rgba(255,255,255,0.2);
    }
    .grid-btn-3d:active { transform: translateY(4px); box-shadow: 0px 2px 0px rgba(0,0,0,0.3); }

    .btn-col-1 { background-image: linear-gradient(135deg, #11998e, #38ef7d, #00b09b, #96c93d); }
    .btn-col-2 { background-image: linear-gradient(135deg, #ff416c, #ff4b2b, #ff0844, #ffb199); }
    .btn-col-3 { background-image: linear-gradient(135deg, #1f4037, #99f2c8, #005c97, #363795); }
    .btn-col-4 { background-image: linear-gradient(135deg, #00c6ff, #0072ff, #00d2ff, #3a7bd5); }
    .btn-col-5 { background-image: linear-gradient(135deg, #8e2de2, #4a00e0, #654ea3, #eaafc8); }
    .btn-col-6 { background-image: linear-gradient(135deg, #d31027, #ea384d, #e52d27, #b31217); }
    .btn-col-7 { background-image: linear-gradient(135deg, #f857a6, #ff5858, #f7b733, #fc4a1a); color: #000 !important; }
    .btn-col-8 { background-image: linear-gradient(135deg, #00b4db, #0083b0, #136a8a, #267871); }
    .btn-icon { font-size: 22px; margin-bottom: 4px; }

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

# ==========================================
# २. सेशन्स आणि स्टेट मॅनेजमेंट
# ==========================================
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'draft_history' not in st.session_state:
    st.session_state.draft_history = []
if 'generated_draft' not in st.session_state:
    st.session_state.generated_draft = ""

query_params = st.query_params
current_form = query_params.get("form", "jodpatra_a")

# ==========================================
# ३. १-पेज A4 PDF व DOCX जनरेटर
# ==========================================
def generate_colorful_a4_pdf(title_text, content_text):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    story = []
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'HeaderTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#1E3C72'),
        alignment=1,
        spaceAfter=10
    )
    
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor('#222222'),
        spaceAfter=8
    )

    header_data = [[Paragraph(f"<b>{title_text.upper()}</b>", title_style)]]
    header_table = Table(header_data, colWidths=[520])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EBF3FA')),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#1E3C72')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 10))

    paragraphs = content_text.split('\n')
    formatted_content = []
    for line in paragraphs:
        if line.strip():
            formatted_content.append([Paragraph(line.replace('\n', '<br/>'), body_style)])

    content_table = Table(formatted_content, colWidths=[520])
    content_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#2A5298')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FAFAFA')),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(content_table)

    doc.build(story)
    buffer.seek(0)
    return buffer

def generate_docx(text):
    doc = Document()
    doc.add_heading('आकांक्षा AI कायदेशीर मसुदा', level=1)
    for line in text.split('\n'):
        doc.add_paragraph(line)
    bio = io.BytesIO()
    doc.save(bio)
    bio.seek(0)
    return bio

def get_share_links(text):
    encoded_text = urllib.parse.quote(text[:1000] + "...\n\n(पूर्ण मसुदा आकांक्षा AI द्वारे तयार केला आहे.)")
    whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_text}"
    mailto_url = f"mailto:?subject=कायदेशीर मसुदा - आकांक्षा AI&body={encoded_text}"
    return whatsapp_url, mailto_url

# ==========================================
# ४. AI कॉन्फिगरेशन
# ==========================================
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", "")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

UNIVERSAL_SYSTEM_PROMPT = "तुम्ही 'आकांक्षा AI असिस्टंट' आहात - कायदेशीर व सर्वसमावेशक AI सहाय्यक."

# ==========================================
# ५. ३D बॅनर व ८ ग्रिड बटने
# ==========================================
st.markdown("""
<div class="custom-header-banner">
    <div class="banner-title">✨ आकांक्षा AI कायदेशीर व प्रशासकीय महा-सहाय्यक ✨</div>
    <div class="banner-subtitle">⚡ घरबसल्या RTI अर्ज व कायदेशीर मसुदे एका सेकंदात A4 साईज मध्ये मोफत मिळवा ⚡</div>
    <div class="banner-footer">👤 संकल्पना व निर्मिती: सतीश अशोक प्रधान | 📱 मो. ८६६८२३५३९५ | 📍 छत्रपती संभाजीनगर</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="grid-container">
    <a href="?form=jodpatra_a#form-section" target="_self" class="grid-btn-3d btn-col-1"><span class="btn-icon">📄</span> जोडपत्र 'अ' (RTI)</a>
    <a href="?form=first_appeal#form-section" target="_self" class="grid-btn-3d btn-col-2"><span class="btn-icon">⚖️</span> प्रथम अपील</a>
    <a href="?form=second_appeal#form-section" target="_self" class="grid-btn-3d btn-col-3"><span class="btn-icon">🏛️</span> माहिती आयोग</a>
    <a href="?form=court#form-section" target="_self" class="grid-btn-3d btn-col-5"><span class="btn-icon">📜</span> कोर्ट याचिका</a>
    <a href="?form=complaint#form-section" target="_self" class="grid-btn-3d btn-col-6"><span class="btn-icon">📢</span> शासकीय तक्रार</a>
    <a href="?form=affidavit#form-section" target="_self" class="grid-btn-3d btn-col-7"><span class="btn-icon">📝</span> प्रतिज्ञापत्र</a>
    <a href="?form=consumer#form-section" target="_self" class="grid-btn-3d btn-col-8"><span class="btn-icon">🛒</span> ग्राहक मंच</a>
    <a href="?form=ai_chat#form-section" target="_self" class="grid-btn-3d btn-col-4"><span class="btn-icon">✨</span> AI चॅट</a>
</div>
""", unsafe_allow_html=True)
st.markdown('<div id="form-section"></div>', unsafe_allow_html=True)

# ==========================================
# ६. ७ फॉर्म्स (Form Sections)
# ==========================================

# १. जोडपत्र 'अ'
if current_form == "jodpatra_a":
    st.info("📋 जोडपत्र 'अ' - माहितीचा अधिकार अधिनियम, २००५ अन्वये अर्ज (कलम ६(१))")
    with st.form("form_a"):
        karyalay = st.text_input("जन माहिती अधिकाऱ्याच्या कार्यालयाचे नाव व पत्ता:", value="जन माहिती अधिकारी, जिल्हाधिकारी कार्यालय, छत्रपती संभाजीनगर")
        name = st.text_input("अर्जदाराचे संपूर्ण नाव:", value="सतीश अशोक प्रधान")
        address = st.text_area("अर्जदाराचा पूर्ण पत्ता:", value="छत्रपती संभाजीनगर, मो. ८६६८२३५३९५")
        subject = st.text_input("माहितीचा विषय:", value="प्रशासकीय कामाचा निधी व खर्च तपशील")
        period = st.text_input("माहितीचा कालावधी:", value="०१ जानेवारी २०२५ ते ३१ डिसेंबर २०२५")
        desc = st.text_area("हव्या असलेल्या माहितीचे वर्णन:", value="१. वरील कालावधीतील सर्व मंजूर निधी व कामांची यादी.\n२. संबंधित कामांच्या निविदा व पेमेंट प्रती.")
        post_type = st.selectbox("माहिती कशी हवी आहे?", ["टपालाद्वारे (नोंदणीकृत / स्पीड पोस्ट)", "व्यक्तीश: (रूबरू)", "जी-मेल (E-mail)"])
        bpl_status = st.checkbox("अर्जदार दारिद्र्यरेषेखालील (BPL) आहे का?", value=False)
        submitted_a = st.form_submit_button("📄 जोडपत्र 'अ' मसुदा तयार करा")

        if submitted_a:
            fee_str = "माहिती अधिकार कायद्यानुसार १०/- रुपयाचा कोर्ट फी स्टॅम्प जोडला आहे."
            if bpl_status:
                fee_str = "अर्जदार दारिद्र्यरेषेखालील (BPL) असल्याने शुल्क माफ आहे."

            draft = f"""परिशिष्ट / जोडपत्र 'अ'
(माहितीचा अधिकार अधिनियम, २००५ च्या कलम ६(१) अन्वये अर्ज)

प्रति,
जन माहिती अधिकारी,
{karyalay}

१. अर्जदाराचे नाव : {name}
२. पूर्ण पत्ता व संपर्क : {address}
३. माहितीचा विषय : {subject}
४. कालावधी : {period}
५. हव्या असलेल्या माहितीचे वर्णन :
{desc}

६. माहिती पुरवण्याचा मार्ग : {post_type}
७. अर्जाचे शुल्क : {fee_str}

स्थान: छत्रपती संभाजीनगर
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}

अर्जदाराची स्वाक्षरी: ___________________
({name})"""
            st.session_state.generated_draft = draft
            st.session_state.draft_history.append({"title": f"RTI-A: {subject}", "date": str(datetime.date.today()), "content": draft})

# २. प्रथम अपील
elif current_form == "first_appeal":
    st.info("⚖️ जोडपत्र 'ब' - प्रथम अपील अर्ज (कलम १९ (१))")
    with st.form("form_b"):
        officer = st.text_input("प्रथम अपीलीय अधिकाऱ्याचे पदनाम व पत्ता:", value="प्रथम अपीलीय अधिकारी तथा उपजिल्हाधिकारी, छत्रपती संभाजीनगर")
        name = st.text_input("अपीलकर्त्याचे संपूर्ण नाव:", value="सतीश अशोक प्रधान")
        address = st.text_area("पत्राव्यवहाराचा पत्ता:", value="छत्रपती संभाजीनगर, मो. ८६६८२३५३९५")
        reason = st.text_area("अपील करण्याचे कारण / प्रयोजन:", value="जन माहिती अधिकाऱ्यांनी विहित मुदतीत माहिती पुरवली नाही. त्यामुळे कलम ७(६) नुसार आता माहिती विनामूल्य मिळण्यास मी पात्र आहे.")
        submitted_b = st.form_submit_button("⚖️ प्रथम अपील मसुदा तयार करा")

        if submitted_b:
            draft = f"""जोडपत्र 'ब'
(माहितीचा अधिकार अधिनियम, २००५ च्या कलम १९(१) अन्वये प्रथम अपील)

प्रति,
{officer}

१. अपीलकर्त्याचे नाव व पत्ता : {name}, {address}
२. अपीलाचे कारण व आधार :
{reason}

३. मागितलेली दाद :
जन माहिती अधिकाऱ्यांना तात्काळ व विनामूल्य संपूर्ण अचूक माहिती पुरवण्याचे निर्देश द्यावेत.

स्थान: छत्रपती संभाजीनगर
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}

अपीलकर्त्याची स्वाक्षरी: ___________________
({name})"""
            st.session_state.generated_draft = draft
            st.session_state.draft_history.append({"title": "RTI-First Appeal", "date": str(datetime.date.today()), "content": draft})

# ३. माहिती आयोग (द्वितीय अपील)
elif current_form == "second_appeal":
    st.info("🏛️ जोडपत्र 'क' - द्वितीय अपील अर्ज (राज्य माहिती आयोग कलम १९ (३))")
    with st.form("form_c"):
        commissioner = st.text_input("मा. माहिती आयुक्त व राज्य माहिती आयोग कार्यालय:", value="राज्य माहिती आयोग, खंडपीठ छत्रपती संभाजीनगर")
        name = st.text_input("अपीलकर्त्याचे संपूर्ण नाव:", value="सतीश अशोक प्रधान")
        address = st.text_area("पत्ता व संपर्क:", value="छत्रपती संभाजीनगर, मो. ८६६८२३५३९५")
        reason = st.text_area("दुसऱ्या अपीलाची सविस्तर वस्तुस्थिती:", value="प्रथम अपीलीय अधिकाऱ्यांच्या आदेशानंतरही जन माहिती अधिकाऱ्यांनी माहिती पुरवली नाही. कलम २० अन्वये दंडात्मक कारवाई करण्यात यावी.")
        submitted_c = st.form_submit_button("🏛️ द्वितीय अपील मसुदा तयार करा")

        if submitted_c:
            draft = f"""माहितीचा अधिकार अधिनियम, २००५ च्या कलम १९(३) अन्वये द्वितीय अपील अर्ज

समक्ष:
माननीय राज्य माहिती आयुक्त,
{commissioner}

अपीलकर्ता : {name}, {address}

विषय: द्वितीय अपील अर्ज स्वीकारून माहिती मिळणे व दोषी अधिकाऱ्यांवर कलम २० अन्वये दंडात्मक कारवाई होणेबाबत.

अपिलाची सविस्तर वस्तुस्थिती व मागण्या:
{reason}

स्थान: छत्रपती संभाजीनगर
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}

अपीलकर्त्याची स्वाक्षरी: ___________________
({name})"""
            st.session_state.generated_draft = draft
            st.session_state.draft_history.append({"title": "RTI-Second Appeal", "date": str(datetime.date.today()), "content": draft})

# ४. कोर्ट याचिका
elif current_form == "court":
    st.info("📜 कोर्ट याचिका / लीगल नोटीस मसुदा")
    with st.form("court_form"):
        court_type = st.selectbox("कोर्टाचा प्रकार:", ["मे. दिवाणी न्यायालय वरिष्ठ स्तर, छत्रपती संभाजीनगर", "उच्च न्यायालय (High Court)", "फौजदारी न्यायालय"])
        petitioner = st.text_input("वादी / याचिकाकर्ता:", value="सतीश अशोक प्रधान")
        respondent = st.text_input("प्रतिवादी / सामनेवाला:", value="संबंधित विभाग / खाजगी संस्था")
        matter = st.text_area("घटनेचा किंवा वादाचा मुख्य मुद्दा:", value="प्रतिवादीने कराराचे उल्लंघन केले असून बेकायदेशीर कृत्य केले आहे.")
        prayers = st.text_area("न्यायालयाकडे मागितलेली दाद (Prayer):", value="प्रतिवादीस कायदेशीर प्रतिबंध करण्यात यावा व झालेल्या नुकसानीची भरपाई देण्यात यावी.")
        submitted_court = st.form_submit_button("📜 याचिका मसुदा तयार करा")

        if submitted_court:
            draft = f"""समक्ष : माननीय {court_type}

याचिकाकर्ता: {petitioner}
विरुद्ध
प्रतिवादी: {respondent}

विषय: विनंती याचिका / अर्ज.

वादीचा सविस्तर युक्तीवाद व वस्तुस्थिती:
{matter}

प्रार्थना (Prayer):
{prayers}

स्थान: छत्रपती संभाजीनगर
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}

वादीची स्वाक्षरी: ___________________
({petitioner})"""
            st.session_state.generated_draft = draft
            st.session_state.draft_history.append({"title": "Court Petition", "date": str(datetime.date.today()), "content": draft})

# ५. शासकीय तक्रार
elif current_form == "complaint":
    st.info("📢 शासकीय तक्रार निवारण अर्ज")
    with st.form("complaint_form"):
        dept = st.text_input("तक्रार स्वीकारणारे वरिष्ठ अधिकारी / विभाग:", value="मा. जिल्हाधिकारी साहेब, छत्रपती संभाजीनगर")
        name = st.text_input("तक्रारदाराचे नाव व संपर्क:", value="सतीश अशोक प्रधान, मो. ८६६८२३५३९५")
        subject = st.text_input("तक्रारीचा मुख्य विषय:", value="शासकीय कामातील गैरव्यवहार आणि चौकशीबाबत")
        short_issue = st.text_area("तक्रारीचा सविस्तर विषय व मागण्या:", value="संबंधित अधिकाऱ्यांनी पदाचा गैरवापर करून नियमांचे उल्लंघन केले आहे. दोषींवर कारवाई करण्यात यावी.")
        submitted_comp = st.form_submit_button("📢 तक्रार अर्ज तयार करा")

        if submitted_comp:
            draft = f"""प्रशासकीय तक्रार अर्ज

प्रति,
{dept}

तक्रारदार : {name}
विषय : {subject}

तक्रारीचा सविस्तर तपशील व मागणी:
{short_issue}

स्थान: छत्रपती संभाजीनगर
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}

आपला नम्र,
___________________
({name})"""
            st.session_state.generated_draft = draft
            st.session_state.draft_history.append({"title": f"Complaint: {subject}", "date": str(datetime.date.today()), "content": draft})

# ६. प्रतिज्ञापत्र (Affidavit)
elif current_form == "affidavit":
    st.info("📝 प्रतिज्ञापत्र (Affidavit Draft)")
    with st.form("affidavit_form"):
        name = st.text_input("प्रतिज्ञापत्र करणाऱ्याचे पूर्ण नाव:", value="सतीश अशोक प्रधान")
        address = st.text_area("पूर्ण पत्ता:", value="छत्रपती संभाजीनगर")
        purpose = st.text_input("प्रतिज्ञापत्राचे कारण:", value="शासकीय योजनेच्या लाभासाठी व सत्यता पडताळणीसाठी")
        statements = st.text_area("सत्य विधाने:", value="१. मी असे प्रतिज्ञापूर्वक सांगतो की वरील पत्त्यावर मी कायमस्वरूपी राहणारा आहे.\n२. माझ्याद्वारे दिलेली माहिती सत्य व बरोबर आहे.")
        submitted_aff = st.form_submit_button("📝 प्रतिज्ञापत्र तयार करा")

        if submitted_aff:
            draft = f"""प्रतिज्ञापत्र (AFFIDAVIT)

मी, {name}, राहणार: {address}, प्रतिज्ञापत्राद्वारे लिहून देतो की:

१. हे प्रतिज्ञापत्र मी {purpose} या कारणासाठी सादर करत आहे.
२. माझे सत्य कथन खालीलप्रमाणे आहे:
{statements}

सत्यता पडताळणी (Verification):
आज दिनांक {datetime.date.today().strftime('%d/%m/%Y')} रोजी छत्रपती संभाजीनगर येथे वरील मजकूर खरा असल्याबाबत प्रतिज्ञापूर्वक स्वाक्षरी केली.

प्रतिज्ञापत्र करणारा: ___________________
({name})"""
            st.session_state.generated_draft = draft
            st.session_state.draft_history.append({"title": f"Affidavit: {purpose}", "date": str(datetime.date.today()), "content": draft})

# ७. ग्राहक मंच
elif current_form == "consumer":
    st.info("🛒 ग्राहक मंच (Consumer Forum) अर्ज मसुदा")
    with st.form("consumer_form"):
        name = st.text_input("तक्रारदाराचे नाव व पत्ता:", value="सतीश अशोक प्रधान, छत्रपती संभाजीनगर")
        company = st.text_input("सामनेवाला (कंपनी/विक्रेता):", value="मे. फायनान्स कंपनी / शोरूम")
        claim = st.text_input("मागितलेली भरपाई रक्कम (रु.):", value="५०,०००/-")
        complaint_desc = st.text_area("सेवेतील त्रुटी व फसवणुकीचा सविस्तर तपशील:", value="विरोधी पक्षाने सेवेत त्रुटी ठेवली असून अनुचित व्यापार पद्धतीचा वापर केला आहे.")
        submitted_cons = st.form_submit_button("🛒 ग्राहक मंच मसुदा तयार करा")

        if submitted_cons:
            draft = f"""समक्ष : माननीय जिल्हा ग्राहक वाद निवारण आयोग, छत्रपती संभाजीनगर

तक्रारदार: {name}
विरुद्ध
सामनेवाला: {company}

विषय: ग्राहक संरक्षण कायदा २०१९ अन्वये तक्रार अर्ज.

तक्रारीचे कारण व सेवेतील त्रुटी:
{complaint_desc}

मागितलेली भरपाई:
तक्रारदारास झालेल्या त्रासाबद्दल रु. {claim} भरपाई म्हणून देववावेत.

स्थान: छत्रपती संभाजीनगर
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}

तक्रारदाराची स्वाक्षरी: ___________________"""
            st.session_state.generated_draft = draft
            st.session_state.draft_history.append({"title": "Consumer Complaint", "date": str(datetime.date.today()), "content": draft})

# ==========================================
# ७. मसुदा डिस्प्ले, PDF, Word व डाऊनलोड ऑप्शन्स
# ==========================================
if st.session_state.generated_draft and current_form != "ai_chat":
    st.markdown("---")
    st.subheader("📋 तयार झालेला कायदेशीर मसुदा (Preview):")
    st.markdown(f'<div class="draft-preview">{st.session_state.generated_draft}</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📥 मसुदा डाऊनलोड व शेअर करा:")
    
    col_pdf, col_docx, col_txt, col_wa, col_mail = st.columns(5)
    
    with col_pdf:
        pdf_bytes = generate_colorful_a4_pdf("कायदेशीर मसुदा", st.session_state.generated_draft)
        st.download_button(label="🔴 A4 PDF डाऊनलोड", data=pdf_bytes, file_name="Legal_Draft_A4.pdf", mime="application/pdf")
        
    with col_docx:
        docx_file = generate_docx(st.session_state.generated_draft)
        st.download_button(label="📝 Word (DOCX)", data=docx_file, file_name="Legal_Draft.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        
    with col_txt:
        st.download_button(label="📄 TXT डाऊनलोड", data=st.session_state.generated_draft, file_name="Legal_Draft.txt", mime="text/plain")

    wa_link, mail_link = get_share_links(st.session_state.generated_draft)
    with col_wa:
        st.markdown(f'<a href="{wa_link}" target="_blank"><button style="width:100%; background-color:#22C55E; color:white; border:none; padding:8px; border-radius:8px; font-weight:bold;">📲 WhatsApp</button></a>', unsafe_allow_html=True)
    with col_mail:
        st.markdown(f'<a href="{mail_link}" target="_blank"><button style="width:100%; background-color:#3B82F6; color:white; border:none; padding:8px; border-radius:8px; font-weight:bold;">✉️ Email</button></a>', unsafe_allow_html=True)

# ==========================================
# ८. सोशल मीडिया शेअर बटण
# ==========================================
st.markdown("---")
app_link = "https://rti-ai-app-eydmnrwsnhwwhmryv7nn4v.streamlit.app/?v=3"
share_text = f"घरबसल्या RTI अर्ज, शासकीय तक्रारी व AI मदतीसाठी हे मोफत AI ॲप वापरा: {app_link}"

whatsapp_url = f"https://api.whatsapp.com/send?text={share_text}"
facebook_url = f"https://www.facebook.com/sharer/sharer.php?u={app_link}"
telegram_url = f"https://t.me/share/url?url={app_link}&text=RTI व सर्वसमावेशक AI ॲप"

single_share_code = f"""
<style>
.share-details {{ background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); border: 2px solid #ffd700; border-radius: 12px; padding: 12px; color: white; margin-bottom: 20px; }}
.share-summary {{ font-size: 16px; font-weight: bold; cursor: pointer; color: #ffd700; }}
.share-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 8px; margin-top: 15px; }}
.share-item {{ display: flex; align-items: center; justify-content: center; padding: 10px; border-radius: 8px; color: white !important; font-weight: bold; text-decoration: none !important; }}
</style>
<details class="share-details">
    <summary class="share-summary">📢 हे ॲप मित्रांना शेअर करा (सर्व पर्याय) ▼</summary>
    <div class="share-grid">
        <a href="{whatsapp_url}" target="_blank" class="share-item" style="background-color: #25D366;">WhatsApp</a>
        <a href="{facebook_url}" target="_blank" class="share-item" style="background-color: #1877F2;">Facebook</a>
        <a href="{telegram_url}" target="_blank" class="share-item" style="background-color: #0088cc;">Telegram</a>
    </div>
</details>
"""
st.markdown(single_share_code, unsafe_allow_html=True)

# ==========================================
# ९. AI चॅट लॉजिक (सर्वात शेवटी - एरर-फ्री ऑटो-फॉलबॅक सह)
# ==========================================
st.markdown("---")
st.subheader("💬 AI कायदेशीर मदत व चॅट बॉक्स")

# जुने चॅट मेसेज दाखवणे
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# नवीन चॅट इनपुट
if user_input := st.chat_input("आकांक्षा AI ला कायदेशीर प्रश्न विचारा..."):
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("AI विचार करत आहे व उत्तर तयार करत आहे..."):
            # API चालणारे मूळ नाव आणि मॅन्युअल नाव दोन्ही सिस्टममध्ये समाविष्ट केले आहे
            auto_models = [
                "gemini-2.5-flash", 
                "gemini-2.0-flash", 
                "gemini-1.5-flash",
                "gemini-1.5-pro",
                "gemini-3.6-flash",
                "gemini-3.5-flash-lite",
                "gemini-3.1-pro"
            ]
            response_text = None
            last_error = ""
            for m_name in auto_models:
                try:
                    model = genai.GenerativeModel(m_name)
                    response = model.generate_content([UNIVERSAL_SYSTEM_PROMPT, user_input])
                    if response and response.text:
                        response_text = response.text
                        break
                except Exception as err:
                    last_error = str(err)
                    continue
            if response_text:
                st.markdown(response_text)
                st.session_state.chat_history.append({"role": "assistant", "content": response_text})
            else:
                st.error(f"❌ API कनेक्ट करताना अडचण येत आहे. कृपया API Key तपासा: {last_error}")
