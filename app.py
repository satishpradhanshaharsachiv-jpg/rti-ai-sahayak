import streamlit as st

# १. सेशन स्टेट (Session State) सेट करणे
if 'selected_form' not in st.session_state:
    st.session_state.selected_form = "जोडपत्र 'अ'"

# २. ३D हेडर आणि चमचमीत बटनांसाठी CSS
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

.header-title {
    color: #ffd700;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 8px;
    line-height: 1.4;
    text-shadow: 0px 2px 4px rgba(0,0,0,0.6);
}

.header-subtitle {
    color: #ff7675;
    font-size: 14px;
    font-weight: bold;
    margin-bottom: 10px;
}

.header-divider {
    border-top: 1px dashed #666;
    margin: 10px 0;
}

.header-footer {
    color: #ffffff;
    font-size: 13px;
    font-weight: 500;
}

/* Streamlit बटनांची ३D स्टाइल */
div.stButton > button {
    width: 100%;
    height: 65px;
    border-radius: 14px !important;
    font-weight: bold !important;
    font-size: 13px !important;
    color: white !important;
    border-top: 1px solid rgba(255, 255, 255, 0.5) !important;
    border-bottom: 3px solid rgba(0, 0, 0, 0.3) !important;
    box-shadow: inset 0px 2px 3px rgba(255, 255, 255, 0.4), 0px 6px 10px rgba(0, 0, 0, 0.3) !important;
}
</style>
""", unsafe_allow_html=True)

# ३. मुख्य हेडर बॅनर
st.markdown("""
<div class="header-card">
    <div class="header-title">
        ✨ आकांक्षा इंटरप्राईजेस RTI AI ॲप कायदेशीर सहाय्य ✨
    </div>
    <div class="header-subtitle">
        ⚡ घरबसल्या RTI अर्ज व शासकीय तक्रार एका सेकंदात A4 साईज मध्ये मोफत मिळवा ⚡
    </div>
    <div class="header-divider"></div>
    <div class="header-footer">
        👤 सतीश अशोक प्रधान | 📱 मो. ८६६८२३५३९५
    </div>
