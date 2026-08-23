import streamlit as st

# १. पेज कॉन्फिगरेशन
st.set_page_config(page_title="आकांक्षा RTI AI", layout="wide")

# २. निवडलेला फॉर्म ट्रॅक करणे
query_params = st.query_params
current_form = query_params.get("form", "jodpatra_a")

# ३. A4 साईज PDF/प्रिंट फायली तयार करणारे फंक्शन
def create_a4_pdf_download(title, body_text):
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>{title}</title>
    <style>
        @page {{ size: A4; margin: 20mm; }}
        body {{
            font-family: 'Arial', 'Helvetica', sans-serif;
            font-size: 14pt;
            line-height: 1.6;
            color: #000;
            padding: 10px;
        }}
        .header {{ text-align: center; font-weight: bold; font-size: 18pt; margin-bottom: 20px; border-bottom: 2px solid #000; padding-bottom: 10px; }}
        .footer {{ margin-top: 40px; text-align: right; font-weight: bold; }}
        .content {{ white-space: pre-wrap; font-size: 13pt; text-align: justify; }}
        @media print {{
            .no-print {{ display: none; }}
        }}
        .btn-print {{
            background-color: #27ae60; color: white; padding: 12px 20px; border: none; border-radius: 8px; font-size: 16px; cursor: pointer; margin-bottom: 20px;
        }}
    </style>
    </head>
    <body>
        <button class="btn-print no-print" onclick="window.print()">🖨️ A4 साईज PDF म्हणून सेव्ह / प्रिंट करा</button>
        <div class="header">{title}</div>
        <div class="content">{body_text}</div>
        <div class="footer">
            <br><br>
            अर्जदाराची सही / प्रेषक<br>
            (सतीश अशोक प्रधान)<br>
            मिषारवाडी, छत्रपती संभाजीनगर<br>
            मो. ८६६८२३५३९५
        </div>
    </body>
    </html>
    """
    return html_code

# ४. ३D डिझाईन आणि रंगांसाठी CSS (काहीही बदललेले नाही)
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

# ५. हेडर बॅनर आणि ३D बटणे
full_app_html = """
<div class="header-card">
    <div class="header-title">✨ आकांक्षा इंटरप्राईजेस RTI AI ॲप कायदेशीर सहाय्य ✨</div>
    <div class="header-subtitle">⚡ घरबसल्या RTI अर्ज व शासकीय तक्रार एका सेकंदात A4 साईज मध्ये मोफत मिळवा ⚡</div>
    <div class="header-divider"></div>
    <div class="header-footer">👤 सतीश अशोक प्रधान | 📱 मो. ८६६८२३५३९५</div>
</div>

<div class="btn-container">
    <a href="?form=jodpatra_a" target="_self" class="custom-btn btn-green">📄<br>जोडपत्र 'अ'</a>
    <a href="?form=first_appeal" target="_self" class="custom-btn btn-orange">⚖️<br>प्रथम अपील</a>
    <a href="?form=second_appeal" target="_self" class="custom-btn btn-royal-blue">🏛️<br>माहिती आयोग</a>
    <a href="?form=ai_chat" target="_self" class="custom-btn btn-3d-blue">✨<br>AI चॅट</a>
    <a href="?form=court" target="_self" class="custom-btn btn-purple">📜<br>कोर्ट याचिका</a>
    <a href="?form=complaint" target="_self" class="custom-btn btn-red">📣<br>शासकीय तक्रार</a>
    <a href="?form=rti_portal" target="_self" class="custom-btn btn-gold">🌐<br>आरटीआय ऑनलाइन पोर्टल सहाय्य</a>
    <a href="?form=consumer" target="_self" class="custom-btn btn-cyan">🛒<br>ग्राहक मंच</a>
</div>
"""
st.markdown(full_app_html, unsafe_allow_html=True)

# ---------------------------------------------------------
# ६. बटनानुसार उघडणारे फॉर्म्स व A4 डाऊनलोड (फॉर्मच्या बाहेर)
# ---------------------------------------------------------

# (१) जोडपत्र 'अ'
if current_form == "jodpatra_a":
    st.info("📋 जोडपत्र 'अ' (माहितीचा अधिकार अर्ज - नियम ३) - १ पान A4 मर्यादा")
    with st.form("form_a"):
        karyalay = st.text_input("जन माहिती अधिकाऱ्याच्या कार्यालयाचे नाव व पत्ता")
        name = st.text_input("अर्जदाराचे संपूर्ण नाव", value="सतीश अशोक प्रधान")
        address = st.text_area("अर्जदाराचा पत्ता", value="मिषारवाडी, छत्रपती संभाजीनगर")
        subject = st.text_input("माहितीचा विषय")
        period = st.text_input("माहितीचा कालावधी (उदा. २०२४ ते २०२६)")
        desc = st.text_area("हव्या असलेल्या माहितीचे वर्णन")
        submitted_a = st.form_submit_button("📄 A4 साईज अर्ज तयार करा")
        
        if submitted_a:
            st.session_state.draft_a = f"प्रति,\nराज्य जन माहिती अधिकारी,\n{karyalay}\n\n१. अर्जदाराचे नाव: {name}\n२. पत्ता: {address}\n\n३. हव्या असलेल्या माहितीचा तपशील:\n(एक) विषय: {subject}\n(दोन) कालावधी: {period}\n(तीन) माहितीचे वर्णन: {desc}\n(चार) माहिती टपालाद्वारे नोंदणीकृत टपालाने हवी आहे.\n\n४. अर्जदार दारिद्र्यरेषेखालील नाही.\n\nठिकाण: छत्रपती संभाजीनगर\nदिनांक: २४/०२/२०२६"

    if 'draft_a' in st.session_state:
        st.success("तुमचा जोडपत्र 'अ' अर्ज तयार झाला आहे!")
        st.subheader("📋 मसुदा पाहणी (A4 फॉरमॅट):")
        st.text_area("", st.session_state.draft_a, height=250)
        st.download_button("📥 A4 PDF फाईल डाऊनलोड करा", data=create_a4_pdf_download("माहितीचा अधिकार अर्ज (जोडपत्र अ)", st.session_state.draft_a), file_name="RTI_Application_A4.html", mime="text/html")

# (२) प्रथम अपील
elif current_form == "first_appeal":
    st.info("⚖️ जोडपत्र 'ब' - प्रथम अपील अर्ज (कलम १९(१))")
    with st.form("form_b"):
        officer = st.text_input("प्रथम अपीलीय अधिकाऱ्याचे पदनाम व पत्ता")
        name = st.text_input("अपीलकाराचे नाव", value="सतीश अशोक प्रधान")
        reason = st.text_area("अपील करण्याचे कारण (माहिती दिली नाही/अपूर्ण दिली)")
        submitted_b = st.form_submit_button("⚖️ A4 प्रथम अपील तयार करा")
        
        if submitted_b:
            st.session_state.draft_b = f"प्रति,\nप्रथम अपीलीय अधिकारी,\n{officer}\n\nअपीलकाराचे नाव: {name}\nपत्ता: मिषारवाडी, छत्रपती संभाजीनगर\n\nअपील करण्याचे कारण:\n{reason}\n\nजन माहिती अधिकाऱ्याने मुदतीत योग्य माहिती न दिल्याने सदर प्रथम अपील सादर करत आहे."

    if 'draft_b' in st.session_state:
        st.success("प्रथम अपील मसुदा तयार झाला आहे!")
        st.subheader("📋 मसुदा पाहणी:")
        st.text_area("", st.session_state.draft_b, height=220)
        st.download_button("📥 A4 PDF प्रथम अपील डाऊनलोड करा", data=create_a4_pdf_download("प्रथम अपील अर्ज", st.session_state.draft_b), file_name="First_Appeal_A4.html", mime="text/html")

# (३) माहिती आयोग (द्वितीय अपील)
elif current_form == "second_appeal":
    st.info("🏛️ जोडपत्र 'क' - द्वितिय अपील अर्ज (राज्य माहिती आयोग)")
    with st.form("form_c"):
        commissioner = st.text_input("मा. माहिती आयुक्त व राज्य माहिती आयोग कार्यालय पत्ता")
        reason = st.text_area("दुसरे अपील करण्याचे प्रयोजन")
        submitted_c = st.form_submit_button("🏛️ A4 द्वितीय अपील तयार करा")
        
        if submitted_c:
            st.session_state.draft_c = f"प्रति,\nमा. राज्य माहिती आयुक्त,\n{commissioner}\n\nअपीलकार: सतीश अशोक प्रधान, छत्रपती संभाजीनगर\n\nप्रयोजन:\n{reason}\n\nप्रथम अपीलीय अधिकाऱ्याच्या आदेशानंतरही माहिती मिळालेली नाही, तरी योग्य कारवाई करून माहिती मिळावी."

    if 'draft_c' in st.session_state:
        st.success("द्वितीय अपील मसुदा तयार झाला आहे!")
        st.subheader("📋 मसुदा पाहणी:")
        st.text_area("", st.session_state.draft_c, height=220)
        st.download_button("📥 A4 PDF द्वितीय अपील डाऊनलोड करा", data=create_a4_pdf_download("द्वितीय अपील माहिती आयोग", st.session_state.draft_c), file_name="Second_Appeal_A4.html", mime="text/html")

# (४) कोर्ट याचिका (वकिलांना ड्राफ्ट देण्यासाठी मसुदा)
elif current_form == "court":
    st.info("📜 कोर्ट याचिका / कायदेशीर मसुदा (वकिलांसाठी लीगल ब्रीफ)")
    with st.form("court_form"):
        court_type = st.selectbox("कोर्टाचा प्रकार", ["जिल्हा व सत्र न्यायालय", "उच्च न्यायालय (High Court)", "दीवाणी न्यायालय (Civil Court)", "महसूल न्यायालय (Revenue Court)"])
        petitioner = st.text_input("वादी / अर्जदाराचे नाव", value="सतीश अशोक प्रधान")
        respondent = st.text_input("प्रतिवादी / विरोधी पक्षाचे नाव")
        matter = st.text_area("घटनेचा किंवा वादाचा मुख्य मुद्दा (काय घडले व काय न्याय हवा आहे?)")
        submitted_court = st.form_submit_button("📜 वकिलांसाठी मसुदा तयार करा")
        
        if submitted_court:
            st.session_state.draft_court = f"समक्ष: {court_type}\n\nवादी/अर्जदार: {petitioner}\nविरुद्ध\nप्रतिवादी: {respondent}\n\nविषय: कायदेशीर दाव्याचा/याचिकेचा प्राथमिक मसुदा व तथ्ये.\n\nप्रकरणाची पार्श्वभूमी व मुख्य मुद्दे:\n{matter}\n\nमागणी / प्रार्थना (Relief Claimed):\n१. वरील तथ्यांच्या आधारे वादीस योग्य तो कायदेशीर न्याय व भरपाई देण्यात यावी.\n२. प्रतिवादीस तात्काळ समज पत्र (Notice) जारी करण्यात यावे."

    if 'draft_court' in st.session_state:
        st.success("कोर्ट याचिका मसुदा तयार झाला आहे!")
        st.subheader("📋 मसुदा पाहणी:")
        st.text_area("", st.session_state.draft_court, height=250)
        st.download_button("📥 A4 PDF कोर्ट मसुदा डाऊनलोड करा", data=create_a4_pdf_download("कायदेशीर याचिका मसुदा", st.session_state.draft_court), file_name="Court_Petition_Draft_A4.html", mime="text/html")

# (५) शासकीय तक्रार
elif current_form == "complaint":
    st.info("📣 शासकीय तक्रार निवारण अर्ज (केवळ २-३ शब्दांत अडचण लिहा)")
    with st.form("complaint_form"):
        dept = st.text_input("शासकीय विभाग / कार्यालय", placeholder="उदा. महानगरपालिका / पोलीस स्टेशन / महावितरण")
        short_issue = st.text_input("तक्रारीचा विषय (केवळ २-३ शब्दांत)", placeholder="उदा. रस्त्यावरील खड्डे / लाईटचे बिल")
        details = st.text_area("समस्येची थोडक्यात माहिती")
        submitted_comp = st.form_submit_button("📣 पूर्ण तक्रार अर्ज तयार करा")
        
        if submitted_comp:
            st.session_state.draft_comp = f"प्रति,\nमा. विभाग प्रमुख / अधिकारी,\n{dept}\n\nविषय: {short_issue} बाबत तात्काळ शासकीय तक्रार व कारवाईबाबत.\n\nमहोदय,\n\nमी सतीश अशोक प्रधान, नागरिक राहणारे छत्रपती संभाजीनगर, या पत्राद्वारे आपल्या निदर्शनास आणून देतो की, माझ्या भागात खालीलप्रमाणे गंभीर समस्या निर्माण झाली आहे:\n\nतक्रारीचा तपशील:\n{details}\n\nतरी वरील समस्येचे गांभीर्य लक्षात घेऊन संबंधितांवर तात्काळ योग्य ती कारवाई करावी व मला केलेल्या कारवाईचा अहवाल पाठवावा."

    if 'draft_comp' in st.session_state:
        st.success("शासकीय तक्रार अर्ज तयार झाला आहे!")
        st.subheader("📋 तयार झालेला तक्रार अर्ज:")
        st.text_area("", st.session_state.draft_comp, height=220)
        st.download_button("📥 A4 PDF तक्रार अर्ज डाऊनलोड करा", data=create_a4_pdf_download("शासकीय तक्रार अर्ज", st.session_state.draft_comp), file_name="Govt_Complaint_A4.html", mime="text/html")

# (६) ग्राहक मंच
elif current_form == "consumer":
    st.info("🛒 ग्राहक मंच (Consumer Commission) संपूर्ण मार्गदर्शन व अर्ज मसुदा")
    st.markdown("""
    **📌 प्राथमिक तयारी व कोर्ट अधिकार क्षेत्र (आर्थिक मर्यादेनुसार):**
    * **जिल्हा आयोग (District Commission):** ₹१ कोटी रुपयांपर्यंतचे दावे.
    * **राज्य आयोग (State Commission):** ₹१ कोटी ते ₹१० कोटी रुपयांपर्यंतचे दावे.
    * **राष्ट्रीय आयोग (National Commission):** ₹१० कोटींपेक्षा जास्त रक्कमेचे दावे.
    * **e-Daakhil पोर्टल:** ई-डाखील (`edaakhil.nic.in`) वर ऑनलाईन तक्रार दाखल करता येते.
    """)
    st.markdown("---")
    
    with st.form("consumer_form"):
        st.subheader("📝 ग्राहक मंच तक्रार अर्ज मसुदा")
        company = st.text_input("ज्या कंपनी/दुकानाची तक्रार आहे त्याचे नाव व पत्ता")
        product = st.text_input("खरेदी केलेली वस्तू / घेतलेली सेवा", placeholder="उदा. मोबाईल / फ्रीज / विमा पॉलिसी")
        amount = st.text_input("फसवणुकीची किंवा नुकसानाची रक्कम (₹)")
        complaint_desc = st.text_area("काय फसवणूक किंवा सेवेत त्रुटी झाली?")
        submitted_cons = st.form_submit_button("🛒 ग्राहक मंच तक्रार मसुदा तयार करा")
        
        if submitted_cons:
            st.session_state.draft_cons = f"समक्ष: मा. जिल्हा ग्राहक वाद निवारण आयोग\n\nतक्रारदार: सतीश अशोक प्रधान (मो. ८६६८२३५३९५)\nविरुद्ध\nसामनेवाला (विपक्षी): {company}\n\nतक्रारीचा अर्ज: ग्राहक संरक्षण कायदा २०१९ अन्वये.\n\n१. तक्रारदाराने सामनेवाला यांच्याकडून '{product}' ही वस्तू/सेवा खरेदी केली होती.\n२. नुकसानाची रक्कम: ₹ {amount}/-\n\n३. तक्रारीचे कारण व फसवणूक:\n{complaint_desc}\n\nमागणी:\nतक्रारदारास नुकसान भरपाईपोटी ₹ {amount}/- परत मिळावेत व मानसिक त्रासापोटी योग्य भरपाई मंजूर व्हावी."

    if 'draft_cons' in st.session_state:
        st.success("ग्राहक मंच तक्रार मसुदा तयार झाला आहे!")
        st.subheader("📋 मसुदा पाहणी:")
        st.text_area("", st.session_state.draft_cons, height=220)
        st.download_button("📥 A4 PDF ग्राहक मंच अर्ज डाऊनलोड करा", data=create_a4_pdf_download("ग्राहक मंच तक्रार अर्ज", st.session_state.draft_cons), file_name="Consumer_Complaint_A4.html", mime="text/html")

# (७) आरटीआय ऑनलाईन पोर्टल
elif current_form == "rti_portal":
    st.info("🌐 आरटीआय ऑनलाईन पोर्टल मार्गदर्शन")
    st.write("• **महाराष्ट्र आरटीआय पोर्टल:** १५० शब्दांची मर्यादा.")
    st.write("• **केंद्रीय आरटीआय पोर्टल:** ५०० शब्दांची मर्यादा.")
