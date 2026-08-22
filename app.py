import streamlit as st
import datetime

# ==============================================================================
# आकांक्षा AI - RTI व कायदेशीर महा-सहाय्यक (मोबाईल ऑप्टिमाइझ्ड व्हर्जन)
# विकासक: सतीश अशोक प्रधान (छत्रपती संभाजीनगर) | मोबाईल: ८६६८२३५३९५
# ==============================================================================

st.set_page_config(
    page_title="RTI & Legal Assistant - Satish Pradhan",
    page_icon="📜",
    layout="centered"  # मोबाईलसाठी सेंटर व कॉम्पॅक्ट लेआउट
)

# मोबाईल फ्रेंडली आणि चमचमीत CSS स्टाईलिंग (समान आकाराची आकर्षक बटने)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .header-box {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        margin-bottom: 15px;
    }
    .header-box h1 {
        font-size: 24px;
        margin-bottom: 5px;
        font-weight: bold;
        color: #FFD700;
    }
    .header-box p {
        font-size: 14px;
        margin: 0;
        color: #E2E8F0;
    }
    /* सर्व बटने एकाच आकाराची व चमचमीत */
    .stButton>button {
        width: 100%;
        height: 50px;
        font-size: 15px;
        font-weight: bold;
        color: white;
        background: linear-gradient(45deg, #FF416C, #FF4B2B);
        border: none;
        border-radius: 10px;
        box-shadow: 0 3px 8px rgba(255, 75, 43, 0.4);
        transition: 0.2s ease;
        margin-bottom: 8px;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #FF4B2B, #FF416C);
        box-shadow: 0 5px 12px rgba(255, 75, 43, 0.6);
        transform: translateY(-1px);
    }
    .a4-container {
        background-color: #ffffff;
        border: 2px dashed #1e3c72;
        padding: 20px;
        border-radius: 10px;
        font-family: 'Arial', sans-serif;
        color: #111827;
        font-size: 14px;
        line-height: 1.6;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# हेडर प्रदर्शन
st.markdown("""
    <div class="header-box">
        <h1>✨ आकांक्षा AI - RTI महा-सहाय्यक ✨</h1>
        <p>👤 सतीश अशोक प्रधान | 📱 ८६६८२३५३९५</p>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# कायमस्वरूपी लॉगिन सिस्टीम (एकदा लॉगिन केल्यावर पुन्हा OTP मागणार नाही)
# ==============================================================================
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if not st.session_state.is_logged_in:
    st.markdown("<h3 style='text-align: center; color: #1e3c72;'>🔐 मोबाईल लॉगिन</h3>", unsafe_allow_html=True)
    mobile_input = st.text_input("१० अंकी मोबाईल नंबर टाка:", placeholder="8668235395", max_chars=10)
    
    if st.button("🚀 ॲपमध्ये प्रवेश करा (सतत लॉगिन राहिल)"):
        if len(mobile_input) == 10 and mobile_input.isdigit():
            st.session_state.is_logged_in = True
            st.session_state.user_mobile = mobile_input
            st.success("लॉगिन यशस्वी! ॲप सुरू होत आहे...")
            st.rerun()
        else:
            st.error("कृपया अचूक १० अंकी मोबाईल नंबर प्रविष्ट करा.")
else:
    # युजर लॉग इन झाल्यानंतर डॅशबोर्ड व कायमस्वरूपी युजर ओळख
    st.sidebar.markdown(f"### 👤 युजर: सतीश प्रधान")
    st.sidebar.markdown(f"📱 **+91 {st.session_state.get('user_mobile', '8668235395')}**")
    if st.sidebar.button("🔒 लॉग आउट"):
        st.session_state.is_logged_in = False
        st.rerun()

    if "active_module" not in st.session_state:
        st.session_state.active_module = "rti"

    st.markdown("### 🎛️ कायदेशीर सेवा निवडा:")

    # ९ बटने मोबाईलसाठी योग्य अशा ग्रिडमध्ये (समान आकार)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📄 जोडपत्र 'अ'"): st.session_state.active_module = "rti"
        if st.button("⚖️ प्रथम अपील"): st.session_state.active_module = "first_appeal"
        if st.button("🏛️ माहिती आयोग"): st.session_state.active_module = "commission"
    with col2:
        if st.button("⚖️ कोर्ट याचिका"): st.session_state.active_module = "court"
        if st.button("📣 शासकीय तक्रार"): st.session_state.active_module = "complaint"
        if st.button("✏️ प्रतिज्ञापत्र"): st.session_state.active_module = "affidavit"
    with col3:
        if st.button("🛒 ग्राहक मंच"): st.session_state.active_module = "consumer"
        if st.button("✨ आकांक्षा AI"): st.session_state.active_module = "ai_chat"
        if st.button("🌐 RTI ऑनलाईन"): st.session_state.active_module = "online_rti"

    st.write("---")

    # ==============================================================================
    # ९ मॉड्यूल्सची अंमलबजावणी
    # ==============================================================================

    # १. जोडपत्र 'अ'
    if st.session_state.active_module == "rti":
        st.subheader("📄 जोडपत्र 'अ' - माहिती अधिकार अर्ज")
        dept = st.text_input("जन माहिती अधिकारी, विभाग व पत्ता:")
        subject = st.text_input("माहितीचा विषय:")
        details = st.text_area("हवी असलेली माहितीचे मुद्दे (१ ते ५):")
        bpl = st.radio("BPL (दारिद्र्यरेषेखालील) आहात का?", ["नाही", "होय"])
        
        if st.button("अर्ज तयार करा"):
            bpl_text = "मी BPL नागरिक असल्याने शुल्क माफ आहे." if bpl == "होय" else "₹१० चा पोष्टल ऑर्डर जोडला आहे."
            draft = f"""
**माहिती अधिकाराचा अर्ज (जोडपत्र 'अ')**
प्रति, जन माहिती अधिकारी, {dept}
विषय: {subject}
१. माहितीचा तपशील: {details}
२. कायदेशीर अट: कलम ६(३) नुसार अर्ज वर्ग करावा. {bpl_text}

**अर्जदार:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर | मो. ८६६८२३५३९५ | दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # २. प्रथम अपील
    elif st.session_state.active_module == "first_appeal":
        st.subheader("⚖️ प्रथम अपील (कलम १९ मानकानुसार)")
        fa_dept = st.text_input("प्रथम अपिलीय अधिकारी व पत्ता:")
        pious_date = st.text_input("मूळ अर्ज केल्याची तारीख:")
        reason = st.text_area("अपिलाचे कारण:")
        if st.button("प्रथम अपील तयार करा"):
            draft = f"""
**प्रथम अपील अर्ज (कलम १९(१))**
प्रति, अपिलीय अधिकारी, {fa_dept}
विषय: दिनांक {pious_date} रोजीच्या अर्जानुसार माहिती न मिळाल्याबाबत.
कारण: {reason}

**अपीलार्थी:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर | दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # ३. माहिती आयोग
    elif st.session_state.active_module == "commission":
        st.subheader("🏛️ राज्य माहिती आयोग (द्वितीय अपील)")
        bench = st.text_input("माहिती आयोग खंडपीठ (उदा. औरंगाबाद):")
        comm_details = st.text_area("घटनाक्रम व तक्रार तपशील:")
        if st.button("माहिती आयोग अर्ज तयार करा"):
            draft = f"""
**द्वितीय अपील अर्ज - राज्य माहिती आयोग ({bench})**
विषय: प्रथम अपिलीय आदेशानंतरही माहिती न मिळाल्याबाबत.
तपशील: {comm_details}

**अर्जदार:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर | दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # ४. कोर्ट याचिका
    elif st.session_state.active_module == "court":
        st.subheader("⚖️ न्यायालयीन याचिका मसुदा")
        court_name = st.text_input("न्यायालयाचे नाव:")
        opponent = st.text_input("सामनेवाला नाव व पत्ता:")
        facts = st.text_area("प्रकरणाची हकीकत:")
        prayer = st.text_input("न्यायालयाकडे मागितलेला न्याय:")
        if st.button("कोर्ट याचिका तयार करा"):
            draft = f"""
**न्यायालयीन याचिका - मा. {court_name}**
याचिकाकर्ता: सतीश अशोक प्रधान विरुद्ध सामनेवाला: {opponent}
विषय: {prayer}
हकीकत: {facts}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # ५. शासकीय तक्रार
    elif st.session_state.active_module == "complaint":
        st.subheader("📣 शासकीय अधिकारी तक्रार अर्ज")
        target_officer = st.text_input("वरिष्ठ अधिकारी पद व कार्यालय:")
        comp_subject = st.text_input("तक्रारीचा विषय:")
        comp_details = st.text_area("घटनेचा तपशील:")
        if st.button("शासकीय तक्रार तयार करा"):
            draft = f"""
**शासकीय तक्रार अर्ज**
प्रति, {target_officer}
विषय: {comp_subject}
तपशील: {comp_details}
तक्रारदार: सतीश अशोक प्रधान, छत्रपती संभाजीनगर | मो. ८६६८२३५३९५
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # ६. प्रतिज्ञापत्र
    elif st.session_state.active_module == "affidavit":
        st.subheader("✏️ कायदेशीर प्रतिज्ञापत्र")
        aff_reason = st.text_input("प्रतिज्ञापत्राचे कारण:")
        aff_statements = st.text_area("शपथपूर्वक घोषित करावयाचे मुद्दे:")
        if st.button("प्रतिज्ञापत्र तयार करा"):
            draft = f"""
**कायदेशीर प्रतिज्ञापत्र (Affidavit)**
मी सतीश अशोक प्रधान, रा. छत्रपती संभाजीनगर, घोषित करतो की:
कारण: {aff_reason}
मु मुद्दे: {aff_statements}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # ७. ग्राहक मंच
    elif st.session_state.active_module == "consumer":
        st.subheader("🛒 ग्राहक मंच तक्रार अर्ज")
        forum = st.text_input("ग्राहक मंचाचे नाव:")
        seller = st.text_input("व्यापारी/कंपनी नाव:")
        loss_details = st.text_area("फसवणूक/त्रुटीचा तपशील:")
        compensation = st.text_input("मागितलेली भरपाई रक्कम (₹):")
        if st.button("ग्राहक मंच अर्ज तयार करा"):
            draft = f"""
**ग्राहक मंचाकडे तक्रार - {forum}**
तक्रारदार: सतीश अशोक प्रधान विरुद्ध सामनेवाला: {seller}
तपशील: {loss_details} | मागितलेली भरपाई: ₹{compensation}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # ८. AI चॅट
    elif st.session_state.active_module == "ai_chat":
        st.subheader("✨ आकांक्षा AI सल्लागार")
        query = st.text_input("तुमचा कायदेशीर प्रश्न विचारा:")
        if st.button("उत्तर मिळवा"):
            if query:
                st.success(f"🤖 उत्तर: तुमच्या प्रश्न '{query}' नुसार योग्य तो कायदेशीर मार्ग अवलंबणे गरजेचे आहे. वरील योग्य मसुदा निवडून अर्ज दाखल करा.")
            else:
                st.warning("कृपया प्रश्न टाईप करा.")

    # ९. RTI ऑनलाईन (१५० शब्द मर्यादा)
    elif st.session_state.active_module == "online_rti":
        st.subheader("🌐 RTI ऑनलाईन पोर्टल (१५० शब्द क्लिनर)")
        raw_text = st.text_area("मोठा RTI मजकूर इथे पेस्ट करा:")
        if st.button("१५० शब्दांत स्वच्छ करा"):
            clean_text = raw_text.replace("*", "").replace("#", "").replace("'", "")
            words = clean_text.split()
            if len(words) > 150:
                clean_text = " ".join(words[:150]) + "..."
            st.text_area("स्वच्छ मजकूर (कॉपी करण्यासाठी):", value=clean_text, height=150)
import streamlit as st
import datetime

# ==============================================================================
# आकांक्षा AI - RTI व कायदेशीर महा-सहाय्यक (स्क्रीनशॉटमधील डिझाइननुसार परिपूर्ण कोड)
# विकासक: सतीश अशोक प्रधान (छत्रपती संभाजीनगर) | मोबाईल: ८६६८२३५३९५
# ==============================================================================

st.set_page_config(
    page_title="RTI & Legal Assistant - Satish Pradhan",
    page_icon="⚖️",
    layout="centered"
)

# स्क्रीनशॉटमधील डिझाइनसारखे चमचमीत कार्ड्स व बटने यासाठी CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .header-box {
        background: #ffffff;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 15px;
    }
    .header-box h1 {
        font-size: 22px;
        font-weight: bold;
        color: #00A86B;
        margin-bottom: 5px;
    }
    .tag-box {
        background: linear-gradient(90deg, #fff3e0, #ffe0b2);
        padding: 8px 15px;
        border-radius: 20px;
        display: inline-block;
        font-size: 14px;
        font-weight: bold;
        color: #e65100;
        border: 1px dashed #ffa726;
        margin-bottom: 15px;
    }
    /* सुंदर कार्ड डिझाइनसाठी स्टाईल */
    .card-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 15px;
        border-radius: 15px;
        color: white;
        text-align: center;
        cursor: pointer;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        margin-bottom: 10px;
        height: 110px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        transition: 0.2s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.2);
    }
    .a4-container {
        background-color: #ffffff;
        border: 2px dashed #1e3c72;
        padding: 20px;
        border-radius: 12px;
        font-family: 'Arial', sans-serif;
        color: #111827;
        font-size: 14px;
        line-height: 1.7;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# हेडर प्रदर्शन
st.markdown("""
    <div class="header-box">
        <h1>⚖️ RTI AI महा-सहाय्यक</h1>
        <div class="tag-box">⚡ घरसल्या एका मिनिटात अर्ज तयार करा</div>
        <p style="font-size: 13px; color: #555; margin:0;">👤 सतीश अशोक प्रधान | 📱 ८६६८२३५३९५ | छत्रपती संभाजीनगर</p>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# कायमस्वरूपी लॉगिन सिस्टीम (एकदा नंबर टाकला की पुन्हा कधीही OTP किंवा लॉगिन मागणार नाही)
# ==============================================================================
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if not st.session_state.is_logged_in:
    st.markdown("<h3 style='text-align: center; color: #1e3c72;'>🔐 सुरक्षित मोबाईल प्रवेश</h3>", unsafe_allow_html=True)
    col_l1, col_l2, col_l3 = st.columns([1, 3, 1])
    with col_l2:
        mobile_input = st.text_input("तुमचा १० अंकी मोबाईल नंबर टाका:", placeholder="8668235395", max_chars=10)
        
        if st.button("🚀 ॲप सुरू करा (कायमस्वरूपी लॉगिन राहील)"):
            if len(mobile_input) == 10 and mobile_input.isdigit():
                st.session_state.is_logged_in = True
                st.session_state.user_mobile = mobile_input
                st.success("सफलता! ॲप सुरू होत आहे...")
                st.rerun()
            else:
                st.error("कृपया अचूक १० अंकी मोबाईल नंबर प्रविष्ट करा.")
else:
    # साईडबारमध्ये युजर माहिती व लॉग आऊट पर्याय
    st.sidebar.markdown(f"### 👤 युजर: सतीश प्रधान")
    st.sidebar.markdown(f"📱 **+91 {st.session_state.get('user_mobile', '8668235395')}**")
    if st.sidebar.button("🔒 लॉग आऊट"):
        st.session_state.is_logged_in = False
        st.rerun()

    if "active_module" not in st.session_state:
        st.session_state.active_module = "rti"

    st.markdown("### 🎛️ सेवा निवडा:")

    # स्क्रीनशॉटसारखी ४x२ ग्रिड रचना आणि चमचमीत रंगीबेरंगी बटने
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📄\n\nजोडपत्र 'अ'"): st.session_state.active_module = "rti"
    with col2:
        if st.button("⚖️\n\nप्रथम अपील"): st.session_state.active_module = "first_appeal"
    with col3:
        if st.button("🏛️\n\nमाहिती आयोग"): st.session_state.active_module = "commission"
    with col4:
        if st.button("✨\n\nAI चॅट"): st.session_state.active_module = "ai_chat"

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        if st.button("📜\n\nकोर्ट याचिका"): st.session_state.active_module = "court"
    with col6:
        if st.button("📣\n\nशासकीय तक्रार"): st.session_state.active_module = "complaint"
    with col7:
        if st.button("✏️\n\nप्रतिज्ञापत्र"): st.session_state.active_module = "affidavit"
    with col8:
        if st.button("🛒\n\nग्राहक मंच"): st.session_state.active_module = "consumer"

    st.write("---")

    # ==============================================================================
    # सर्व मॉड्यूल्सची मसुदा निर्मिती
    # ==============================================================================

    if st.session_state.active_module == "rti":
        st.subheader("📄 जोडपत्र 'अ' - माहिती अधिकार अर्ज (कलम ६ तर्फे)")
        dept = st.text_input("जन माहिती अधिकारी, विभाग व पत्ता:")
        subject = st.text_input("माहितीचा विषय:")
        details = st.text_area("हवी असलेली माहितीचा तपशील (मुद्देनिहाय):")
        bpl = st.radio("दारिद्र्यरेषेखालील (BPL) आहात का?", ["नाही", "होय"])
        
        if st.button("तयार करा: जोडपत्र 'अ' मसुदा"):
            bpl_text = "मी BPL नागरिक असल्याने शुल्क माफ आहे." if bpl == "होय" else "₹१० चा पोष्टल ऑर्डर/कोर्ट फी जोडली आहे."
            draft = f"""
**माहिती अधिकाराचा अर्ज (जोडपत्र 'अ')**
प्रति, जन माहिती अधिकारी, {dept}
विषय: {subject}
१. माहितीचा तपशील: {details}
२. कायदेशीर अट: कलम ६(३) नुसार अर्ज वर्ग करावा. {bpl_text}

**अर्जदार:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर | मो. ८६६८२३५३९५ | दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    elif st.session_state.active_module == "first_appeal":
        st.subheader("⚖️ प्रथम अपील अर्ज (कलम १९ मानकानुसार)")
        fa_dept = st.text_input("प्रथम अपिलीय अधिकारी व पत्ता:")
        pious_date = st.text_input("मूळ अर्ज केल्याची तारीख:")
        reason = st.text_area("अपिलाचे कारण:")
        if st.button("प्रथम अपील तयार करा"):
            draft = f"""
**प्रथम अपील अर्ज (कलम १९(१))**
प्रति, अपिलीय अधिकारी, {fa_dept}
विषय: दिनांक {pious_date} रोजीच्या अर्जानुसार माहिती न मिळाल्याबाबत.
कारण: {reason}

**अपीलार्थी:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर | दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    elif st.session_state.active_module == "commission":
        st.subheader("🏛️ राज्य माहिती आयोग (द्वितीय अपील)")
        bench = st.text_input("माहिती आयोग खंडपीठ (उदा. औरंगाबाद):")
        comm_details = st.text_area("घटनाक्रम व तक्रार तपशील:")
        if st.button("माहिती आयोग अर्ज तयार करा"):
            draft = f"""
**द्वितीय अपील अर्ज - राज्य माहिती आयोग ({bench})**
विषय: प्रथम अपिलीय आदेशानंतरही माहिती न मिळाल्याबाबत.
तपशील: {comm_details}

**अर्जदार:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर | दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    elif st.session_state.active_module == "ai_chat":
        st.subheader("✨ आकांक्षा AI कायदेशीर सल्लागार")
        query = st.text_input("तुमचा कायदेशीर प्रश्न इथे विचारा:")
        if st.button("उत्तर मिळवा"):
            if query:
                st.success(f"🤖 AI उत्तर: तुमच्या प्रश्न '{query}' नुसार योग्य तो कायदेशीर मार्ग अवलंबणे गरजेचे आहे. अचूक माहितीसाठी योग्य मसुदा निवडा.")
            else:
                st.warning("कृपया प्रश्न टाईप करा.")

    elif st.session_state.active_module == "court":
        st.subheader("⚖️ न्यायालयीन याचिका मसुदा")
        court_name = st.text_input("न्यायालयाचे नाव:")
        opponent = st.text_input("सामनेवाला नाव व पत्ता:")
        facts = st.text_area("प्रकरणाची हकीकत:")
        prayer = st.text_input("न्यायालयाकडे मागितलेला न्याय:")
        if st.button("कोर्ट याचिका तयार करा"):
            draft = f"""
**न्यायालयीन याचिका - मा. {court_name}**
याचिकाकर्ता: सतीश अशोक प्रधान विरुद्ध सामनेवाला: {opponent}
विषय: {prayer}
हकीकत: {facts}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    elif st.session_state.active_module == "complaint":
        st.subheader("📣 शासकीय अधिकारी तक्रार अर्ज")
        target_officer = st.text_input("वरिष्ठ अधिकारी पद व कार्यालय:")
        comp_subject = st.text_input("तक्रारीचा विषय:")
        comp_details = st.text_area("घटनेचा तपशील:")
        if st.button("शासकीय तक्रार तयार करा"):
            draft = f"""
**शासकीय तक्रार अर्ज**
प्रति, {target_officer}
विषय: {comp_subject}
तपशील: {comp_details}
तक्रारदार: सतीश अशोक प्रधान, छत्रपती संभाजीनगर | मो. ८६६८२३५३९५
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    elif st.session_state.active_module == "affidavit":
        st.subheader("✏️ कायदेशीर प्रतिज्ञापत्र")
        aff_reason = st.text_input("प्रतिज्ञापत्राचे कारण:")
        aff_statements = st.text_area("शपथपूर्वक घोषित करावयाचे मुद्दे:")
        if st.button("प्रतिज्ञापत्र तयार करा"):
            draft = f"""
**कायदेशीर प्रतिज्ञापत्र (Affidavit)**
मी सतीश अशोक प्रधान, रा. छत्रपती संभाजीनगर, घोषित करतो की:
कारण: {aff_reason}
मुद्दे: {aff_statements}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    elif st.session_state.active_module == "consumer":
        st.subheader("🛒 ग्राहक मंच तक्रार अर्ज")
        forum = st.text_input("ग्राहक मंचाचे नाव:")
        seller = st.text_input("व्यापारी/कंपनी नाव:")
        loss_details = st.text_area("फसवणूक/त्रुटीचा तपशील:")
        compensation = st.text_input("मागितलेली भरपाई रक्कम (₹):")
        if st.button("ग्राहक मंच अर्ज तयार करा"):
            draft = f"""
**ग्राहक मंचाकडे तक्रार - {forum}**
तक्रारदार: सतीश अशोक प्रधान विरुद्ध सामनेवाला: {seller}
तपशील: {loss_details} | मागितलेली भरपाई: ₹{compensation}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)
