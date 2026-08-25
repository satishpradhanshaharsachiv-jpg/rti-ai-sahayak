import streamlit as st
import google.generativeai as genai

# ==========================================
# १. ३D आणि सतत रंग बदलणारे CSS डिझाईन
# ==========================================
st.set_page_config(page_title="RTI AI महा-सहाय्यक", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    /* १. बॅनरसाठी रंग बदलणारे ॲनिमेशन (Animated Gradient) */
    @keyframes bannerGlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* २. बटनांसाठी ॲनिमेटेड ग्रेडियंट्स */
    @keyframes btnGlow1 { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    
    /* मुख्य बॅनर (३D लुक + गोल्डन बॉर्डर + रंग बदलणारा बॅकग्राउंड) */
    .custom-header-banner {
        background: linear-gradient(-45deg, #1e3c72, #2a5298, #0f2027, #203a43, #2c5364);
        background-size: 400% 400%;
        animation: bannerGlow 10s ease infinite;
        border: 2px solid #ffd700;
        border-radius: 20px;
        padding: 20px 15px;
        text-align: center;
        color: white;
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.4), inset 0px 2px 5px rgba(255, 255, 255, 0.3);
        margin-bottom: 25px;
    }
    
    .banner-title {
        font-size: 20px;
        font-weight: 800;
        color: #ffde59;
        text-shadow: 1px 2px 4px rgba(0,0,0,0.8);
        margin-bottom: 8px;
    }
    .banner-subtitle {
        font-size: 13px;
        color: #ff9999;
        font-weight: 600;
        margin-bottom: 12px;
    }
    .banner-footer {
        border-top: 1px dashed rgba(255,255,255,0.3);
        padding-top: 10px;
        font-size: 14px;
        color: #e0e0e0;
        font-weight: 600;
    }

    /* ३D ग्रिड लेआउट */
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        max-width: 500px;
        margin: 0 auto 25px auto;
    }

    /* ३D बटनांचे डिझाईन (3D Shadow + Animated Gradient Colors) */
    .grid-btn-3d {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 18px 10px;
        border-radius: 16px;
        color: white !important;
        font-weight: 700;
        text-decoration: none !important;
        text-align: center;
        font-size: 15px;
        background-size: 300% 300%;
        animation: btnGlow1 6s ease infinite;
        box-shadow: 0px 6px 0px rgba(0,0,0,0.3), 0px 8px 15px rgba(0,0,0,0.3);
        transition: all 0.2s ease;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .grid-btn-3d:active {
        transform: translateY(4px);
        box-shadow: 0px 2px 0px rgba(0,0,0,0.3), 0px 4px 8px rgba(0,0,0,0.3);
    }

    /* प्रत्येक बटनाचा स्वतंत्र रंग बदलणारा (Changing Color) शेड */
    .btn-col-1 { background-image: linear-gradient(135deg, #11998e, #38ef7d, #00b09b, #96c93d); }
    .btn-col-2 { background-image: linear-gradient(135deg, #ff416c, #ff4b2b, #ff0844, #ffb199); }
    .btn-col-3 { background-image: linear-gradient(135deg, #1f4037, #99f2c8, #005c97, #363795); }
    .btn-col-4 { background-image: linear-gradient(135deg, #00c6ff, #0072ff, #00d2ff, #3a7bd5); }
    .btn-col-5 { background-image: linear-gradient(135deg, #8e2de2, #4a00e0, #654ea3, #eaafc8); }
    .btn-col-6 { background-image: linear-gradient(135deg, #d31027, #ea384d, #e52d27, #b31217); }
    .btn-col-7 { background-image: linear-gradient(135deg, #f857a6, #ff5858, #f7b733, #fc4a1a); color: #000 !important; }
    .btn-col-8 { background-image: linear-gradient(135deg, #00b4db, #0083b0, #136a8a, #267871); }

    .btn-icon {
        font-size: 22px;
        margin-bottom: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# २. API KEY कॉन्फिगरेशन
# ==========================================
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", "")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    st.warning("⚠️ कृपया Streamlit Secrets मध्ये GEMINI_API_KEY जोडा.")

UNIVERSAL_SYSTEM_PROMPT = """
तुम्ही 'आकांक्षा AI असिस्टंट' आहात - एक बुद्धिमत्तापूर्ण, सर्वसमावेशक आणि बहुगुणी AI सहाय्यक.
तुमचे काम विचारलेल्या प्रश्नाला सोप्या, अचूक आणि उपयुक्त मराठी भाषेत उत्तरे देणे आहे.
"""

query_params = st.query_params
current_form = query_params.get("form", "jodpatra_a")

# ==========================================
# ३. ३D ॲनिमेटेड बॅनर
# ==========================================
banner_html = """
<div class="custom-header-banner">
    <div class="banner-title">✨ आकांक्षा इंटरप्राईजेस RTI AI ॲप कायदेशीर सहाय्य ✨</div>
    <div class="banner-subtitle">⚡ घरबसल्या RTI अर्ज व शासकीय तक्रार एका सेकंदात A4 साईज मध्ये मोफत मिळवा ⚡</div>
    <div class="banner-footer">
        👤 सतीश अशोक प्रधान | 📱 मो. ८६६८२३५३९५
    </div>
</div>
"""
st.markdown(banner_html, unsafe_allow_html=True)

# ==========================================
# ४. ३D ॲनिमेटेड ग्रिड बटने
# ==========================================
grid_buttons_html = """
<div class="grid-container">
    <a href="?form=jodpatra_a#form-section" target="_self" class="grid-btn-3d btn-col-1">
        <span class="btn-icon">📄</span> जोडपत्र 'अ'
    </a>
    <a href="?form=first_appeal#form-section" target="_self" class="grid-btn-3d btn-col-2">
        <span class="btn-icon">⚖️</span> प्रथम अपील
    </a>
    <a href="?form=second_appeal#form-section" target="_self" class="grid-btn-3d btn-col-3">
        <span class="btn-icon">🏛️</span> माहिती आयोग
    </a>
    <a href="?form=ai_chat#form-section" target="_self" class="grid-btn-3d btn-col-4">
        <span class="btn-icon">✨</span> AI चॅट
    </a>
    <a href="?form=court#form-section" target="_self" class="grid-btn-3d btn-col-5">
        <span class="btn-icon">📜</span> कोर्ट याचिका
    </a>
    <a href="?form=complaint#form-section" target="_self" class="grid-btn-3d btn-col-6">
        <span class="btn-icon">📢</span> शासकीय तक्रार
    </a>
    <a href="?form=rti_portal#form-section" target="_self" class="grid-btn-3d btn-col-7">
        <span class="btn-icon">🌐</span> आरटीआय ऑनलाईन पोर्टल सहाय्य
    </a>
    <a href="?form=consumer#form-section" target="_self" class="grid-btn-3d btn-col-8">
        <span class="btn-icon">🛒</span> ग्राहक मंच
    </a>
</div>
"""
st.markdown(grid_buttons_html, unsafe_allow_html=True)
st.markdown('<div id="form-section"></div>', unsafe_allow_html=True)

# ==========================================
# ५. कायदेशीर फॉर्म्स
# ==========================================

if current_form == "jodpatra_a":
    st.info("📋 जोडपत्र 'अ' - माहितीचा अधिकार अधिनियम, २००५ अन्वये अर्ज (नियम ३)")
    with st.form("form_a"):
        karyalay = st.text_input("जन माहिती अधिकाऱ्याच्या कार्यालयाचे नाव व पत्ता")
        name = st.text_input("अर्जदाराचे संपूर्ण नाव", placeholder="तुमचे पूर्ण नाव")
        address = st.text_area("अर्जदाराचा पूर्ण पत्राव्यवहाराचा पत्ता")
        mobile = st.text_input("मोबाईल क्रमांक")
        subject = st.text_input("माहितीचा विषय")
        period = st.text_input("माहितीचा कालावधी", placeholder="उदा. २०२४ ते २०२५")
        desc = st.text_area("हव्या असलेल्या माहितीचे वर्णन (सविस्तर मुद्दे)")
        post_type = st.selectbox("माहिती कशी हवी आहे?", ["टपालाद्वारे (साधे/नोंदणीकृत)", "व्यक्तीश: (रूबरू)"])
        submitted_a = st.form_submit_button("📄 जोडपत्र 'अ' तयार करा")

        if submitted_a:
            draft = f"प्रति,\nजन माहिती अधिकारी,\n{karyalay}\n\nअर्जदार: {name}\nपत्ता: {address}\nमोबाईल: {mobile}\n\nविषय: {subject}\nकालावधी: {period}\n\nमाहितीचा तपशील:\n{desc}\n\nमाहिती मिळण्याचा प्रकार: {post_type}"
            st.session_state.draft_a_text = draft

    if "draft_a_text" in st.session_state:
        st.success("अर्जाचा मसुदा तयार झाला आहे!")
        st.text_area("मसुदा पाहणी:", st.session_state.draft_a_text, height=200)

elif current_form == "first_appeal":
    st.info("⚖️ जोडपत्र 'ब' - प्रथम अपील अर्ज (कलम १९ (१) - नियम ५(१))")
    with st.form("form_b"):
        officer = st.text_input("प्रथम अपीलीय अधिकाऱ्याचे पदनाम व पत्ता")
        name = st.text_input("अपीलकर्त्याचे संपूर्ण नाव")
        address = st.text_area("पत्राव्यवहाराचा पत्ता")
        reason = st.text_area("अपील करण्याचे कारण / प्रयोजन")
        submitted_b = st.form_submit_button("⚖️ प्रथम अपील मसुदा तयार करा")

        if submitted_b:
            draft = f"प्रति,\nप्रथम अपीलीय अधिकारी,\n{officer}\n\nअपीलकर्ता: {name}\nपत्ता: {address}\n\nअपील करण्याचे कारण: {reason}"
            st.session_state.draft_b_text = draft

    if "draft_b_text" in st.session_state:
        st.success("प्रथम अपील मसुदा तयार झाला आहे!")
        st.text_area("मसुदा पाहणी:", st.session_state.draft_b_text, height=200)

elif current_form == "second_appeal":
    st.info("🏛️ जोडपत्र 'क' - द्वितीय अपील अर्ज (कलम १९ (३) - नियम ५(२))")
    with st.form("form_c"):
        commissioner = st.text_input("मा. माहिती आयुक्त व राज्य माहिती आयोग कार्यालय पत्ता")
        name = st.text_input("अपीलकर्त्याचे संपूर्ण नाव")
        reason = st.text_area("दुसरे अपील करण्याचे प्रयोजन")
        submitted_c = st.form_submit_button("🏛️ द्वितीय अपील मसुदा तयार करा")

        if submitted_c:
            draft = f"प्रति,\nमा. राज्य माहिती आयुक्त,\n{commissioner}\n\nअपीलकर्ता: {name}\n\nप्रयोजन: {reason}"
            st.session_state.draft_c_text = draft

    if "draft_c_text" in st.session_state:
        st.success("द्वितीय अपील मसुदा तयार झाला आहे!")
        st.text_area("मसुदा पाहणी:", st.session_state.draft_c_text, height=200)

elif current_form == "ai_chat":
    st.info("✨ आकांक्षा AI चॅट असिस्टंट - सर्व प्रकारची कायदेशीर व बहुगुणी मदत घ्या.")

elif current_form == "court":
    st.info("📜 कोर्ट याचिका / लीगल ब्रीफ मसुदा")
    with st.form("court_form"):
        court_type = st.selectbox("कोर्टाचा प्रकार", ["जिल्हा व सत्र न्यायालय", "उच्च न्यायालय (High Court)", "दिवाणी न्यायालय"])
        petitioner = st.text_input("वादी / अर्जदाराचे नाव")
        respondent = st.text_input("प्रतिवादी / विरोधी पक्षाचे नाव")
        matter = st.text_area("घटनेचा किंवा वादाचा मुख्य मुद्दा")
        submitted_court = st.form_submit_button("📜 याचिका मसुदा तयार करा")

        if submitted_court:
            draft = f"समक्ष: {court_type}\n\nवादी: {petitioner}\nविरुद्ध\nप्रतिवादी: {respondent}\n\nविषय/घटना:\n{matter}"
            st.session_state.draft_court_text = draft

    if "draft_court_text" in st.session_state:
        st.success("याचिका मसुदा तयार झाला आहे!")
        st.text_area("मसुदा पाहणी:", st.session_state.draft_court_text, height=200)

elif current_form == "complaint":
    st.info("📢 शासकीय तक्रार निवारण अर्ज")
    with st.form("complaint_form"):
        dept = st.text_input("शासकीय विभाग / कार्यालय")
        name = st.text_input("तक्रारदाराचे नाव")
        short_issue = st.text_area("तक्रारीचा सविस्तर विषय")
        submitted_comp = st.form_submit_button("📢 तक्रार अर्ज तयार करा")

        if submitted_comp:
            draft = f"प्रति,\nमा. विभाग प्रमुख / अधिकारी,\n{dept}\n\nतक्रारदार: {name}\n\nविषय: {short_issue}"
            st.session_state.draft_comp_text = draft

    if "draft_comp_text" in st.session_state:
        st.success("तक्रार अर्ज तयार झाला आहे!")
        st.text_area("मसुदा पाहणी:", st.session_state.draft_comp_text, height=200)

elif current_form == "rti_portal":
    st.info("🌐 आरटीआय ऑनलाईन पोर्टल मार्गदर्शन")
    st.write("* **महाराष्ट्र आरटीआय पोर्टल:** १५० शब्दांची मर्यादा व १० रु. शुल्क.")
    st.write("* **केंद्रीय आरटीआय पोर्टल:** ५०० शब्दांची मर्यादा व १० रु. शुल्क.")

elif current_form == "consumer":
    st.info("🛒 ग्राहक मंच (Consumer Commission) संपूर्ण मार्गदर्शन व अर्ज मसुदा")
    with st.form("consumer_form"):
        name = st.text_input("तक्रारदाराचे नाव")
        company = st.text_input("सामनेवाला (ज्या कंपनी/दुकानावर तक्रार आहे)")
        complaint_desc = st.text_area("काय फसवणूक किंवा सेवेत त्रुटी झाली?")
        submitted_cons = st.form_submit_button("🛒 ग्राहक मंच मसुदा तयार करा")

        if submitted_cons:
            draft = f"प्रति,\nमा. अध्यक्ष, जिल्हा ग्राहक वाद निवारण आयोग\n\nतक्रारदार: {name}\nविरुद्ध\nसामनेवाला: {company}\n\nतक्रारीचे कारण: {complaint_desc}"
            st.session_state.draft_cons_text = draft

    if "draft_cons_text" in st.session_state:
        st.success("ग्राहक मंच तक्रार मसुदा तयार झाला आहे!")
        st.text_area("मसुदा पाहणी:", st.session_state.draft_cons_text, height=200)

# ==========================================
# ६. सोशली शेअर पर्याय
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
# ७. AI चॅट लॉजिक (ऑटो-मॉडेल स्वॅपिंग)
# ==========================================
st.subheader("💬 AI कायदेशीर मदत व चॅट बॉक्स")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("AI ला कायदेशीर प्रश्न विचारा..."):
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("AI विचार करत आहे व उत्तर तयार करत आहे..."):
            auto_models = [
                "gemini-3.6-flash",
                "gemini-3.5-flash-lite",
                "gemini-3.1-pro",
                "gemini-2.5-flash",
                "gemini-1.5-flash"
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
                st.error(f"❌ API एरर: {last_error}")
