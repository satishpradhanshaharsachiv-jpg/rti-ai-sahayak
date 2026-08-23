import streamlit as st

# १. ३D आणि चमचमीत (Glossy/Metallic) बटनांसाठी CSS
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

/* बटनांची Grid (मोबाईल व डेस्कटॉप फिट) */
.btn-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin-top: 10px;
    margin-bottom: 20px;
}

@media (max-width: 600px) {
    .btn-container {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* ३D बटनांची डिझाईन (3D Glossy Effect) */
.custom-btn {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 12px 6px;
    text-decoration: none !important;
    color: white !important;
    font-weight: bold;
    font-size: 13px;
    border-radius: 14px;
    text-align: center;
    /* ३D खोली आणि शाइन देणारा शेडो प्रभाव */
    box-shadow: inset 0px 2px 3px rgba(255, 255, 255, 0.6), 0px 6px 10px rgba(0, 0, 0, 0.35);
    border-top: 1px solid rgba(255, 255, 255, 0.5);
    border-bottom: 3px solid rgba(0, 0, 0, 0.3);
    text-shadow: 0px 1px 2px rgba(0, 0, 0, 0.7);
}

/* ३D चमचमीत कलर्स (Shiny 3D Gradients) */
.btn-gold { 
    background: linear-gradient(180deg, #ffe066 0%, #d4af37 50%, #996515 100%); 
    color: #111111 !important; 
    text-shadow: none;
}
.btn-green { 
    background: linear-gradient(180deg, #52c234 0%, #061700 100%); 
}
.btn-orange { 
    background: linear-gradient(180deg, #ff7e5f 0%, #feb47b 50%, #d9381e 100%); 
}
.btn-royal-blue { 
    background: linear-gradient(180deg, #3a7bd5 0%, #3a6073 100%); 
}
.btn-purple { 
    background: linear-gradient(180deg, #b92b27 0%, #1565c0 100%); 
}
.btn-red { 
    background: linear-gradient(180deg, #ff4e50 0%, #f9d423 100%); 
    color: #111 !important;
    text-shadow: none;
}
.btn-3d-blue { 
    background: linear-gradient(180deg, #00c6ff 0%, #0072ff 100%); 
}
.btn-cyan { 
    background: linear-gradient(180deg, #11998e 0%, #38ef7d 100%); 
}
</style>
""", unsafe_allow_html=True)

# २. ३D हेडर आणि नवीन बटनांचा HTML कोड
full_app_html = """
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

<div class="btn-container">
    <a href="#" class="custom-btn btn-green">📄<br>जोडपत्र 'अ'</a>
    <a href="#" class="custom-btn btn-orange">⚖️<br>प्रथम अपील</a>
    <a href="#" class="custom-btn btn-royal-blue">🏛️<br>माहिती आयोग</a>
    <a href="#" class="custom-btn btn-3d-blue">✨<br>AI चॅट</a>
    <a href="#" class="custom-btn btn-purple">📜<br>कोर्ट याचिका</a>
    <a href="#" class="custom-btn btn-red">📣<br>शासकीय तक्रार</a>
    <a href="#" class="custom-btn btn-gold">🌐<br>आरटीआय ऑनलाइन पोर्टल सहाय्य</a>
    <a href="#" class="custom-btn btn-cyan">🛒<br>ग्राहक मंच</a>
</div>
"""

# ३. स्क्रीनवर दाखवण्यासाठी
st.markdown(full_app_html, unsafe_allow_html=True)
