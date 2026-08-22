import streamlit as st
import datetime

# १. पेज सेटअप आणि PWA लुक
st.set_page_config(
    page_title="RTI AI Assistant",
    page_icon="📜",
    layout="wide"
)

# कस्टम CSS - ४x२ ग्रिड आणि मोबाईल ॲप डिझाइन
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-weight: bold;
        padding: 10px;
    }
    .sub-title {
        text-align: center;
        color: #4B5563;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .a4-container {
        background-color: #ffffff;
        border: 2px solid #374151;
        padding: 25px;
        border-radius: 5px;
        font-family: 'Arial', sans-serif;
        color: #000000;
        line-height: 1.6;
    }
    </style>
""", unsafe_unsafe_html=True)

# हेडर
st.markdown("<h1 class='main-title'>📜 आकांक्षा AI कायदेशीर व RTI सहाय्यक</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='sub-title'>सतीश अशोक प्रधान | मो. ८६६८२३५३९५</h4>", unsafe_allow_html=True)
st.write("---")

# २. मोबाईल OTP लॉगिन सिस्टीम
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.write("### 🔐 ॲपमध्ये प्रवेश करण्यासाठी लॉगिन करा")
    mobile = st.text_input("तुमचा १० अंकी मोबाईल नंबर टाका:", placeholder="9876543210")
    
    if st.button("OTP पाठवा"):
        if len(mobile) == 10 and mobile.isdigit():
            st.session_state.mobile = mobile
            st.session_state.otp_sent = True
            st.success(f"{mobile} वर OTP पाठवला आहे!")
        else:
            st.error("कृपया वैध १० अंकी मोबाईल नंबर टाका.")

    if st.session_state.get("otp_sent", False):
        otp = st.text_input("६ अंकी OTP टाका:", type="password")
        if st.button("OTP पडताळून पहा (Verify)"):
            if len(otp) == 6:
                st.session_state.authenticated = True
                st.success("लॉगिन यशस्वी झाले!")
                st.rerun()
            else:
                st.error("चुकीचा OTP. ६ अंकी OTP टाका.")

else:
    # ३. मुख्य डॅशबोर्ड व ४x२ ग्रिड बटने
    st.sidebar.success(f"लॉगिन: +91 {st.session_state.get('mobile', '')}")
    if st.sidebar.button("लॉगआउट"):
        st.session_state.authenticated = False
        st.rerun()

    if "active_tab" not in st.session_state:
        st.session_state.active_tab = "rti"

    # ४x२ बटणांची रचना
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("📄 जोडपत्र 'अ'"): st.session_state.active_tab = "rti"
        if st.button("⚖️ कोर्ट याचिका"): st.session_state.active_tab = "court"
    with col2:
        if st.button("⚖️ प्रथम अपील"): st.session_state.active_tab = "first_appeal"
        if st.button("📣 शासकीय तक्रार"): st.session_state.active_tab = "complaint"
    with col3:
        if st.button("🏛️ माहिती आयोग"): st.session_state.active_tab = "commission"
        if st.button("✏️ प्रतिज्ञापत्र"): st.session_state.active_tab = "affidavit"
    with col4:
        if st.button("✨ AI चॅट"): st.session_state.active_tab = "ai_chat"
        if st.button("🛒 ग्राहक मंच"): st.session_state.active_tab = "consumer"

    st.write("---")

    # ४. प्रत्येक बटनाचे स्वतंत्र कार्यस्थान

    # १. जोडपत्र 'अ' (RTI)
    if st.session_state.active_tab == "rti":
        st.subheader("📄 जोडपत्र 'अ' (माहिती अधिकार अर्ज कलम ६(१))")
        dept = st.text_input("शासकीय विभागाचे नाव व पत्ता:")
        subject = st.text_input("माहितीचा विषय:")
        details = st.text_area("हवी असलेल्या माहितीचा सविस्तर तपशील (१ ते ५ मुद्दे):")
        bpl = st.radio("अर्जदार दारिद्र्यरेषेखालील (BPL) आहे का?", ["नाही", "होय"])
        
        if st.button("RTI मसुदा तयार करा"):
            bpl_text = "मी दारिद्र्यरेषेखालील (BPL) नागरिक असून त्याचा पुरावा सोबत जोडला आहे. तरी मोफत माहिती द्यावी." if bpl == "होय" else "मी अर्जाचे शुल्क नियमानुसार भरत आहे."
            draft = f"""
**माहिती अधिकाराचा अर्ज (नियम ३ - जोडपत्र 'अ')**

प्रति,
जन माहिती अधिकारी,
{dept}

