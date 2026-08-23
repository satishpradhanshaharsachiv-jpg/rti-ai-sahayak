import streamlit as st

# १. पेज कॉन्फिगरेशन
st.set_page_config(page_title="आकांक्षा RTI AI", layout="wide")

# २. क्लिक केलेल्या बटनाचा अर्ज ओळखणे
query_params = st.query_params
current_form = query_params.get("form", "jodpatra_a")

# ३. ३D डिझाईन आणि सुंदर रंगांसाठी CSS
st.markdown("""
<style>
/* हेडर बॅनर */
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
    font-size: 19px;
    font-weight: bold;
    margin-bottom: 6px;
    line-height: 1.3;
}
.header-subtitle {
    color: #ff7675;
    font-size: 13px;
    font-weight: bold;
    margin-bottom: 8px;
}
.header-divider {
    border-top: 1px dashed #666;
    margin: 8px 0;
}
.header-footer {
    color: #ffffff;
    font-size: 13px;
}

/* २x४ बटनांची पक्की चौकट (Grid) */
.btn-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    margin-bottom: 25px;
}
@media (max-width: 600px) {
    .btn-container {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* कधीही न बिघडणारी ३D बटणे */
.custom-btn {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 12px 4px;
    text-decoration: none !important;
    color: white !important;
    font-weight: bold;
    font-size: 13px;
    border-radius: 12px;
    text-align: center;
    box-shadow: inset 0px 2px 3px rgba(255, 255, 255, 0.5), 0px 5px 8px rgba(0, 0, 0, 0.35);
    border-top: 1px solid rgba(255, 255, 255, 0.4);
    border-bottom: 3px solid rgba(0, 0, 0, 0.4);
    transition: transform 0.1s;
}
.custom-btn:active {
    transform: translateY(2px);
}

/* चमकणारे ३D कलर्स */
.btn-green { background: linear-gradient(180deg, #11998e 0%, #38ef7d 100%); }
.btn-orange { background: linear-gradient(180deg, #FF416C 0%, #FF4B2B 100%); }
.btn-royal-blue { background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%); }
.btn-3d-blue { background: linear-gradient(180deg, #00c6ff 0%, #0072ff 100%); }
.btn-purple { background: linear-gradient(180deg, #8E2DE2 0%, #4A00E0 100%); }
.btn-red { background: linear-gradient(180deg, #e52d27 0%, #b31217 100%); }
.btn-gold { background: linear-gradient(180deg, #ffe066 0%, #d4af37 50%, #996515 100%); color: #000 !important; text-shadow: none; }
.btn-cyan { background: linear-gradient(180deg, #00B4DB 0%, #0083B0 100%); }
</style>
""", unsafe_allow_html=True)

# ४. हेडर बॅनर आणि ३D बटनांचा HTML कोड
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

# ५. क्लिक केलेल्या बटनानुसार उघडणारा फॉर्म (PDF नमुन्यांनुसार)
if current_form == "jodpatra_a":
    st.info("📋 जोडपत्र 'अ' (माहितीचा अर्ज - नियम ३) - ₹१० कोर्ट फी स्टॅम्प")
    with st.form("form_a"):
        st.text_input("जन माहिती अधिकाऱ्याच्या कार्यालयाचे नाव व पत्ता")
        st.text_input("अर्जदाराचे संपूर्ण नाव")
        st.text_area("अर्जदाराचा पूर्ण पत्ता")
        st.text_input("माहितीचा विषय")
        st.text_input("माहितीचा कालावधी")
        st.text_area("हव्या असलेल्या माहितीचे वर्णन")
        st.selectbox("माहिती कशी हवी आहे?", ["टपालाद्वारे", "व्यक्तिशः"])
        st.form_submit_button("📄 A4 साईज PDF अर्ज तयार करा")

elif current_form == "first_appeal":
    st.info("📋 जोडपत्र 'ब' (प्रथम अपील अर्ज - नियम ५(१)) - ₹२० कोर्ट फी स्टॅम्प")
    with st.form("form_b"):
        st.text_input("प्रथम अपीलीय अधिकाऱ्याचे पदनाम व पत्ता")
        st.text_input("अपीलकाराचे संपूर्ण नाव")
        st.text_area("अपीलकाराचा पूर्ण पत्ता व संपर्क")
        st.text_input("संबंधित जन माहिती अधिकाऱ्याचा तपशील")
        st.text_area("अपील करण्याचे कारण / प्रयोजन")
        st.form_submit_button("⚖️ प्रथम अपील A4 PDF तयार करा")

elif current_form == "second_appeal":
    st.info("📋 जोडपत्र 'क' (द्वितिय अपील अर्ज - नियम ५(२) - माहिती आयोग)")
    with st.form("form_c"):
        st.text_input("मा. माहिती आयुक्त व राज्य माहिती आयोग कार्यालयाचा पत्ता")
        st.text_input("अपीलकाराचे नाव व पूर्ण पत्ता")
        st.text_input("संबंधित जन माहिती अधिकाऱ्याचा तपशील")
        st.text_input("प्रथम अपीलीय प्राधिकाऱ्याचा तपशील")
        st.text_area("द्वितीय अपील करण्याचे प्रयोजन")
        st.form_submit_button("🏛️ द्वितीय अपील A4 PDF तयार करा")

elif current_form == "rti_portal":
    st.info("🌐 आरटीआय ऑनलाईन पोर्टल सहाय्य")
    st.write("• **महाराष्ट्र आरटीआय पोर्टल:** १५० शब्दांची मर्यादा.")
    st.write("• **केंद्रीय आरटीआय पोर्टल:** ५०० शब्दांची मर्यादा.")
