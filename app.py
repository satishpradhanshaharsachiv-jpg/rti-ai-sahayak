import streamlit as st

# १. बटनांची स्टाइल (CSS) - जवळ-जवळ आणि रंगीबेरंगी लेआउटसाठी
st.markdown("""
<style>
/* बटनांची चौकट (Grid) */
.btn-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr); /* एका रांगेत ४ बटणे */
    gap: 8px; /* बटनांमधील अंतर कमी ठेवण्यासाठी */
    margin-top: 10px;
    margin-bottom: 20px;
}

/* मोबाईलवर २ बटणे आणि डेस्कटॉप स्विचवर ४ बटणे ऑटो-फिट करण्यासाठी */
@media (max-width: 600px) {
    .btn-container {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* बटनांची मूळ डिझाईन */
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

/* चंचमीत आणि चमकणारे वेगवेगळे कलर्स */
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

# २. रंगीबेरंगी बटनांचा HTML कोड
buttons_html = """
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

# हे लिहिणे अत्यंत गरजेचे आहे जेणेकरून कोड मजकुरासारखा दिसणार नाही
st.markdown(buttons_html, unsafe_allow_html=True)
