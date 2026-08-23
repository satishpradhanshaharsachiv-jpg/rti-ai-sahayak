import streamlit as st
from PIL import Image
import google.generativeai as genai
from gtts import gTTS
import io

# १. पेज कॉन्फिगरेशन
st.set_page_config(page_title="आकांक्षा RTI AI", layout="wide")

# २. स्ट्रीमलिट टूलबार लपवण्यासाठी CSS (ब्राउझरचा हेडर चालू राहील)
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        div[data-testid="stToolbar"] {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# ३. निवडलेला फॉर्म ट्रॅक करणे
query_params = st.query_params
current_form = query_params.get("form", "jodpatra_a")

# ४. शासकीय राजपत्राच्या हुबेहूब A4 नमुन्यात PDF/प्रिंट तयार करणारे फंक्शन
def create_official_a4_pdf(title_header, rule_text, main_title, body_content, applicant_name, applicant_address, applicant_mobile):
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>{main_title}</title>
    <style>
        @page {{ size: A4; margin: 15mm 20mm 20mm 20mm; }}
        body {{
            font-family: 'Arial', 'Helvetica', sans-serif;
            font-size: 13pt;
            line-height: 1.5;
            color: #000;
            padding: 5px;
        }}
        .stamp-box {{
            float: right;
            border: 1px dashed #000;
            padding: 8px;
            font-size: 9pt;
            text-align: center;
            width: 140px;
            margin-bottom: 10px;
        }}
        .title-container {{ text-align: center; margin-top: 10px; margin-bottom: 20px; clear: both; }}
        .jodpatra-title {{ font-size: 18pt; font-weight: bold; text-decoration: underline; margin-bottom: 4px; }}
        .rule-text {{ font-size: 11pt; font-weight: bold; margin-bottom: 4px; }}
        .act-title {{ font-size: 13pt; font-weight: bold; }}
        .content {{ font-size: 12pt; text-align: justify; margin-top: 15px; line-height: 1.6; }}
        .footer-section {{ margin-top: 40px; float: right; text-align: left; width: 250px; font-size: 12pt; }}
        .bottom-clear {{ clear: both; }}
        @media print {{
            .no-print {{ display: none; }}
        }}
        .btn-print {{
            background-color: #27ae60; color: white; padding: 10px 18px; border: none; border-radius: 6px; font-size: 15px; cursor: pointer; margin-bottom: 15px; font-weight: bold;
        }}
    </style>
    </head>
    <body>
        <button class="btn-print no-print" onclick="window.print()">🖨️ A4 साईज PDF म्हणून सेव्ह / प्रिंट करा</button>
        
        <div class="stamp-box">
            येथे कोर्ट फी मुद्रांक चिकटवावा
        </div>
        
        <div class="title-container">
            <div class="jodpatra-title">{title_header}</div>
            <div class="rule-text">{rule_text}</div>
            <div class="act-title">{main_title}</div>
        </div>
        
        <div class="content">
            {body_content}
        </div>
        
        <div class="footer-section">
            <br>
            <strong>अर्जदाराची सही / अंगठा:</strong> _____________<br>
            <strong>नाव:</strong> {applicant_name}<br>
            <strong>पत्ता:</strong> {applicant_address}<br>
            <strong>मोबाईल:</strong> {applicant_mobile}
        </div>
        <div class="bottom-clear"></div>
    </body>
    </html>
    """
    return html_code

# ५. ३D डिझाईन आणि रंगांसाठी CSS
st.markdown("""
<style>
.header-card {
    background: linear-gradient(135deg, #0f172a, #1e1b4b);
    border: 2px solid #ffd700;
    border-radius: 16px;
    padding: 16px 12px;
    text-align: center;
    box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.5);
    margin-bottom: 20px;
}
.header-title { color: #ffd700; font-size: 19px; font-weight: bold; margin-bottom: 6px; line-height: 1.3; }
.header-subtitle { color: #ff7675; font-size: 13px; font-weight: bold; margin-bottom: 8px; }
.header-divider { border-top: 1px dashed #666; margin: 8px 0; }
.header-footer { color: #ffffff; font-size: 13px; }

.btn-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    margin-bottom: 25px;
}
@media (max-width: 600px) {
    .btn-container { grid-template-columns: repeat(2, 1fr); }
}

.custom-btn {
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    padding: 12px 4px; text-decoration: none !important; color: white !important;
    font-weight: bold; font-size: 13px; border-radius: 12px; text-align: center;
    box-shadow: inset 0px 2px 3px rgba(255, 255, 255, 0.5), 0px 5px 8px rgba(0, 0, 0, 0.35);
    border-top: 1px solid rgba(255, 255, 255, 0.4); border-bottom: 3px solid rgba(0, 0, 0, 0.4);
}
.btn-green { background: linear-gradient(180deg, #11998e 0%, #38ef7d 100%); }
.btn-orange { background: linear-gradient(180deg, #FF416C 0%, #FF4B2B 100%); }
.btn-royal-blue { background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%); }
.btn-3d-blue { background: linear-gradient(180deg, #00c6ff 0%, #0072ff 100%); }
.btn-purple { background: linear-gradient(180deg, #8E2DE2 0%, #4A00E0 100%); }
.btn-red { background: linear-gradient(180deg, #e52d27 0%, #b31217 100%); }
.btn-gold { background: linear-gradient(180deg, #ffe066 0%, #d4af37 50%, #996515 100%); color: #000 !important; }
.btn-cyan { background: linear-gradient(180deg, #00B4DB 0%, #0083B0 100%); }
</style>
""", unsafe_allow_html=True)

# ६. हेडर बॅनर आणि ३D बटणे
full_app_html = """
<div class="header-card">
    <div class="header-title">✨ आकांक्षा एंटरप्राईजेस RTI AI ॲप कायदेशीर सहाय्य ✨</div>
    <div class="header-subtitle">⚡ घरबसल्या RTI अर्ज व शासकीय तक्रार एका सेकंदात A4 साईज मध्ये मोफत मिळवा ⚡</div>
    <div class="header-divider"></div>
    <div class="header-footer">👤 सतीश अशोक प्रधान | 📱 मो. ८६६8235395</div>
</div>

<div class="btn-container">
    <a href="?form=jodpatra_a" target="_self" class="custom-btn btn-green">📄<br>जोडपत्र 'अ'</a>
    <a href="?form=first_appeal" target="_self" class="custom-btn btn-orange">⚖️<br>प्रथम अपील</a>
    <a href="?form=second_appeal" target="_self" class="custom-btn btn-royal-blue">🏛️<br>माहिती आयोग</a>
    <a href="?form=ai_chat" target="_self" class="custom-btn btn-3d-blue">✨<br>AI चॅट</a>
    <a href="?form=court" target="_self" class="custom-btn btn-purple">📜<br>कोर्ट याचिका</a>
    <a href="?form=complaint" target="_self" class="custom-btn btn-red">📣<br>शासकीय तक्रार</a>
    <a href="?form=rti_portal" target="_self" class="custom-btn btn-gold">🌐<br>आरटीआय ऑनलाईन पोर्टल सहाय्य</a>
    <a href="?form=consumer" target="_self" class="custom-btn btn-cyan">🛒<br>ग्राहक मंच</a>
</div>
"""
st.markdown(full_app_html, unsafe_allow_html=True)

# ---------------------------------------------------------
# ७. फॉर्म्स व AI चॅट ऑपरेशन्स
# ---------------------------------------------------------

if current_form == "jodpatra_a":
    st.info("📋 जोडपत्र 'अ' - माहितीचा अधिकार अधिनियम, २००५ अन्वये अर्ज (नियम ३)")
    with st.form("form_a"):
        karyalay = st.text_input("जन माहिती अधिकाऱ्याच्या कार्यालयाचे नाव व पत्ता")
        name = st.text_input("अर्जदाराचे संपूर्ण नाव", placeholder="तुमचे पूर्ण नाव लिहा")
        address = st.text_area("अर्जदाराचा पूर्ण पत्रव्यवहाराचा पत्ता", placeholder="घर क्र., रस्ता, भाग, शहर...")
        mobile = st.text_input("मोबाईल क्रमांक", placeholder="उदा. 9876543210")
        subject = st.text_input("माहितीचा विषय")
        period = st.text_input("माहितीचा कालावधी", placeholder="उदा. २०२४ ते २०२६")
        desc = st.text_area("हव्या असलेल्या माहितीचे वर्णन (सविस्तर मुद्दे)")
        post_type = st.selectbox("माहिती कशी हवी आहे?", ["टपालाद्वारे (साधे/नोंदणीकृत)", "व्यक्तिशः (स्वहस्ते)"])
        submitted_a = st.form_submit_button("📄 जोडपत्र 'अ' A4 अर्ज तयार करा")
        
        if submitted_a:
            body = f"""
            <strong>प्रति,</strong><br>
            जन माहिती अधिकारी,<br>
            {karyalay}<br><br>
            <strong>१. अर्जदाराचे संपूर्ण नाव:</strong> {name}<br>
            <strong>२. पत्ता:</strong> {address}<br><br>
            <strong>३. हव्या असलेल्या माहितीचा तपशील:</strong><br>
            (एक) माहितीचा विषय: {subject}<br>
            (दोन) ज्या कालावधी संबंधात माहिती हवी असेल तो कालावधी: {period}<br>
            (तीन) हव्या असलेल्या माहितीचे वर्णन: {desc}<br>
            (चार) माहिती टपालाद्वारे हवी आहे की व्यक्तिशः हवी आहे: {post_type}<br>
            (पाच) टपालाद्वारे हवी असल्यास: नोंदणीकृत टपालाने<br><br>
            <strong>४. अर्जदार दारिद्र्यरेषेखालील आहे किंवा कसे:</strong> नाही.<br><br>
            <strong>ठिकाण:</strong> _______________<br>
            <strong>दिनांक:</strong> ___/___/२०__
            """
            pdf_code = create_official_a4_pdf("जोडपत्र 'अ'", "(नियम ३ पहा)", "माहितीचा अधिकार अधिनियम, २००५ अन्वये माहिती मिळविण्यासाठीच्या अर्जाचा नमुना", body, name, address, mobile)
            st.session_state.draft_a_text = f"जोडपत्र 'अ' (नियम ३ पहा)\nप्रति,\nजन माहिती अधिकारी, {karyalay}\n\n१. नाव: {name}\n२. पत्ता: {address}\n\n३. माहितीचा तपशील:\n- विषय: {subject}\n- कालावधी: {period}\n- वर्णन: {desc}\n- टपाल प्रकार: {post_type}"
            st.session_state.pdf_a = pdf_code

    if 'draft_a_text' in st.session_state:
        st.success("अर्जाचा मसुदा तयार झाला आहे!")
        st.subheader("📋 अर्जाचा मसुदा पाहणी:")
        st.text_area("", st.session_state.draft_a_text, height=220)
        st.download_button("📥 जोडपत्र 'अ' (A4 PDF) डाऊनलोड करा", data=st.session_state.pdf_a, file_name="Jodpatra_A_RTI.html", mime="text/html")

elif current_form == "first_appeal":
    st.info("⚖️ जोडपत्र 'ब' - प्रथम अपील अर्ज (कलम १९ (१) - नियम ५(१))")
    with st.form("form_b"):
        officer = st.text_input("प्रथम अपीलीय अधिकाऱ्याचे पदनाम व पत्ता")
        name = st.text_input("अपीलकाराचे संपूर्ण नाव", placeholder="तुमचे नाव")
        address = st.text_area("पत्रव्यवहाराचा पत्ता", placeholder="तुमचा पत्ता")
        mobile = st.text_input("मोबाईल क्रमांक")
        pio_details = st.text_input("संबंधित जन माहिती अधिकाऱ्याचा तपशील")
        reason = st.text_area("अपील करण्याचे कारण / प्रयोजन", placeholder="उदा. वेळेत माहिती न दिल्याने / चुकीची माहिती दिल्याने...")
        info_detail = st.text_area("आवश्यक असलेल्या माहितीचा तपशील व विभाग")
        submitted_b = st.form_submit_button("⚖️ जोडपत्र 'ब' A4 अपील तयार करा")
        
        if submitted_b:
            body = f"""
            <strong>प्रति,</strong><br>
            प्रथम अपीलीय अधिकारी,<br>
            {officer}<br><br>
            <strong>(१) अपीलकाराचे पूर्ण नाव:</strong> {name}<br>
            <strong>(२) पूर्ण पत्ता:</strong> {address}<br>
            <strong>(३) संबंधित जन माहिती अधिकाऱ्याचा तपशील:</strong> {pio_details}<br>
            <strong>(४) ज्या निर्णयाविरुद्ध अपील करावयाचे आहे त्याची तारीख:</strong> माहिती मिळाली नाही / अनिर्णित<br>
            <strong>(५) अपील करण्याचे प्रयोजन:</strong> {reason}<br>
            <strong>(६) आवश्यक असलेल्या माहितीचा तपशील:</strong> {info_detail}<br>
            <strong>(७) माहितीशी संबंधित कार्यालय व विभाग:</strong> मूळ अर्ज जोडपत्र 'अ' ची छायाप्रत सोबत जोडली आहे.<br><br>
            <strong>ठिकाण:</strong> _______________<br>
            <strong>दिनांक:</strong> ___/___/२०__
            """
            pdf_code = create_official_a4_pdf("जोडपत्र 'ब'", "(नियम ५(१) नुसार)", "माहितीचा अधिकार कायदा, २००५ - कलम १९ (१) अन्वये प्रथम अपील अर्ज", body, name, address, mobile)
            st.session_state.draft_b_text = f"जोडपत्र 'ब' (नियम ५(१))\nप्रति, प्रथम अपीलीय अधिकारी, {officer}\n१. अपीलकार: {name}\n२. पत्ता: {address}\n३. प्रयोजन: {reason}"
            st.session_state.pdf_b = pdf_code

    if 'draft_b_text' in st.session_state:
        st.success("प्रथम अपील मसुदा तयार झाला आहे!")
        st.subheader("📋 मसुदा पाहणी:")
        st.text_area("", st.session_state.draft_b_text, height=220)
        st.download_button("📥 जोडपत्र 'ब' (A4 PDF) डाऊनलोड करा", data=st.session_state.pdf_b, file_name="Jodpatra_B_First_Appeal.html", mime="text/html")

elif current_form == "second_appeal":
    st.info("🏛️ जोडपत्र 'क' - द्वितिय अपील अर्ज (कलम १९ (३) - नियम ५(२))")
    with st.form("form_c"):
        commissioner = st.text_input("मा. माहिती आयुक्त व राज्य माहिती आयोग कार्यालय पत्ता")
        name = st.text_input("अपीलकाराचे संपूर्ण नाव", placeholder="तुमचे नाव")
        address = st.text_area("पत्रव्यवहाराचा पत्ता", placeholder="तुमचा पत्ता")
        mobile = st.text_input("मोबाईल क्रमांक")
        pio_info = st.text_input("संबंधित जन माहिती अधिकाऱ्याचा तपशील")
        fa_info = st.text_input("प्रथम अपीलीय प्राधिकाऱ्याचा तपशील")
        reason = st.text_area("दुसरे अपील करण्याचे प्रयोजन")
        submitted_c = st.form_submit_button("🏛️ जोडपत्र 'क' A4 द्वितीय अपील तयार करा")
        
        if submitted_c:
            body = f"""
            <strong>प्रति,</strong><br>
            मा. माहिती आयुक्त,<br>
            राज्य माहिती आयोग कार्यालय,<br>
            {commissioner}<br><br>
            <strong>(१) अपीलकाराचे पूर्ण नाव:</strong> {name}<br>
            <strong>(२) पत्रव्यवहाराचा पत्ता:</strong> {address}<br>
            <strong>(३) संबंधित जन माहिती अधिकाऱ्याचा तपशील:</strong> {pio_info}<br>
            <strong>(४) प्रथम अपीलीय प्राधिकाऱ्याचा तपशील:</strong> {fa_info}<br>
            <strong>(५) दुसरे अपील करण्याचे प्रयोजन:</strong> {reason}<br>
            <strong>(६) आवश्यक असलेल्या माहितीचा तपशील:</strong> सोबत मूळ अर्ज जोडपत्र 'अ' व प्रथम अपीलाची प्रत जोडली आहे.<br><br>
            <strong>ठिकाण:</strong> _______________<br>
            <strong>दिनांक:</strong> ___/___/२०__
            """
            pdf_code = create_official_a4_pdf("जोडपत्र 'क'", "(नियम ५(२) नुसार)", "माहितीचा अधिकार कायदा, २००५ - कलम १९ (३) अन्वये द्वितिय अपील अर्ज", body, name, address, mobile)
            st.session_state.draft_c_text = f"जोडपत्र 'क' (नियम ५(२))\nप्रति, मा. माहिती आयुक्त, {commissioner}\nअपीलकार: {name}\nप्रयोजन: {reason}"
            st.session_state.pdf_c = pdf_code

    if 'draft_c_text' in st.session_state:
        st.success("द्वितीय अपील मसुदा तयार झाला आहे!")
        st.subheader("📋 मसुदा पाहणी:")
        st.text_area("", st.session_state.draft_c_text, height=220)
        st.download_button("📥 जोडपत्र 'क' (A4 PDF) डाऊनलोड करा", data=st.session_state.pdf_c, file_name="Jodpatra_C_Second_Appeal.html", mime="text/html")

elif current_form == "ai_chat":
    st.info("✨ आकांक्षा AI चॅट असिस्टंट - RTI, कायदेशीर व शासकीय कामांसाठी मोफत AI मदत व ऑडिओ ऐका")

    GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", "")
    if GEMINI_API_KEY:
        genai.configure(api_key=GEMINI_API_KEY)
    else:
        st.warning("⚠️ कृपया Streamlit Secrets मध्ये GEMINI_API_KEY जोडा.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    uploaded_file = st.file_uploader("📷 शासकीय पत्र किंवा कागदपत्राचा फोटो अपलोड करा (ऐच्छिक):", type=["jpg", "jpeg", "png"])
    image_data = None
    if uploaded_file:
        image_data = Image.open(uploaded_file)
        st.image(image_data, caption="अपलोड केलेले कागदपत्र", width=250)

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message["role"] == "assistant" and "audio_data" in message:
                st.audio(message["audio_data"], format="audio/mp3")

    if user_input := st.chat_input("तुमचा प्रश्न किंवा अडचण येथे लिहा..."):
        st.chat_message("user").markdown(user_input)
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        system_prompt = """
        तू 'आकांक्षा RTI व कायदेशीर AI असिस्टंट' आहेस. 
        तुझे काम भारतातील व महाराष्ट्रातील नागरिकांना माहिती अधिकार अधिनियम (RTI 2005), 
        ग्राहक संरक्षण कायदा, शासकीय तक्रारी, कोर्ट मसुदा आणि कायदेशीर बाबींवर सोप्या व अचूक मराठीत मार्गदर्शन करणे आहे.
        """

        with st.chat_message("assistant"):
            with st.spinner("AI विचार करत आहे व स्पष्ट मराठी आवाज तयार करत आहे..."):
                auto_models = [
                    "gemini-2.0-flash",
                    "gemini-2.0-flash-lite",
                    "gemini-1.5-flash",
                    "gemini-1.5-pro" 
                    "gemini-2.5-flash",
                    "gemini-3.7-flash",]

                response_text = None
                last_error = ""

                for m_name in auto_models:
                    try:
                        model = genai.GenerativeModel(m_name)
                        if image_data:
                            response = model.generate_content([system_prompt, user_input, image_data])
                        else:
                            response = model.generate_content(f"{system_prompt}\n\nयुझर प्रश्न: {user_input}")
                        
                        if response and response.text:
                            response_text = response.text
                            break
                    except Exception as err:
                        last_error = str(err)
                        continue

                if response_text:
                    st.markdown(response_text)
                    
                    try:
                        tts = gTTS(text=response_text, lang='mr', slow=False)
                        audio_fp = io.BytesIO()
                        tts.write_to_fp(audio_fp)
                        audio_bytes = audio_fp.getvalue()
                        
                        st.audio(audio_bytes, format="audio/mp3")
                        
                        st.session_state.chat_history.append({
                            "role": "assistant", 
                            "content": response_text,
                            "audio_data": audio_bytes
                        })
                    except Exception as tts_err:
                        st.session_state.chat_history.append({"role": "assistant", "content": response_text})
                else:
                    st.error(f"❌ API एरर: {last_error}")

elif current_form == "court":
    st.info("📜 कोर्ट याचिका / लीगल ब्रीफ (वकिलांसाठी मसुदा)")
    with st.form("court_form"):
        court_type = st.selectbox("कोर्टाचा प्रकार", ["जिल्हा व सत्र न्यायालय", "उच्च न्यायालय (High Court)", "दीवाणी न्यायालय (Civil Court)", "महसूल न्यायालय"])
        petitioner = st.text_input("वादी / अर्जदाराचे नाव", placeholder="तुमचे नाव")
        address = st.text_area("अर्जदाराचा पत्ता")
        mobile = st.text_input("मोबाईल क्रमांक")
        respondent = st.text_input("प्रतिवादी / विरोधी पक्षाचे नाव")
        matter = st.text_area("घटनेचा किंवा वादाचा मुख्य मुद्दा")
        submitted_court = st.form_submit_button("📜 वकिलांसाठी मसुदा तयार करा")
        
        if submitted_court:
            body = f"""
            <strong>समक्ष: {court_type}</strong><br><br>
            <strong>वादी / अर्जदार:</strong> {petitioner}<br>
            <strong>विरुद्ध</strong><br>
            <strong>प्रतिवादी:</strong> {respondent}<br><br>
            <strong>विषय:</strong> कायदेशीर दाव्याचा / याचिकेचा प्राथमिक मसुदा व तथ्ये.<br><br>
            <strong>प्रकरणाची पार्श्वभूमी व मुख्य मुद्दे:</strong><br>{matter}<br><br>
            <strong>मागणी / प्रार्थना (Relief Claimed):</strong><br>
            १. वरील तथ्यांच्या आधारे वादीस योग्य तो कायदेशीर न्याय व भरपाई देण्यात यावी.<br>
            २. प्रतिवादीस तात्काळ समज पत्र (Notice) जारी करण्यात यावे.
            """
            pdf_code = create_official_a4_pdf("कोर्ट याचिका मसुदा", "कायदेशीर मसुदा नमुना", f"समक्ष: {court_type}", body, petitioner, address, mobile)
            st.session_state.draft_court_text = f"समक्ष: {court_type}\nवादी: {petitioner}\nविरुद्ध\nप्रतिवादी: {respondent}\nमुद्दा: {matter}"
            st.session_state.pdf_court = pdf_code

    if 'draft_court_text' in st.session_state:
        st.success("कोर्ट याचिका मसुदा तयार झाला आहे!")
        st.subheader("📋 मसुदा पाहणी:")
        st.text_area("", st.session_state.draft_court_text, height=220)
        st.download_button("📥 कोर्ट मसुदा (A4 PDF) डाऊनलोड करा", data=st.session_state.pdf_court, file_name="Court_Petition_Draft.html", mime="text/html")

elif current_form == "complaint":
    st.info("📣 शासकीय तक्रार निवारण अर्ज")
    with st.form("complaint_form"):
        dept = st.text_input("शासकीय विभाग / कार्यालय", placeholder="उदा. महानगरपालिका / पोलीस स्टेशन / महावितरण")
        name = st.text_input("तक्रारदाराचे नाव", placeholder="तुमचे नाव")
        address = st.text_area("तक्रारदाराचा पत्ता")
        mobile = st.text_input("मोबाईल क्रमांक")
        short_issue = st.text_input("तक्रारीचा विषय (केवळ २-३ शब्दांत)", placeholder="उदा. रस्त्यावरील खड्डे / कचरा समस्या")
        details = st.text_area("समस्येची माहिती")
        submitted_comp = st.form_submit_button("📣 शासकीय तक्रार अर्ज तयार करा")
        
        if submitted_comp:
            body = f"""
            <strong>प्रति,</strong><br>
            मा. विभाग प्रमुख / अधिकारी,<br>
            {dept}<br><br>
            <strong>विषय:</strong> {short_issue} बाबत तात्काळ शासकीय तक्रार व कारवाईबाबत.<br><br>
            <strong>महोदय,</strong><br><br>
            मी {name}, नागरिक या पत्राद्वारे आपल्या निदर्शनास आणून देतो की, माझ्या भागात खालीलप्रमाणे गंभीर समस्या निर्माण झाली आहे:<br><br>
            <strong>तक्रारीचा तपशील:</strong><br>{details}<br><br>
            तरी वरील समस्येचे गांभीर्य लक्षात घेऊन संबंधितांवर तात्काळ योग्य ती कारवाई करावी व मला केलेल्या कारवाईचा अहवाल पाठवावा.
            """
            pdf_code = create_official_a4_pdf("शासकीय तक्रार अर्ज", "अधिकृत तक्रार नमुना", "शासकीय विभाग तक्रार निवारण पत्र", body, name, address, mobile)
            st.session_state.draft_comp_text = f"प्रति, मा. अधिकारी, {dept}\nविषय: {short_issue}\nतक्रारदार: {name}\nतपशील: {details}"
            st.session_state.pdf_comp = pdf_code

    if 'draft_comp_text' in st.session_state:
        st.success("तक्रार अर्ज तयार झाला आहे!")
        st.subheader("📋 अर्जाचा मसुदा पाहणी:")
        st.text_area("", st.session_state.draft_comp_text, height=220)
        st.download_button("📥 तक्रार अर्ज (A4 PDF) डाऊनलोड करा", data=st.session_state.pdf_comp, file_name="Govt_Complaint.html", mime="text/html")

elif current_form == "rti_portal":
    st.info("🌐 आरटीआय ऑनलाईन पोर्टल मार्गदर्शन")
    st.write("• **महाराष्ट्र आरटीआय पोर्टल:** १५० शब्दांची मर्यादा व ₹१० शुल्क.")
    st.write("• **केंद्रीय आरटीआय पोर्टल:** ५०० शब्दांची मर्यादा व ₹१० शुल्क.")

elif current_form == "consumer":
    st.info("🛒 ग्राहक मंच (Consumer Commission) संपूर्ण मार्गदर्शन व अर्ज मसुदा")
    st.markdown("""
    <strong>📌 प्राथमिक तयारी व कोर्ट अधिकार क्षेत्र:</strong>
    * **जिल्हा आयोग:** ₹१ कोटी रुपयांपर्यंतचे दावे.
    * **राज्य आयोग:** ₹१ कोटी ते ₹१० कोटी रुपयांपर्यंतचे दावे.
    * **राष्ट्रीय आयोग:** ₹१० कोटींपेक्षा जास्त रक्कमेचे दावे.
    * **e-Daakhil पोर्टल:** ई-डाखील (`edaakhil.nic.in`) वर ऑनलाईन तक्रार दाखल करता येते.
    """)
    st.markdown("---")
    
    with st.form("consumer_form"):
        name = st.text_input("तक्रारदाराचे नाव", placeholder="तुमचे नाव")
        address = st.text_area("तक्रारदाराचा पत्ता")
        mobile = st.text_input("मोबाईल क्रमांक")
        company = st.text_input("सामनेवाला (ज्या कंपनी/दुकानाची तक्रार आहे)")
        product = st.text_input("खरेदी केलेली वस्तू / घेतलेली सेवा")
        amount = st.text_input("फसवणुकीची किंवा नुकसानाची रक्कम (₹)")
        complaint_desc = st.text_area("काय फसवणूक किंवा सेवेत त्रुटी झाली?")
        submitted_cons = st.form_submit_button("🛒 ग्राहक मंच तक्रार मसुदा तयार करा")
        
        if submitted_cons:
            body = f"""
            <strong>समक्ष: मा. जिल्हा ग्राहक वाद निवारण आयोग</strong><br><br>
            <strong>तक्रारदार:</strong> {name}<br>
            <strong>विरुद्ध</strong><br>
            <strong>सामनेवाला (विपक्षी):</strong> {company}<br><br>
            <strong>तक्रारीचा अर्ज: ग्राहक संरक्षण कायदा २०१९ अन्वये.</strong><br><br>
            १. तक्रारदाराने सामनेवाला यांच्याकडून '{product}' ही वस्तू/सेवा खरेदी केली होती.<br>
            २. नुकसानाची रक्कम: ₹ {amount}/-<br><br>
            <strong>३. तक्रारीचे कारण व फसवणूक:</strong><br>{complaint_desc}<br><br>
            <strong>मागणी:</strong><br>तक्रारदारास नुकसान भरपाईपोटी ₹ {amount}/- परत मिळावेत व मानसिक त्रासापोटी योग्य भरपाई मंजूर व्हावी.
            """
            pdf_code = create_official_a4_pdf("ग्राहक मंच तक्रार अर्ज", "ग्राहक संरक्षण कायदा २०१९ अन्वये", "समक्ष: मा. जिल्हा ग्राहक वाद निवारण आयोग", body, name, address, mobile)
            st.session_state.draft_cons_text = f"समक्ष: मा. जिल्हा ग्राहक वाद निवारण आयोग\nतक्रारदार: {name}\nविरुद्ध: {company}\nरक्कम: ₹ {amount}/-\nकारण: {complaint_desc}"
            st.session_state.pdf_cons = pdf_code

    if 'draft_cons_text' in st.session_state:
        st.success("ग्राहक मंच तक्रार मसुदा तयार झाला आहे!")
        st.subheader("📋 मसुदा पाहणी:")
        st.text_area("", st.session_state.draft_cons_text, height=220)
        st.download_button("📥 ग्राहक मंच अर्ज (A4 PDF) डाऊनलोड करा", data=st.session_state.pdf_cons, file_name="Consumer_Complaint.html", mime="text/html")

# ---------------------------------------------------------
# ८. सोशियल मीडिया शेअर - ऑल-इन-वन शेअर बटण (Drop-down Menu)
# ---------------------------------------------------------
st.markdown("---")

app_link = "https://rti-ai-app-eydmnrwsmhvwhmryv7nn4v.streamlit.app/?v=3"
share_text = f"घरबसल्या RTI अर्ज व शासकीय तक्रारीसाठी हे मोफत AI ॲप वापरा: {app_link}"

# शेअरिंग लिंक्स
whatsapp_url = f"https://api.whatsapp.com/send?text={share_text}"
facebook_url = f"https://www.facebook.com/sharer/sharer.php?u={app_link}"
telegram_url = f"https://t.me/share/url?url={app_link}&text=RTI व कायदेशीर सहाय्य AI ॲप"
sms_url = f"sms:?body={share_text}"
messenger_url = f"fb-messenger://share/?link={app_link}"
instagram_url = "https://www.instagram.com/"

# एकाच बटनात सर्व पर्याय दाखवणारा HTML & CSS कोड
single_share_code = f"""
<style>
.share-details {{
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    border: 2px solid #ffd700;
    border-radius: 12px;
    padding: 12px;
    color: white;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}}
.share-summary {{
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    list-style: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #ffd700;
}}
.share-summary::-webkit-details-marker {{
    display: none;
}}
.share-grid {{
    display: grid;
    grid-template-columns: repeat( auto-fit, minmax(130px, 1fr) );
    gap: 8px;
    margin-top: 15px;
    padding-top: 10px;
    border-top: 1px dashed rgba(255,255,255,0.3);
}}
.share-item {{
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
    border-radius: 8px;
    color: white !important;
    font-weight: bold;
    font-size: 13px;
    text-decoration: none !important;
    text-align: center;
}}
</style>

<details class="share-details">
    <summary class="share-summary">
        <span>📢 हे ॲप मित्रांना शेअर करा (सर्व पर्याय)</span>
        <span style="font-size: 18px;">▼</span>
    </summary>
    <div class="share-grid">
        <a href="{whatsapp_url}" target="_blank" class="share-item" style="background-color: #25D366;">💬 WhatsApp</a>
        <a href="{facebook_url}" target="_blank" class="share-item" style="background-color: #1877F2;">📘 Facebook</a>
        <a href="{telegram_url}" target="_blank" class="share-item" style="background-color: #0088cc;">✈️ Telegram</a>
        <a href="{sms_url}" class="share-item" style="background-color: #ff9900;">📱 SMS</a>
        <a href="{messenger_url}" target="_blank" class="share-item" style="background-color: #006AFF;">💬 Messenger</a>
        <a href="{instagram_url}" target="_blank" class="share-item" style="background-color: #E1306C;">📸 Instagram</a>
    </div>
</details>
"""

st.markdown(single_share_code, unsafe_allow_html=True)
