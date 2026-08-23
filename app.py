import streamlit as st

# १. सर्व स्टाइल (बॅनर आणि बटणांसाठी)
st.markdown("""
<style>
/* १. स्क्रीनशॉटनुसार हेडर बॅनर डिझाईन */
.header-card {
    background: linear-gradient(135deg, #0f172a, #1e1b4b);
    border: 2px solid #f1c40f;
    border-radius: 16px;
    padding: 16px 12px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.4);
    margin-bottom: 20px;
}

.header-title {
    color: #f1c40f;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 8px;
    line-height: 1.4;
}

.header-subtitle {
    color: #ff7675;
    font-size: 14px;
    font-weight: bold;
    margin-bottom: 10px;
}

.header-divider {
    border-top: 1px dashed #555;
    margin: 10px 0;
}

.header-footer {
    color: #ffffff;
    font-size: 13px;
    font-weight: 500;
}

/* २. रंगीबेरंगी बटनांची चौकट (Grid) */
.btn-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    margin-top: 10px;
    margin-bottom: 20px;
}

/* मोबाईल आणि क्रोम डेस्कटॉप स्विच दोन्हीवर ऑटो-फिट */
@media (max-width: 600px) {
    .btn-container {
        grid-template-columns: repeat(2, 1fr);
    }
}

.custom-btn {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 12px 6px;
    text-decoration: none !important;
    color: white !important;
    font-weight: bold;
    font-size: 14px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.25);
    transition: transform 0.2s;
}

/* चंचमीत आणि आकर्षक कलर्स */
.btn-gold { background: linear-gradient(135deg, #BF953F, #FCF6BA, #B38728, #FBF5B7); color: #000 !important; }
.btn-green { background: linear-gradient(135deg, #11998e, #38ef7d); }
.btn-orange { background: linear-gradient(135deg, #FF416C, #FF4B2B); }
.btn-blue { background: linear-gradient(135deg, #3A1C71, #D76D77, #FFAF7B); }
.btn-purple { background: linear-gradient(135deg, #8E2DE2, #4A00E0); }
.btn-red { background: linear-gradient(135deg, #e52d27, #b31217); }
.btn-dark { background: linear-gradient(135deg, #141E30, #243B55); }
.btn-cyan { background: linear-gradient(135deg, #00B4DB, #0083B0); }
</style>
""", unsafe_allow_html=True)

# २. हेडर बॅनर आणि बटनांचा HTML कोड
full_app_html = """
<!-- वरचा हेडर बॅनर -->
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

<!-- खालील रंगीबेरंगी बटणे -->
<div class="btn-container">
    <a href="#" class="custom-btn btn-green">📄<br>जोडपत्र 'अ'</a>
    <a href="#" class="custom-btn btn-orange">⚖️<br>प्रथम अपील</a>
    <a href="#" class="custom-btn btn-dark">🏛️<br>माहिती आयोग</a>
    <a href="#" class="custom-btn btn-blue">✨<br>AI चॅट</a>
    <a href="#" class="custom-btn btn-purple">📜<br>कोर्ट याचिका</a>
    <a href="#" class="custom-btn btn-red">📣<br>शासकीय तक्रार</a>
    <a href="#" class="custom-btn btn-gold">✏️<br>प्रतिज्ञापत्र</a>
    <a href="#" class="custom-btn btn-cyan">🛒<br>ग्राहक मंच</a>
</div>
"""

# ३. ॲपमध्ये प्रदर्शित करण्यासाठी
st.markdown(full_app_html, unsafe_allow_html=True)