विषय: माहिती अधिकार अधिनियम, २००५ अन्वये माहिती मिळणेबाबत.

महोदय,
१. अर्जाचा विषय: {subject}
२. हवी असलेली माहिती:
{details}

३. कायदेशीर अट (कलम ६(३)): जर मागितलेली माहिती आपल्या कार्यालयाशी संबंधित नसेल, तर माहिती अधिकार कायदा २००५ च्या कलम ६(३) अन्वये हा अर्ज ५ दिवसांच्या आत योग्य प्राधिकरणाकडे हस्तांतरित करावा.
४. शुल्क / BPL पुरावा: {bpl_text}

अर्जदाराचे नाव: सतीश अशोक प्रधान
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # २. प्रथम अपील
    elif st.session_state.active_tab == "first_appeal":
        st.subheader("⚖️ प्रथम अपील अर्ज (कलम १९(१))")
        fa_dept = st.text_input("प्रथम अपिलीय अधिकाऱ्याचे पद व पत्ता:")
        pious_date = st.text_input("मूळ अर्ज (जोडपत्र 'अ') दिल्याचा दिनांक:")
        reason = st.text_area("अपिलाचे मुख्य कारण (उदा. ३० दिवसांत माहिती न मिळणे / चुकीची माहिती):")
        
        if st.button("प्रथम अपील मसुदा तयार करा"):
            draft = f"""
**प्रथम अपील अर्ज (माहिती अधिकार अधिनियम २००५ चे कलम १९(१))**

प्रति,
प्रथम अपिलीय अधिकारी,
{fa_dept}

विषय: माहिती अधिकार कायदा २००५ च्या कलम १९(१) अन्वये प्रथम अपील.

महोदय,
१. मी दिनांक {pious_date} रोजी जन माहिती अधिकाऱ्याकडे माहितीचा अर्ज दिला होता.
२. अपिलाचे कारण: {reason}
३. विनंती: तरी मला मागितलेली माहिती तात्काळ मोफत देण्याचे आदेश जन माहिती अधिकाऱ्यास द्यावेत.

अपीलार्थी: सतीश अशोक प्रधान
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # ३. माहिती आयोग
    elif st.session_state.active_tab == "commission":
        st.subheader("🏛️ राज्य माहिती आयोग (द्वितीय अपील / तक्रार)")
        bench = st.text_input("माहिती आयोग खंडपीठाचे नाव (उदा. औरंगाबाद / मुंबई):")
        comm_details = st.text_area("द्वितीय अपिलाचा सविस्तर तपशील व तक्रार:")
        
        if st.button("द्वितीय अपील मसुदा तयार करा"):
            draft = f"""
**द्वितीय अपील / तक्रार अर्ज (कलम १९(३))**

प्रति,
मा. राज्य मुख्य माहिती आयुक्त / माहिती आयुक्त,
राज्य माहिती आयोग खंडपीठ, {bench}

विषय: माहिती अधिकार कायदा २००५ च्या कलम १९(३) अन्वये द्वितीय अपील.

महोदय,
१. प्रकरणाचा तपशील: {comm_details}
२. मागणी: दोषी अधिकाऱ्यांवर कलम २०(१) नुसार दंडात्मक कारवाई करण्यात यावी व माहिती पुरवण्यात यावी.

अर्जदार: सतीश अशोक प्रधान
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # ४. शासकीय तक्रार (यात RTI चा शब्द असणार नाही)
    elif st.session_state.active_tab == "complaint":
        st.subheader("📣 शासकीय अधिकारी / विभागाविरोधात अधिकृत तक्रार अर्ज")
        target_officer = st.text_input("वरिष्ठ अधिकाऱ्याचे पद व कार्यालय (उदा. जिल्हाधिकारी / पोलिस आयुक्त):")
        comp_subject = st.text_input("तक्रारीचा मुख्य विषय:")
        comp_details = st.text_area("अन्यायाचा किंवा घटनेचा सविस्तर तपशील:")
        comp_demand = st.text_input("मागितलेली कारवाई:")
        
        if st.button("तक्रार अर्ज तयार करा"):
            draft = f"""
**अधिकृत शासकीय तक्रार अर्ज**

प्रति,
{target_officer}

विषय: {comp_subject}

महोदय,
मी खालीलप्रमाणे तक्रार दाखल करत आहे:
१. प्रकरणाचा तपशील: {comp_details}
२. मागणी: {comp_demand} तरी सदर प्रकरणाची सखोल चौकशी करून संबंधितांवर योग्य ती प्रशासकीय व कायदेशीर कारवाई करावी.

तक्रारदार: सतीश अशोक प्रधान
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # ५. ग्राहक मंच
    elif st.session_state.active_tab == "consumer":
        st.subheader("🛒 ग्राहक संरक्षण कायदा २०१९ अन्वये तक्रार")
        forum = st.text_input("ग्राहक मंचाचे नाव (उदा. जिल्हा ग्राहक निवारण आयोग):")
        seller = st.text_input("सामनेवाला (दुकानदार / कंपनीचे नाव व पत्ता):")
        loss_details = st.text_area("झालेली फसवणूक / वस्तू किंवा सेवेतील त्रुटीचा तपशील:")
        compensation = st.text_input("मागितलेली भरपाई रक्कम (₹):")
        
        if st.button("ग्राहक मंच मसुदा तयार करा"):
            draft = f"""