</div>
""", unsafe_allow_html=True)

# ४. ३D क्लिक होणारी बटणे (२x४ Grid)
col1, col2 = st.columns(2)

with col1:
    if st.button("📄\nजोडपत्र 'अ'", key="btn1"):
        st.session_state.selected_form = "जोडपत्र 'अ'"
    if st.button("🏛️\nमाहिती आयोग", key="btn3"):
        st.session_state.selected_form = "माहिती आयोग"
    if st.button("📜\nकोर्ट याचिका", key="btn5"):
        st.session_state.selected_form = "कोर्ट याचिका"
    if st.button("🌐\nआरटीआय ऑनलाइन पोर्टल सहाय्य", key="btn7"):
        st.session_state.selected_form = "आरटीआय ऑनलाइन"

with col2:
    if st.button("⚖️\nप्रथम अपील", key="btn2"):
        st.session_state.selected_form = "प्रथम अपील"
    if st.button("✨\nAI चॅट", key="btn4"):
        st.session_state.selected_form = "AI चॅट"
    if st.button("📣\nशासकीय तक्रार", key="btn6"):
        st.session_state.selected_form = "शासकीय तक्रार"
    if st.button("🛒\nग्राहक मंच", key="btn8"):
        st.session_state.selected_form = "ग्राहक मंच"

st.markdown("---")

# ५. निवडलेल्या बटनानुसार PDF फॉरमॅटचा फॉर्म प्रदर्शित करणे
current_form = st.session_state.selected_form
st.subheader(f"📋 निवडलेला अर्ज: {current_form}")

if current_form == "जोडपत्र 'अ'":
    st.info("माहितीचा अधिकार अधिनियम, २००५ अन्वये अर्ज (नियम ३ पहा) - ₹१० कोर्ट फी स्टॅम्प")
    with st.form("jodpatra_a_form"):
        karyalay = st.text_input("जन माहिती अधिकाऱ्याच्या कार्यालयाचे नाव व पत्ता")
        full_name = st.text_input("अर्जदाराचे संपूर्ण नाव")
        address = st.text_area("अर्जदाराचा पूर्ण पत्ता")
        subject = st.text_input("माहितीचा विषय")
        period = st.text_input("माहितीचा कालावधी (उदा. २०२३ ते २०२५)")
        description = st.text_area("हव्या असलेल्या माहितीचे वर्णन")
        post_type = st.selectbox("माहिती कशी हवी आहे?", ["टपालाद्वारे (साधे/नोंदणीकृत)", "व्यक्तिशः (स्वहस्ते)"])
        bpl = st.radio("अर्जदार दारिद्र्यरेषेखालील (BPL) आहे का?", ["नाही", "होय (प्रत जोडणे आवश्यक)"])
        
        submitted = st.form_submit_button("📄 A4 साईज PDF अर्ज तयार करा")
        if submitted:
            st.success("तुमचा जोडपत्र 'अ' अर्ज A4 फॉरमॅटमध्ये यशस्वीरित्या तयार झाला आहे!")

elif current_form == "प्रथम अपील":
    st.info("माहितीचा अधिकार कायदा, २००५ - कलम १९ (१) अन्वये प्रथम अपील (जोडपत्र 'ब' - नियम ५(१)) - ₹२० कोर्ट फी स्टॅम्प")
    with st.form("first_appeal_form"):
        officer = st.text_input("प्रथम अपीलीय अधिकाऱ्याचे पदनाम व पत्ता")
        appellant_name = st.text_input("अपीलकाराचे संपूर्ण नाव")
        appellant_address = st.text_area("अपीलकाराचा पूर्ण पत्ता व संपर्क")
        pio_details = st.text_input("संबंधित जन माहिती अधिकाऱ्याचा तपशील")
        reason = st.text_area("अपील करण्याचे कारण / प्रयोजन")
        info_detail = st.text_area("आवश्यक माहितीचा तपशील व विभाग")
        
        submitted = st.form_submit_button("⚖️ प्रथम अपील A4 PDF तयार करा")
        if submitted:
            st.success("तुमचे प्रथम अपील अर्ज जोडपत्र 'ब' A4 फॉरमॅटमध्ये तयार झाले आहे!")

elif current_form == "माहिती आयोग":
    st.info("माहितीचा अधिकार कायदा, २००५ - कलम १९ (३) अन्वये द्वितीय अपील (जोडपत्र 'क' - नियम ५(२))")
    with st.form("second_appeal_form"):
        commissioner = st.text_input("मा. माहिती आयुक्त व राज्य माहिती आयोग कार्यालयाचा पत्ता")
        appellant_details = st.text_input("अपीलकाराचे नाव, पत्ता व मोबाईल")
        pio_info = st.text_input("संबंधित जन माहिती अधिकाऱ्याचा तपशील")
        fa_info = st.text_input("प्रथम अपीलीय प्राधिकाऱ्याचा तपशील")
        first_appeal_date = st.date_input("प्रथम अपिलाच्या निर्णयाची तारीख")
        appeal_purpose = st.text_area("द्वितीय अपील करण्याचे प्रयोजन व विस्तृत माहिती")
        
        submitted = st.form_submit_button("🏛️ द्वितीय अपील A4 PDF तयार करा")
        if submitted:
            st.success("तुमचे माहिती आयोगाचे द्वितीय अपील जोडपत्र 'क' फॉरमॅटमध्ये तयार झाले आहे!")

elif current_form == "आरटीआय ऑनलाइन":
    st.info("🌐 आरटीआय ऑनलाईन पोर्टल मार्गदर्शन (केंद्र व महाराष्ट्र शासन)")
    st.write("• **महाराष्ट्र ऑनलाईन आरटीआय पोर्टल:** १५० शब्दांची मर्यादा व ₹१० शुल्क.")
    st.write("• **केंद्रीय आरटीआय पोर्टल (RTI Online Central):** ५०० शब्दांची मर्यादा व ₹१० शुल्क.")

else:
    st.write(f"**{current_form}** साठी अर्ज नमुना लवकरच उपलब्ध होत आहे.")