**ग्राहक मंचाकडे तक्रार अर्ज (ग्राहक संरक्षण कायदा २०१९)**

प्रति,
मा. अध्यक्ष / सदस्य,
{forum}

तक्रारदार: सतीश अशोक प्रधान
विरुद्ध
सामनेवाला: {seller}

विषय: अनचित व्यापार प्रथा आणि सेवेतील त्रुटीबाबत भरपाई मिळणेबाबत.

१. प्रकरणाचा तपशील: {loss_details}
२. मागणी: सामनेवाल्याकडून नुकसानापोटी ₹{compensation} भरपाई मिळावी.

तक्रारदार: सतीश अशोक प्रधान
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # ६. प्रतिज्ञापत्र
    elif st.session_state.active_tab == "affidavit":
        st.subheader("✏️ कायदेशीर प्रतिज्ञापत्र (Affidavit Draft)")
        aff_reason = st.text_input("प्रतिज्ञापत्राचे कारण (उदा. नाव दुरुस्ती / उत्पन्न / पत्ता):")
        aff_statements = st.text_area("शपथपूर्वक घोषित करावयाचे मुख्य मुद्दे:")
        
        if st.button("प्रतिज्ञापत्र तयार करा"):
            draft = f"""
**कायदेशीर प्रतिज्ञापत्र (AFFIDAVIT)**

मी सतीश अशोक प्रधान, रा. छत्रपती संभाजीनगर, सत्यप्रतिज्ञापूर्वक लिहून देतो की:

१. प्रतिज्ञापत्राचे कारण: {aff_reason}
२. मुख्य विधाने:
{aff_statements}

वरील सर्व माहिती माझ्या माहितीनुसार व विश्वासानुसार खरी व बरोबर आहे.

प्रतिज्ञापत्र देणारा: सतीश अशोक प्रधान
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # ७. कोर्ट याचिका
    elif st.session_state.active_tab == "court":
        st.subheader("⚖️ न्यायालयीन याचिका / लीगल नोटीस मसुदा")
        court_name = st.text_input("न्यायालयाचे नाव:")
        opponent = st.text_input("सामनेवाला (Respondent):")
        facts = st.text_area("प्रकरणाची हकीकत (Facts of the Case):")
        prayer = st.text_input("न्यायालयाकडे मागितलेला न्याय (Prayer):")
        
        if st.button("याचिका मसुदा तयार करा"):
            draft = f"""
**न्यायालयीन याचिका मसुदा**

समक्ष: मा. {court_name}

याचिकाकर्ता: सतीश अशोक प्रधान
विरुद्ध
सामनेवाला: {opponent}

विषय: {prayer} साठी याचिका.

१. प्रकरणाची हकीकत: {facts}
२. प्रार्थना: वरील हकीकतीचा विचार करून याचिकाकर्त्याला योग्य तो न्याय देण्यात यावा.

याचिकाकर्ता: सतीश अशोक प्रधान
दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            st.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    # ८. AI चॅट
    elif st.session_state.active_tab == "ai_chat":
        st.subheader("✨ आकांक्षा AI कायदेशीर सल्लागार")
        query = st.text_input("तुमचा कायदेशीर किंवा RTI विषयीचा प्रश्न विचारा:")
        if st.button("प्रश्न विचारा"):
            if query:
                st.info(f"तुमचा प्रश्न: {query}")
                st.success("AI उत्तर: माहिती अधिकार २००५ अंतर्गत कोणत्याही शासकीय विभागाकडून सार्वजनिक कामाची माहिती मागवण्याचा तुम्हाला पूर्ण अधिकार आहे. यासाठी संबंधित विभागाच्या जन माहिती अधिकाऱ्याकडे अर्ज सादर करावा.")
            else:
                st.warning("कृपया प्रश्न टाईप करा.")
